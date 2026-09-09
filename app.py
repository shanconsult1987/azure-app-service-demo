from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure App Service Demo</title>
        </head>
        <body>
            <h1>Azure App Service Demo</h1>
            <p>Application is running successfully.</p>
            <p>Deployed using GitHub Actions.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "azure-app-service-demo"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
