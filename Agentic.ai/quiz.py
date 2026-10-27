from flask import Flask, request, render_template_string

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "What is the capital of Telangana?",
        "answer": "hyderabad"
    },
    {
        "question": "What is the capital of Karnataka?",
        "answer": "bengaluru"
    },
    {
        "question": "What is the capital of Tamil Nadu?",
        "answer": "chennai"
    },
    {
        "question": "What is the capital of Kerala?",
        "answer": "thiruvananthapuram"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    number = request.args.get("q", 0, type=int)
    number = max(0, min(number, len(questions) - 1))

    result = ""
    user_answer = ""

    if request.method == "POST":
        number = request.form.get("number", 0, type=int)
        number = max(0, min(number, len(questions) - 1))

        user_answer = request.form.get("answer", "").strip()

        if user_answer.lower() == questions[number]["answer"]:
            result = "Correct Answer! 🎉"
        else:
            result = (
                "Wrong Answer! The correct answer is "
                + questions[number]["answer"].title()
            )

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quiz Master</title>

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #141e30, #243b55);
                padding: 20px;
            }

            .quiz-container {
                width: 100%;
                max-width: 480px;
                background: white;
                padding: 35px;
                border-radius: 20px;
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
            }

            .logo {
                font-size: 42px;
                text-align: center;
            }

            h1 {
                text-align: center;
                color: #243b55;
                margin-bottom: 8px;
            }

            .subtitle {
                text-align: center;
                color: #777;
                margin-bottom: 30px;
            }

            .progress {
                color: #555;
                font-size: 14px;
                margin-bottom: 12px;
            }

            .progress-bar {
                height: 8px;
                background: #e5e7eb;
                border-radius: 10px;
                overflow: hidden;
                margin-bottom: 25px;
            }

            .progress-fill {
                height: 100%;
                background: #6c63ff;
                border-radius: 10px;
            }

            .question {
                font-size: 22px;
                font-weight: bold;
                color: #222;
                line-height: 1.5;
                margin-bottom: 22px;
            }

            input[type="text"] {
                width: 100%;
                padding: 15px;
                border: 2px solid #ddd;
                border-radius: 10px;
                font-size: 16px;
                outline: none;
                margin-bottom: 18px;
            }

            input[type="text"]:focus {
                border-color: #6c63ff;
            }

            button, .next-button {
                display: block;
                width: 100%;
                padding: 14px;
                border: none;
                border-radius: 10px;
                background: #6c63ff;
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
            }

            button:hover, .next-button:hover {
                background: #5148e5;
            }

            .result {
                margin-top: 20px;
                padding: 14px;
                border-radius: 10px;
                background: #f0f4ff;
                color: #243b55;
                text-align: center;
                font-weight: bold;
                overflow-wrap: anywhere;
            }

            .footer {
                text-align: center;
                color: #888;
                font-size: 12px;
                margin-top: 25px;
            }
        </style>
    </head>

    <body>
        <div class="quiz-container">

            <div class="logo">🧠</div>

            <h1>Quiz Master</h1>

            <p class="subtitle">
                Test your knowledge, one question at a time!
            </p>

            <div class="progress">
                Question {{ number + 1 }} of {{ total }}
            </div>

            <div class="progress-bar">
                <div class="progress-fill"
                     style="width: {{ ((number + 1) / total) * 100 }}%;">
                </div>
            </div>

            <div class="question">
                {{ question }}
            </div>

            <form method="POST">
                <input type="hidden"
                       name="number"
                       value="{{ number }}">

                <input type="text"
                       name="answer"
                       placeholder="Type your answer here..."
                       value="{{ user_answer }}"
                       required
                       autocomplete="off">

                <button type="submit">Check Answer</button>
            </form>

            {% if result %}
                <div class="result">
                    {{ result }}
                </div>

                {% if number + 1 < total %}
                    <a class="next-button"
                       style="margin-top: 15px;"
                       href="/?q={{ number + 1 }}">
                        Next Question →
                    </a>
                {% else %}
                    <a class="next-button"
                       style="margin-top: 15px;"
                       href="/">
                        Restart Quiz ↻
                    </a>
                {% endif %}
            {% endif %}

            <div class="footer">
                Made with Python + Flask ❤️
            </div>

        </div>
    </body>
    </html>
    """,
    number=number,
    total=len(questions),
    question=questions[number]["question"],
    result=result,
    user_answer=user_answer
    )

if __name__ == "__main__":
    app.run(debug=True)
