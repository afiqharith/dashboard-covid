from flask import Flask

class Dashboard:
    def __init__(self) -> None:
        self.start_server = self.init()

    def init(self) -> Flask:
        app = Flask(__name__)
        app.config["SECRET_KEY"] = "MYDASHBOARD123"

        from .views import views
        app.register_blueprint(views, url_prefix="/")

        return app