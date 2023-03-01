from flask import Flask
from flask_cors import CORS
from models import db, migrate

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def hello_world():
        return 'weeeeeeew'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)