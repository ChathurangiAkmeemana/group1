from app import app

@app.route('/')
def home():
    return "🚀 Hello from the Flask Team App!"
