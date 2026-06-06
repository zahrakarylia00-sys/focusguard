"""
app.py — FocusGuard Flask Server (Hosting Version)
Deteksi dilakukan di browser (MediaPipe WASM)
Server hanya menyimpan sesi & generate QR
"""

from flask import Flask, render_template, request, jsonify
import uuid, qrcode, io, base64
from datetime import datetime

app      = Flask(__name__)
sessions = {}

# ── Ganti ini dengan domain hosting kamu nanti ──────────────
BASE_URL = "https://web-production-ca39.up.railway.app"   # ← ubah saat deploy ke: "https://namadomain.up.railway.app"


def make_qr(url: str) -> str:
    qr = qrcode.QRCode(version=1, box_size=8, border=3,
                       error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color="#0f172a", back_color="white")
    buf = io.BytesIO(); img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


@app.route("/")
def index():
    return render_template("index.html",
                           qr_data=make_qr(BASE_URL),
                           app_url=BASE_URL)

@app.route("/detect")
def detect_page():
    return render_template("detect.html")

@app.route("/result/<sid>")
def result(sid):
    data = sessions.get(sid)
    url  = f"{BASE_URL}/result/{sid}"
    return render_template("result.html",
                           session=data, session_id=sid,
                           qr_data=make_qr(url), result_url=url)

@app.route("/api/save_session", methods=["POST"])
def save_session():
    data              = request.get_json()
    sid               = str(uuid.uuid4())[:8]
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sessions[sid]     = data
    url               = f"{BASE_URL}/result/{sid}"
    return jsonify({"session_id": sid, "url": url, "qr": make_qr(url)})


if __name__ == "__main__":
    print("="*50)
    print("  FOCUSGUARD — Buka: http://localhost:5000")
    print("="*50)
    app.run(host="0.0.0.0", port=5000, debug=False)
