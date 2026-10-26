
from flask import Flask, request, render_template_string

app = Flask(__name__)

inbuilt_user_name = "admin"
inbuilt_user_password = "admin123"

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus | Login</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            background:
                radial-gradient(circle at top left, #253b75, transparent 45%),
                radial-gradient(circle at bottom right, #52265f, transparent 45%),
                #080c19;
            color: white;
        }

        .container {
            display: flex;
            width: 100%;
            max-width: 900px;
            min-height: 520px;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 22px;
            overflow: hidden;
            background: rgba(255,255,255,0.04);
            box-shadow: 0 25px 70px rgba(0,0,0,0.5);
            backdrop-filter: blur(20px);
        }

        .welcome {
            flex: 1;
            padding: 45px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            background: linear-gradient(
                145deg,
                rgba(55,80,160,0.65),
                rgba(90,40,125,0.35)
            );
        }

        .logo {
            font-size: 21px;
            font-weight: bold;
            letter-spacing: 4px;
            color: #bdcaff;
            margin-bottom: 65px;
        }

        .welcome h1 {
            font-size: 40px;
            line-height: 1.25;
            margin-bottom: 20px;
        }

        .welcome h1 span {
            color: #a5b7ff;
        }

        .welcome p {
            color: #d0d7ed;
            font-size: 14px;
            line-height: 1.8;
        }

        .line {
            width: 55px;
            height: 4px;
            background: #9eafff;
            border-radius: 10px;
            margin-top: 30px;
        }

        .login {
            flex: 1;
            padding: 45px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .login h2 {
            font-size: 31px;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #9ca8c5;
            font-size: 14px;
            margin-bottom: 32px;
        }

        .input-group {
            margin-bottom: 22px;
        }

        .input-group label {
            display: block;
            font-size: 14px;
            margin-bottom: 10px;
            color: #dce3f7;
        }

        .input-group input[type="text"],
        .input-group input[type="password"] {
            width: 100%;
            padding: 14px;
            border-radius: 9px;
            border: 1px solid #343d58;
            outline: none;
            background: rgba(8,13,29,0.8);
            color: white;
            font-size: 14px;
            transition: 0.3s;
        }

        .input-group input:focus {
            border-color: #93a8ff;
            box-shadow: 0 0 12px rgba(120,145,255,0.2);
        }

        input::placeholder {
            color: #69738f;
        }

        .show-password {
            display: flex !important;
            align-items: center;
            gap: 8px;
            margin-top: 12px;
            color: #aab4cf !important;
            cursor: pointer;
        }

        .show-password input {
            accent-color: #879fff;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 5px;
            border: none;
            border-radius: 9px;
            background: linear-gradient(100deg, #526fe3, #9360d9);
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(82,111,227,0.35);
        }

        .message {
            padding: 12px;
            margin-top: 20px;
            border-radius: 8px;
            text-align: center;
            font-size: 13px;
        }

        .success {
            color: #83f5bc;
            background: rgba(32,180,112,0.12);
            border: 1px solid rgba(32,180,112,0.3);
        }

        .error {
            color: #ff9baf;
            background: rgba(255,70,100,0.1);
            border: 1px solid rgba(255,70,100,0.3);
        }

        .footer {
            margin-top: 28px;
            text-align: center;
            font-size: 12px;
            color: #737f9e;
        }

        @media (max-width: 700px) {
            .container {
                flex-direction: column;
                max-width: 430px;
            }

            .welcome, .login {
                padding: 30px;
            }

            .logo {
                margin-bottom: 25px;
            }

            .welcome h1 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <div class="welcome">
            <div class="logo">NEXUS.</div>

            <h1>Welcome to<br><span>Your Space.</span></h1>

            <p>
                A secure place to begin your journey.
                Sign in to continue and enjoy a simple,
                seamless login experience.
            </p>

            <div class="line"></div>
        </div>

        <div class="login">
            <h2>Sign in</h2>

            <p class="subtitle">
                Welcome back! Please enter your details.
            </p>

            <form method="POST">

                <div class="input-group">
                    <label for="username">Username</label>

                    <input
                        type="text"
                        id="username"
                        name="username"
                        placeholder="Enter your username"
                        autocomplete="username"
                        required
                    >
                </div>

                <div class="input-group">
                    <label for="password">Password</label>

                    <input
                        type="password"
                        id="password"
                        name="password"
                        placeholder="Enter your password"
                        autocomplete="current-password"
                        required
                    >

                    <label class="show-password">
                        <input
                            type="checkbox"
                            onchange="togglePassword()"
                        >
                        Show password
                    </label>
                </div>

                <button type="submit">Login →</button>

            </form>

            {% if message %}
                <div class="message {{ status }}">
                    {{ message }}
                </div>
            {% endif %}

            <div class="footer">
                © 2026 NEXUS. Secure access portal.
            </div>
        </div>

    </div>

    <script>
        function togglePassword() {
            const password = document.getElementById("password");

            password.type =
                password.type === "password" ? "text" : "password";
        }
    </script>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    status = ""

    if request.method == "POST":

        user_name = request.form.get("username", "")
        user_password = request.form.get("password", "")

        if (
            user_name == inbuilt_user_name
            and user_password == inbuilt_user_password
        ):
            message = "Login successful! Welcome, admin."
            status = "success"
        else:
            message = "Invalid username or password. Please try again."
            status = "error"

    return render_template_string(
        html,
        message=message,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)
