// ... importaciones
import React, { useState, useEffect } from "react";
import DiagnosticoCard from "./DiagnosticoCard";
import axios from "axios";

function Tabs({ usuario }) {
  const [activeTab, setActiveTab] = useState("opcion1");
  const [diagnosticos, setDiagnosticos] = useState([]);
  const [idPaciente, setIdPaciente] = useState("");
  const [entrada, setEntrada] = useState("");
  const [fecha] = useState(new Date().toISOString().split("T")[0]);
  const [mensaje, setMensaje] = useState("");

  const [selectedDiagnosticos, setSelectedDiagnosticos] = useState([]);
  const [resumenGenerado, setResumenGenerado] = useState("");
  const [historialResumenes, setHistorialResumenes] = useState([]);
  const [cargandoResumenes, setCargandoResumenes] = useState(false);
  const [loadingResumen, setLoadingResumen] = useState(false);
  const [savingResumen, setSavingResumen] = useState(false);

  const cargarDiagnosticos = async () => {
    try {
      const response = await axios.post("http://localhost:5000/diagnosticos", {
        id_usuario: usuario.id_usuario,
      });
      setDiagnosticos(response.data);
    } catch (error) {
      console.error("Error al cargar diagnósticos:", error);
    }
  };

  const obtenerHistorialResumenes = async () => {
    try {
      setCargandoResumenes(true);
      const response = await axios.post("http://localhost:5000/resumenes", {
        id_usuario: usuario.id_usuario,
      });
      setHistorialResumenes(response.data);
    } catch (error) {
      console.error("Error al obtener resúmenes:", error);
    } finally {
      setCargandoResumenes(false);
    }
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
    if (tab === "opcion1") {
      cargarDiagnosticos();
    } else if (tab === "opcion2") {
      cargarDiagnosticos();
      if (usuario.tipo_u !== "m") {
        obtenerHistorialResumenes();
      }
    }
  };

  const handleSubmit = async () => {
    if (!idPaciente || !entrada) {
      setMensaje("Completa todos los campos.");
      return;
    }

    try {
      await axios.post("http://localhost:5000/diagnosticos/entrada", {
        id_usuario: usuario.id_usuario,
        id_paciente: idPaciente,
        d_especialidad: usuario.d_especialidad,
        fecha,
        entrada,
      });

      setMensaje("Diagnóstico guardado correctamente.");
      setIdPaciente("");
      setEntrada("");
      cargarDiagnosticos();
    } catch (error) {
      console.error("Error al guardar el diagnóstico:", error);
      setMensaje("Hubo un error al guardar el diagnóstico.");
    }
  };

  const toggleDiagnostico = (diag) => {
    setSelectedDiagnosticos((prev) => {
      const yaSeleccionado = prev.some((d) => d.id === diag.id_diagnostico);
      if (yaSeleccionado) {
        return prev.filter((d) => d.id !== diag.id_diagnostico);
      } else {
        return [...prev, { id: diag.id_diagnostico, texto: diag.diagnostico }];
      }
    });
  };

  const generarResumen = async () => {
    if (selectedDiagnosticos.length === 0) {
      alert("Selecciona al menos un diagnóstico.");
      return;
    }

    const textosSeleccionados = selectedDiagnosticos
      .map((d) => d.texto?.trim())
      .filter((texto) => texto && texto.length > 0);

    if (textosSeleccionados.length === 0) {
      alert("Los diagnósticos seleccionados no tienen contenido.");
      return;
    }

    const texto = textosSeleccionados.join(". ");
    console.log("Texto a resumir:", texto, `\nLongitud: ${texto.length}`);

    setLoadingResumen(true);

    try {
      const response = await axios.post(
        "http://localhost:5000/resumenes/generar",
        { texto }
      );
      setResumenGenerado(response.data.resumen);
    } catch (error) {
      console.error("Error al generar resumen:", error);
      alert("Hubo un error al generar el resumen.");
    } finally {
      setLoadingResumen(false);
    }
  };

  const guardarResumen = async () => {
    setSavingResumen(true);
    try {
      console.log("Resumen a guardar:", resumenGenerado);
      await axios.post("http://localhost:5000/resumenes/entrada", {
        resumen: resumenGenerado,
        id_usuario: usuario.id_usuario,
      });
      setResumenGenerado("");
      obtenerHistorialResumenes();
    } catch (error) {
      console.error("Error al guardar resumen:", error);
      alert("Hubo un error al guardar el resumen.");
    } finally {
      setSavingResumen(false);
    }
  };

  const cancelarResumen = () => {
    setResumenGenerado("");
    setSelectedDiagnosticos([]);
  };

  useEffect(() => {
    cargarDiagnosticos();
  }, []);

  return (
    <>
      <ul className="nav nav-tabs mb-3">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === "opcion1" ? "active" : ""}`}
            onClick={() => handleTabChange("opcion1")}
          >
            Historial de Diagnósticos
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === "opcion2" ? "active" : ""}`}
            onClick={() => handleTabChange("opcion2")}
          >
            {usuario.tipo_u === "m" ? "Nueva Consulta" : "Resumen"}
          </button>
        </li>
      </ul>

      {activeTab === "opcion1" && (
        <>
          {diagnosticos.length > 0 ? (
            diagnosticos.map((diag, idx) => (
              <DiagnosticoCard
                key={idx}
                diagnostico={diag}
                tipoUsuario={usuario.tipo_u}
                usuarioActual={usuario.id_usuario}
              />
            ))
          ) : (
            <p>No hay diagnósticos registrados.</p>
          )}
        </>
      )}

      {activeTab === "opcion2" && usuario.tipo_u === "m" && (
        <div className="card p-4 shadow-sm">
          <h5 className="mb-3">Registrar nuevo diagnóstico</h5>
          <div className="mb-3">
            <label>ID del paciente</label>
            <input
              type="text"
              className="form-control"
              value={idPaciente}
              onChange={(e) => setIdPaciente(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label>Fecha</label>
            <input
              type="text"
              className="form-control"
              value={fecha}
              readOnly
            />
          </div>
          <div className="mb-3">
            <label>Diagnóstico</label>
            <textarea
              className="form-control"
              rows={4}
              value={entrada}
              onChange={(e) => setEntrada(e.target.value)}
            ></textarea>
          </div>
          {mensaje && <div className="alert alert-info">{mensaje}</div>}
          <button className="btn btn-success" onClick={handleSubmit}>
            Guardar diagnóstico
          </button>
        </div>
      )}

      {activeTab === "opcion2" && usuario.tipo_u !== "m" && (
        <div className="card p-4 shadow-sm">
          <h5 className="mb-3">Selecciona diagnósticos para resumir</h5>
          {diagnosticos.length > 0 ? (
            diagnosticos.map((diag, idx) => {
              const estaSeleccionado = selectedDiagnosticos.some(
                (d) => d.id === diag.id_diagnostico
              );
              return (
                <div key={idx} className="form-check mb-2">
                  <input
                    type="checkbox"
                    className="form-check-input"
                    id={`check-${idx}`}
                    checked={estaSeleccionado}
                    onChange={() => toggleDiagnostico(diag)}
                  />
                  <label className="form-check-label" htmlFor={`check-${idx}`}>
                    {diag.diagnostico?.slice(0, 100) ||
                      "Diagnóstico sin entrada..."}
                  </label>
                </div>
              );
            })
          ) : (
            <p>No hay diagnósticos disponibles.</p>
          )}

          <button
            className="btn btn-primary mt-3"
            onClick={generarResumen}
            disabled={loadingResumen}
          >
            {loadingResumen ? (
              <>
                <span
                  className="spinner-border spinner-border-sm me-2"
                  role="status"
                  aria-hidden="true"
                ></span>
                Generando resumen...
              </>
            ) : (
              "Generar resumen"
            )}
          </button>

          {resumenGenerado && (
            <div className="mt-4">
              <h6>Resumen generado:</h6>
              <p>{resumenGenerado}</p>
              <button
                className="btn btn-success mt-2"
                onClick={guardarResumen}
                disabled={savingResumen}
              >
                {savingResumen ? (
                  <>
                    <span
                      className="spinner-border spinner-border-sm me-2"
                      role="status"
                      aria-hidden="true"
                    ></span>
                    Guardando...
                  </>
                ) : (
                  "Guardar resumen"
                )}
              </button>
              <button
                className="btn btn-secondary mt-2 ms-2"
                onClick={cancelarResumen}
              >
                Cancelar resumen
              </button>
            </div>
          )}

          <hr className="my-4" />
          <h5>Historial de resúmenes</h5>
          {cargandoResumenes ? (
            <div className="d-flex align-items-center">
              <span
                className="spinner-border spinner-border-sm me-2"
                role="status"
                aria-hidden="true"
              ></span>
              Cargando...
            </div>
          ) : historialResumenes.length > 0 ? (
            historialResumenes.map((r, i) => (
              <div key={i} className="card mb-2 p-3">
                <strong>{r.fecha}</strong>
                <p>{r.resumen}</p>
              </div>
            ))
          ) : (
            <p>No hay resúmenes guardados aún.</p>
          )}
        </div>
      )}
    </>
  );
}

export default Tabs;
