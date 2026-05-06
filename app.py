from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """

    <html>

    <head>

        <title>PaaS Web App</title>

        <style>

            body {
                margin: 0;
                font-family: Arial;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                text-align: center;
            }

            .container {
                margin-top: 100px;
            }

            h1 {
                font-size: 50px;
            }

            .card {
                background: rgba(255,255,255,0.2);
                padding: 20px;
                margin: 20px auto;
                width: 50%;
                border-radius: 10px;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>🚀 My Cloud Web App</h1>

            <p>Deployed using PaaS (Render)</p>

            <div class="card">
                <h2>Project Info</h2>
                <p>This app is created using Flask and deployed on cloud.</p>
            </div>

            <div class="card">
                <h2>Features</h2>
                <p>✔ Easy Deployment</p>
                <p>✔ Cloud Hosting</p>
                <p>✔ Scalable Platform</p>
            </div>

            <div class="card">
                <h2>Developed By</h2>
                <p>Your Name</p>
            </div>

        </div>

    </body>

    </html>

    """

if __name__ == "__main__":
    app.run(debug=True)
