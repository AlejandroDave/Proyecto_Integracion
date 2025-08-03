import React, { useEffect, useState } from "react";
import Diagnostico from "./DiagnosticoCard";

function Tabs({ usuario }) {
  const [activeTab, setActiveTab] = useState("opcion1");
  const [diagnosticos, setDiagnosticos] = useState<any[]>([]);
  const [idPaciente, setIdPaciente] = useState("");
  const [diagnosticoTexto, setDiagnosticoTexto] = useState("");
  const [fechaActual, setFechaActual] = useState("");
  const tipoUsuario = usuario.tipo;

  useEffect(() => {
    const hoy = new Date();
    const fecha = hoy.toISOString().split("T")[0];
    setFechaActual(fecha);
  }, []);

  useEffect(() => {
    const fetchDiagnosticos = async () => {
      try {
        const response = await fetch("http://localhost:5000/diagnosticos", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ id_usuario: usuario.id_usuario }),
        });

        const data = await response.json();
        if (Array.isArray(data)) {
          setDiagnosticos(data);
        } else {
          console.error("Formato de datos incorrecto:", data);
        }
      } catch (error) {
        console.error("Error al obtener diagnósticos:", error);
      }
    };

    fetchDiagnosticos();
  }, [usuario.id_usuario]);

  const handleGuardarDiagnostico = async () => {
    if (!idPaciente || !diagnosticoTexto) {
      alert("Por favor completa todos los campos.");
      return;
    }

    const nuevoDiagnostico = {
      id_usuario: usuario.id_usuario,
      id_paciente: idPaciente,
      d_especialidad: usuario.especialidad,
      fecha: fechaActual,
      entrada: diagnosticoTexto,
    };

    try {
      const response = await fetch(
        "http://localhost:5000/diagnosticos/entrada",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(nuevoDiagnostico),
        }
      );

      const data = await response.json();
      if (response.ok) {
        alert("Diagnóstico guardado exitosamente.");
        setDiagnosticoTexto("");
        setIdPaciente("");

        // Agregar el nuevo diagnóstico al inicio del listado
        setDiagnosticos((prev: any[]) => [
          {
            ...nuevoDiagnostico,
            nombre_paciente: "Paciente", // Temporal
            nombre_medico: usuario.nombre,
          },
          ...prev,
        ]);
      } else {
        console.error("Error al guardar diagnóstico:", data.error);
        alert("Error al guardar diagnóstico.");
      }
    } catch (error) {
      console.error("Error en la solicitud:", error);
    }
  };

  return (
    <>
      <ul className="nav nav-tabs mb-3">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === "opcion1" ? "active" : ""}`}
            onClick={() => setActiveTab("opcion1")}
          >
            Ver Diagnósticos
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === "opcion2" ? "active" : ""}`}
            onClick={() => setActiveTab("opcion2")}
          >
            {tipoUsuario === "m" ? "Nueva Consulta" : "Consulta Médica"}
          </button>
        </li>
      </ul>

      <div>
        {activeTab === "opcion1" &&
          diagnosticos.map((diag, index) => (
            <Diagnostico
              key={index}
              diagnostico={diag}
              tipoUsuario={tipoUsuario}
              usuarioActual={usuario.id_usuario}
            />
          ))}

        {activeTab === "opcion2" && tipoUsuario === "m" && (
          <div className="card p-4 shadow">
            <h5 className="mb-3">Registrar Nueva Consulta</h5>

            <div className="mb-3">
              <label htmlFor="idPaciente" className="form-label">
                ID del paciente
              </label>
              <input
                type="text"
                className="form-control"
                id="idPaciente"
                value={idPaciente}
                onChange={(e) => setIdPaciente(e.target.value)}
                placeholder="Ingresa el ID del paciente"
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Nombre del Médico</label>
              <input
                type="text"
                className="form-control"
                value={usuario.nombre}
                disabled
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Especialidad</label>
              <input
                type="text"
                className="form-control"
                value={usuario.especialidad}
                disabled
              />
            </div>

            <div className="mb-3">
              <label className="form-label">Fecha</label>
              <input
                type="date"
                className="form-control"
                value={fechaActual}
                disabled
              />
            </div>

            <div className="mb-3">
              <label htmlFor="diagnosticoTexto" className="form-label">
                Diagnóstico
              </label>
              <textarea
                className="form-control"
                id="diagnosticoTexto"
                rows={5}
                value={diagnosticoTexto}
                onChange={(e) => setDiagnosticoTexto(e.target.value)}
                placeholder="Escribe el diagnóstico aquí..."
              ></textarea>
            </div>

            <button
              className="btn btn-primary"
              onClick={handleGuardarDiagnostico}
            >
              Guardar Diagnóstico
            </button>
          </div>
        )}

        {activeTab === "opcion2" && tipoUsuario === "p" && (
          <div className="alert alert-info">
            Como paciente, puedes consultar tus diagnósticos en la pestaña
            anterior.
          </div>
        )}
      </div>
    </>
  );
}

export default Tabs;
