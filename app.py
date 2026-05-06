from flask import Flask

app = Flask(\__name_\_)

@app.route("/")

def home():

    return """

    &lt;html&gt;

    &lt;head&gt;

        &lt;title&gt;PaaS Web App&lt;/title&gt;

        &lt;style&gt;

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

        &lt;/style&gt;

    &lt;/head&gt;

    &lt;body&gt;

        &lt;div class="container"&gt;

            &lt;h1&gt;🚀 My Cloud Web App&lt;/h1&gt;

            &lt;p&gt;Deployed using PaaS (Render)&lt;/p&gt;

            &lt;div class="card"&gt;

                &lt;h2&gt;Project Info&lt;/h2&gt;

                &lt;p&gt;This app is created using Flask and deployed on cloud.&lt;/p&gt;

            &lt;/div&gt;

            &lt;div class="card"&gt;

                &lt;h2&gt;Features&lt;/h2&gt;

                &lt;p&gt;✔ Easy Deployment&lt;/p&gt;

                &lt;p&gt;✔ Cloud Hosting&lt;/p&gt;

                &lt;p&gt;✔ Scalable Platform&lt;/p&gt;

            &lt;/div&gt;

            &lt;div class="card"&gt;

                &lt;h2&gt;Developed By&lt;/h2&gt;

                &lt;p&gt;Your Name&lt;/p&gt;

            &lt;/div&gt;

        &lt;/div&gt;

    &lt;/body&gt;

    &lt;/html&gt;

    """

if **name** == "\__main_\_":

    [app.run](http://app.run)()