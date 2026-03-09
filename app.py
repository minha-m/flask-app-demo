from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Music Mood Recommender</title>
        <style>

            body{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#667eea,#764ba2);
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                margin:0;
            }

            .card{
                background:white;
                padding:40px;
                border-radius:15px;
                box-shadow:0px 8px 20px rgba(0,0,0,0.2);
                text-align:center;
                width:350px;
            }

            h2{
                margin-bottom:20px;
                color:#333;
            }

            input,select{
                width:100%;
                padding:10px;
                margin:10px 0;
                border-radius:8px;
                border:1px solid #ccc;
            }

            button{
                background:#667eea;
                color:white;
                border:none;
                padding:12px;
                width:100%;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;
            }

            button:hover{
                background:#5a67d8;
            }

        </style>
    </head>

    <body>

        <div class="card">
            <h2>🎧 Music Mood Recommender</h2>

            <form action="/result" method="post">

                <input type="text" name="name" placeholder="Enter your name" required>

                <select name="mood">
                    <option value="">Select your mood</option>
                    <option value="happy">😊 Happy</option>
                    <option value="sad">😢 Sad</option>
                    <option value="relaxed">😌 Relaxed</option>
                    <option value="energetic">⚡ Energetic</option>
                </select>

                <button type="submit">Get Songs 🎵</button>

            </form>
        </div>

    </body>
    </html>
    """


@app.route("/result", methods=["POST"])
def result():

    name = request.form["name"]
    mood = request.form["mood"]

    if mood == "happy":
        songs = "Happy - Pharrell Williams<br>Can't Stop the Feeling - Justin Timberlake"

    elif mood == "sad":
        songs = "Someone Like You - Adele<br>Fix You - Coldplay"

    elif mood == "relaxed":
        songs = "Let Her Go - Passenger<br>Weightless - Marconi Union"

    elif mood == "energetic":
        songs = "Eye of the Tiger - Survivor<br>Thunder - Imagine Dragons"

    else:
        songs = "Shape of You - Ed Sheeran"

    return f"""
    <html>
    <head>
    <style>

        body{{
            font-family:Arial;
            background:linear-gradient(135deg,#764ba2,#667eea);
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
        }}

        .card{{
            background:white;
            padding:40px;
            border-radius:15px;
            text-align:center;
            box-shadow:0px 8px 20px rgba(0,0,0,0.2);
            width:400px;
        }}

        a{{
            text-decoration:none;
            color:white;
            background:#667eea;
            padding:10px 20px;
            border-radius:8px;
        }}

    </style>
    </head>

    <body>

        <div class="card">

        <h2>🎶 Music Recommendation</h2>

        <p><b>Name:</b> {name}</p>
        <p><b>Mood:</b> {mood}</p>

        <p><b>Recommended Songs:</b></p>

        <p>{songs}</p>

        <br>
        <a href="/">Try Again</a>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
