from flask import Flask
app = Flask(__name__)

@app.route('/mem')
def mem():
    return {"mem": ["memb1","mem2"]}


if __name__ == "__main__":
    app.run(debug=True)