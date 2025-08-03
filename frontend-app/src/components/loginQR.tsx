import React, { useState } from "react";
import jsQR from "jsqr";

function LoginQR({ onLogin }) {
  const [archivoQR, setArchivoQR] = useState(null);
  const [error, setError] = useState("");

  const leerQR = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
          const canvas = document.createElement("canvas");
          const ctx = canvas.getContext("2d");

          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0);

          const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const qrCode = jsQR(imageData.data, canvas.width, canvas.height);

          if (qrCode) {
            resolve(qrCode.data);
          } else {
            reject("No se detectó un código QR.");
          }
        };
        img.src = e.target.result;
      };

      reader.onerror = () => {
        reject("Error al leer la imagen.");
      };

      reader.readAsDataURL(file);
    });
  };

  const handleSubmit = async () => {
    setError("");

    if (!archivoQR) {
      setError("Por favor, selecciona una imagen con código QR.");
      return;
    }

    try {
      const contenidoQR = await leerQR(archivoQR);

      const response = await fetch("http://127.0.0.1:5000/login/QR", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ qr_acceso: contenidoQR }),
      });

      const data = await response.json();

      if (response.ok) {
        onLogin(data); // se pasa al dashboard
      } else {
        setError(data.error || "Código QR no válido.");
      }
    } catch (err) {
      console.error("Error al procesar el QR:", err);
      setError("No se pudo leer el código QR.");
    }
  };

  return (
    <div>
      <h2>Acceder con QR</h2>

      {error && <div className="alert alert-danger">{error}</div>}

      <div className="mb-3">
        <label htmlFor="qrInput" className="form-label">
          Subir imagen QR:
        </label>
        <input
          type="file"
          className="form-control"
          id="qrInput"
          accept="image/*"
          onChange={(e) => setArchivoQR(e.target.files[0])}
        />
      </div>

      <button className="btn btn-success" onClick={handleSubmit}>
        Iniciar sesión
      </button>
    </div>
  );
}

export default LoginQR;
