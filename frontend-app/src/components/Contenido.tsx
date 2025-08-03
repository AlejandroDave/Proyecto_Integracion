import { ReactNode } from "react";

interface CuerpoContenido {
  children: ReactNode;
}

function CajaContenido({ children }: CuerpoContenido) {
  return (
    <>
      <div className="card" style={{ width: "750px", background: "white" }}>
        <div className="card-body">{children}</div>
      </div>
    </>
  );
}

export default CajaContenido;

interface contenido {
  id_usuario?: string;
  id_paciente: string;
  d_especialidad?: string;
  texto: string;
  fecha: string;
  tipoContenido: string;
}

export function Cuerpo(props: contenido) {
  const {
    id_usuario,
    id_paciente,
    d_especialidad,
    texto,
    fecha,
    tipoContenido,
  } = props;

  return (
    <>
      {tipoContenido == "d" && (
        <>
          {" "}
          <h5 className="card-title">Consulta de {d_especialidad}</h5>
          <h6 className="card-subtitle mb-2 text-body-secondary">
            Fecha de consulta {fecha}
          </h6>
          <h6 className="card-subtitle mb-2 text-body-secondary">
            Realizada por {id_usuario}
          </h6>
          <p className="card-text">{texto}</p>
        </>
      )}
      {tipoContenido == "r" && (
        <>
          {" "}
          <h5 className="card-title">Resumen realizado en {fecha}</h5>
          <p className="card-text">{texto}</p>
        </>
      )}
    </>
  );
}
