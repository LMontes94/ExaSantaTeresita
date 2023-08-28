from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://l.montes94:ignacio94@exaTorneo/5432'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('/sitio/home.html')


@app.route('/rules')
def about():
    return render_template('/sitio/rules.html')

@app.route('/info')
def info():
    return render_template('/sitio/info.html')

if __name__ == '__main__':
    app.run(debug=True)
