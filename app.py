from flask import Flask, request, render_template_string
import main  # Assuming you refactor your main.py code to be callable from here

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to The Last Light RPG!</h1>")

# Add more routes to interact with your game

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
