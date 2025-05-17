from flask import render_template, Flask

render_template

app = Flask(__name__, static_folder='css')

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)
