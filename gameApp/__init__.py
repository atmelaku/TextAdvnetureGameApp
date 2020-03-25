from flask import Flask, render_template, request, url_for, redirect
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, "gameApp.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

        
    @app.route('/hello')
    def hello_world():
        return 'Hello, World!'
    from . import math
    app.register_blueprint(math.bp)
    app.add_url_rule('/', endpoint='index')




    return app
