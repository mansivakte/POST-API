from app import app

@app.route('/')
def index():
    return "Post application is loading...."