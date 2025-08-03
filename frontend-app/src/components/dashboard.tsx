// components/Dashboard.tsx
import Perfil, { PerfilBody } from "./Perfil";
import React from "react";
import Tabs from "./Tabs"; // Componente que crearemos para las pestañas

const dashboardStyle: React.CSSProperties = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
  backgroundColor: "#e6e9eaff",
};

const contentContainer: React.CSSProperties = {
  display: "flex",
  flexDirection: "row",
  width: "80%",
  maxWidth: "1200px",
  backgroundColor: "#fff",
  borderRadius: "10px",
  boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
  overflow: "hidden",
};

const leftPanel: React.CSSProperties = {
  flex: 1,
  padding: "20px",
};

const rightPanel: React.CSSProperties = {
  width: "350px",
  borderLeft: "1px solid #ddd",
  padding: "20px",
};

function Dashboard({ usuario, onCerrarSesion }) {
  return (
    <div className="dashboard-container">
      <div className="main-content">
        <Tabs usuario={usuario} />
      </div>
      <Perfil onCerrarSesion={onCerrarSesion}>
        <PerfilBody usuario={usuario} />
      </Perfil>
    </div>
  );
}

export default Dashboard;
