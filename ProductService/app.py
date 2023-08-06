from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/ekart'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from product.views import product_blueprint
app.register_blueprint(product_blueprint)
@app.route('/')
def ok():
    return "Ok"


if __name__ == '__main__':
    app.run()

