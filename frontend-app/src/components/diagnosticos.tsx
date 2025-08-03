import React, { useEffect, useState } from "react";
import axios from "axios";

function Diagnosticos({ usuario }) {
  const [diagnosticos, setDiagnosticos] = useState([]);

  useEffect(() => {
    const fetchDiagnosticos = async () => {
      try {
        const response = await axios.post(
          "http://localhost:5000/diagnosticos",
          {
            id_usuario: usuario.id_usuario,
          }
        );
        setDiagnosticos(response.data);
      } catch (error) {
        console.error("Error al obtener diagnósticos:", error);
      }
    };

    fetchDiagnosticos();
  }, [usuario]);

  return (
    <div>
      {diagnosticos.length === 0 ? (
        <p>No hay diagnósticos registrados.</p>
      ) : (
        diagnosticos.map((diag, index) => (
          <div
            key={index}
            className="card mb-3 shadow-sm"
            style={{ fontSize: "0.95rem" }}
          >
            <div className="card-header bg-primary text-white fw-bold">
              {diag.especialidad}
            </div>
            <div className="card-body">
              <h6 className="card-subtitle mb-2 text-muted">
                {usuario.tipo_u === "m"
                  ? `Paciente: ${diag.id_paciente}`
                  : `Médico: ${diag.id_usuario}`}{" "}
                | {new Date(diag.fecha).toLocaleDateString()}
              </h6>
              <p className="card-text" style={{ fontSize: "0.85rem" }}>
                {diag.diagnostico}
              </p>
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default Diagnosticos;
