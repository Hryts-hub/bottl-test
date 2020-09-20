from bottle import Bottle

app = Bottle()

@app.get("/")
def hello():
    return "<h1>hello world</h1>"

app.get("/movies/")
def movies():
    return "a lot of movies"

run(app)