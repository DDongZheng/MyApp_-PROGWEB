from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:mypassword@localhost/myappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)

@app.route('/get-number', methods=['GET'])
def get_number():
    number = Number.query.order_by(db.func.random()).first()
    return jsonify(number=number.value)

@app.route('/init-db')
def init_db():
    db.create_all()
    for i in range(1, 101):
        num = Number(value=i)
        db.session.add(num)
    db.session.commit()
    return 'Database initialized'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
