// Acceso.tsx
import React, { useState } from "react";
import LoginForm from "./components/loginForm";
import LoginQR from "./components/loginQR";

const accesoContainerStyle: React.CSSProperties = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
  backgroundColor: "#e6e9eaff",
};

const accesoBoxStyle: React.CSSProperties = {
  backgroundColor: "#ffffffff",
  padding: "30px",
  borderRadius: "10px",
  boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
  width: "100%",
  maxWidth: "500px",
};

function Acceso({ onLogin }) {
  const [modoQR, setModoQR] = useState(false);

  return (
    <div style={accesoContainerStyle}>
      <div style={accesoBoxStyle}>
        <div className="mb-4 text-center">
          <button
            className={`btn me-3 ${
              !modoQR ? "btn-primary" : "btn-outline-primary"
            }`}
            onClick={() => setModoQR(false)}
          >
            Acceso con Usuario y Contraseña
          </button>
          <button
            className={`btn ${modoQR ? "btn-success" : "btn-outline-success"}`}
            onClick={() => setModoQR(true)}
          >
            Acceso con QR
          </button>
        </div>

        {modoQR ? (
          <LoginQR onLogin={onLogin} />
        ) : (
          <LoginForm onLogin={onLogin} />
        )}
      </div>
    </div>
  );
}

export default Acceso;
