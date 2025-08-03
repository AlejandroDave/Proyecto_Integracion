import { ReactNode } from "react";
import List from "./List";

interface datosPerfil {
  children: ReactNode;
  onCerrarSesion: () => void;
}

function Perfil({ children, onCerrarSesion }: datosPerfil) {
  // Se puede pasar el atributo children de manera directa en lso parametros

  return (
    <>
      <div className="card" style={{ width: "350px" }}>
        <img src="/user-icon.jpg" className="card-img-top" alt="user.jpg" />
        <div className="card-body">{children}</div>
        <div className="card-body">
          <button
            onClick={onCerrarSesion}
            type="button"
            className="btn btn-primary"
          >
            Cerrar Sesion
          </button>
        </div>
      </div>
    </>
  );
}
export default Perfil;

interface usuario {
  id_usuario: string;
  password: string;
  nombre: string;
  fecha_nacimiento: string;
  tipo_u: string;
  tipo_sangre?: string;
  d_especialidad?: string;
  QR_acceso?: string;
  correo_electronico: string;
  telefono: string;
  pad_cronico: string;
  donador_organos: string;
  accede_transfucion: string;
}

export function PerfilBody({ usuario }) {
  /*const { id_usuario,
            password,
            nombre,
            tipo_u,
            d_especialidad,
            correo_electronico,
            telefono,
            pad_cronico,
            donador_organos,
            accede_transfucion} = props;*/

  return (
    <>
      <h5 className="card-title">{usuario.nombre}</h5>

      <ul className="list-group list-group-flush">
        {usuario.tipo_u == "m" && (
          <>
            {" "}
            <p className="card-text">Usuario: Medico</p>
            <h5 className="card-title">
              Especialidad: {usuario.d_especialidad}
            </h5>
            <li className="list-group-item">
              Correo: {usuario.correo_electronico}
            </li>
            <li className="list-group-item">Telefono: {usuario.telefono}</li>
          </>
        )}
        {usuario.tipo_u == "p" && (
          <>
            <p className="card-text">Usuario: Paciente</p>
            <li className="list-group-item">
              Correo: {usuario.correo_electronico}
            </li>
            <li className="list-group-item">Telefono: {usuario.telefono}</li>
          </>
        )}
      </ul>
    </>
  );
}
