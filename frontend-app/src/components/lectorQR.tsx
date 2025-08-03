import jsQR from "jsqr";

function LectorQR(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = function (e) {
      const img = new Image();
      img.onload = function () {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0, img.width, img.height);

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

    reader.onerror = function () {
      reject("Error al leer la imagen.");
    };

    reader.readAsDataURL(file);
  });
}

export default LectorQR;
