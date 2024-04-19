
from flask import Flask
from app.common.encoders import AlchemyEncoder

from app import settings
from app import logs
from app import exception_handlers
from app import blueprints
from flask_cors import CORS


cors = CORS(resources={r"/api/*": {"origins": "*"}})


def create_app():
    """
    pass
    :return:
    """
    app = Flask('weather')
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    # app.config['FLASK_ADMIN_SWATCH'] = settings.FLASK_ADMIN_SWATCH
    # app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
    # app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC+8'
    app.json_encoder = AlchemyEncoder
    app.datetime_format = settings.DATETIME_FORMAT
    app.date_format = settings.DATE_FORMAT

    # 安装插件
    exception_handlers.init_app(app)
    logs.init_app(app)
    cors.init_app(app)
    blueprints.init_app(app)

    return app

application = create_app()


if __name__ == '__main__':
    for url in application.url_map.iter_rules():
        print('{}:{}'.format(url.host, url.rule))
    application.run(debug=True)

