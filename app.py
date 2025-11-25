from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Load Model sekali saja saat aplikasi start
model = load_model('waste_classifier_model.h5')

def prepare_image(image, target_size):
    # Ubah ke RGB (jaga-jaga jika PNG transparan)
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize sesuai input model kamu
    image = image.resize(target_size)
    image = img_to_array(image)
    
    # Normalisasi (0-1) karena training pakai rescale=1./255
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Tidak ada file diunggah"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Nama file kosong"}), 400

    try:
        # Proses Gambar
        image = Image.open(io.BytesIO(file.read()))
        processed_image = prepare_image(image, target_size=(224, 224))
        
        # Prediksi
        prediction = model.predict(processed_image)
        result_index = np.argmax(prediction, axis=1)[0]
        confidence = float(np.max(prediction))

        if result_index == 0:
            label = "Organic"
            tips = [
                "Cocok untuk dijadikan pupuk kompos.",
                "Bisa untuk pakan Maggot (BSF).",
                "Buat lubang biopori untuk pembuangan."
            ]
        else:
            label = "Recyclable"
            tips = [
                "Dapat dijual di Bank Sampah.",
                "Bersihkan dari sisa makanan sebelum dibuang.",
                "Bisa diubah menjadi kerajinan (Ecobrick)."
            ]

        return jsonify({
            "label": label,
            "confidence": f"{confidence*100:.2f}%",
            "tips": tips
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)