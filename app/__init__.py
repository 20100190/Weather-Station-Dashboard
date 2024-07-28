from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        static_folder='static',  # This points to the 'static' folder at the root level
        template_folder='templates'  # This points to the 'templates' folder at the root level
    )
    app.config.from_object('app.config.Config')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.other import bp as other_blueprint
    app.register_blueprint(other_blueprint, url_prefix='/other')

    # wroking for both bps but it's not gurranted either define gloabl error handlers or use no url_prefix
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html')

    return app
