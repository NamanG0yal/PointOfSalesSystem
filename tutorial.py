from flask import Flask
naman = Flask(__name__)

@naman.route("/naman")
def hello_world():
    return "Naman"

if __name__ == "__main__":
    naman.run(debug=True)
