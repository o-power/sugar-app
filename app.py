import os
from flask import Flask

app = Flask(__name__,
            template_folder="templates")

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    #app.run(host=os.environ.get('IP'),
    #        port=int(os.environ.get('PORT')),
    #        debug=False)
    app.run(debug=True)