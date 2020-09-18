from bottle import Bottle, run

app = Bottle()

@app.get("/")
def hello():
    return "<h1>hello world</h1>"

run(app)