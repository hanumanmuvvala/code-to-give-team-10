from flask import Flask
from web.dao.BaseDAO import BaseDAO
from web.dao.DbUtil import DbUtil
baseDAO = None
log = None
db_util = None

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('config')
    
    global log
    log = app.logger
    # Initialize DbUtil
    global db_util
    db_util = DbUtil(app)
    # log.info("Initialized DB UTIL in createapp!")
    # log.info(app.config)
    
    global baseDAO
    baseDAO = BaseDAO(db_util)
    log.info("Initialized Base DAO!")

    from web.routes.user import user_view
    app.register_blueprint(user_view, url_prefix='/')

    from web.routes.wish import wish_view
    app.register_blueprint(wish_view, url_prefix='/wishes')

    from web.routes.messages import message_view
    app.register_blueprint(message_view, url_prefix='/')

    with app.app_context():
        log.info("app.app_context()")

    return app
