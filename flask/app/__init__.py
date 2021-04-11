import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

#this connects to the test database I built in a standalone docker container called "mysql_test"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/daviddb'

#this connect the db to the db I'm building with docker compose
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/daviddb'

db = SQLAlchemy(app)

class CityRecord(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

def get_all_cities():
    return CityRecord.query.all()

@app.route('/', methods=["GET"])
def index():
    cities = get_all_cities();
    result = ""
    for city in cities:
        result += f"<p>{city.name} is the #{city.id} city!</p>"
    return result