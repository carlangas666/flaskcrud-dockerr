from app.app import app
from app.contacts import contacts

app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)