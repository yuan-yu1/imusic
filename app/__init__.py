from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__,
                static_folder='../static',   # 指向项目根目录的 static
                static_url_path='/static')
    app.config.from_object(Config)
    CORS(app)

    # 初始化扩展
    db.init_app(app)

    # 注册蓝图
    from app.routes import bp
    app.register_blueprint(bp)

    return app
