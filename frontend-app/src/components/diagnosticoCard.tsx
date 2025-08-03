// components/DiagnosticoCard.tsx
import React from "react";

function DiagnosticoCard({ diagnostico, tipoUsuario }) {
  const esMedico = tipoUsuario === "m";

  const nombrePersona = esMedico
    ? `Paciente: ${diagnostico.nombre_paciente || diagnostico.id_paciente}`
    : `Médico: ${diagnostico.nombre_medico || diagnostico.id_usuario}`;

  return (
    <div className="card mb-3 shadow-sm">
      <div className="card-header bg-primary text-white">
        Especialidad: {diagnostico.d_especialidad}
      </div>
      <div className="card-body">
        <h6 className="card-subtitle mb-2 text-muted">
          {nombrePersona} — {new Date(diagnostico.fecha).toLocaleDateString()}
        </h6>
        <p className="card-text" style={{ fontSize: "0.9rem" }}>
          {diagnostico.diagnostico}
        </p>
      </div>
    </div>
  );
}

export default DiagnosticoCard;
