from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket

app = Flask(__name__)

# Allow the Next.js frontend (different port = different origin) to call this API.
# For local dev this is wide open; in production, restrict to the real frontend URL(s).
CORS(app)


@app.route("/")
def home():
    return jsonify(
        {
            "app": "flask-basic-app",
            "role": "backend",
            "message": "Hello from the GRAAHO Argo CD on EKS demo backend!",
            "hostname": socket.gethostname(),
        }
    )


@app.route("/healthz")
def healthz():
    # Lightweight endpoint for k8s readiness/liveness probes
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5007))
    app.run(host="0.0.0.0", port=port)
