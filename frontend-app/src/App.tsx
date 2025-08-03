import React, { useState } from "react";
import Acceso from "./Acceso";
import Perfil, { PerfilBody } from "./components/Perfil";
import Tabs from "./components/Tabs";

function App() {
  const [usuario, setUsuario] = useState(null);

  const cerrarSesion = () => {
    setUsuario(null);
  };

  const handleLogin = (data) => {
    setUsuario(data.usuario);
    console.log("Usuario autenticado:", data.usuario);
  };

  if (!usuario) {
    return <Acceso onLogin={handleLogin} />;
  }

  return (
    <div
      className="container d-flex justify-content-center align-items-center"
      style={{ height: "100vh" }}
    >
      <div className="row w-100" style={{ maxWidth: "1200px" }}>
        <div className="col-md-8 border-end pe-4">
          <Tabs usuario={usuario} />
        </div>
        <div className="col-md-4">
          <Perfil onCerrarSesion={cerrarSesion}>
            <PerfilBody usuario={usuario} />
          </Perfil>
        </div>
      </div>
    </div>
  );
}

export default App;
