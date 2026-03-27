from flask import Flask

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)