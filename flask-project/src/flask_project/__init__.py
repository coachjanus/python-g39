from flask import Flask
from flask_project import pages

# app = Flask(__name__)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(pages.bp)
    # @app.route('/')
    # def index():
    #     return "Hello Flask Factory"


    # @app.route('/about')
    # def about():
    #     return "About Page"
    
    # @app.route('/contact')
    # def contact():
    #     return "Contact Us"
    
    return app

def main() -> None:
    # print("Hello from flask-project!")
    create_app().run(debug=True)
