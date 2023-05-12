from flask import Flask, session, g
import config
from exts import db, mail
from blueprints import user_bp, qa_bp
from flask_migrate import Migrate   # 迁移
from models import UserModel
from threading import Lock



app = Flask(__name__)
app.config.from_object(config)   # 配置文件
db.init_app(app)    # 绑定数据库
mail.init_app(app)      # 注册邮箱发送


# 注册到app当中
migrate = Migrate(app, db)


# 将页面注册到app中
app.register_blueprint(user_bp)
app.register_blueprint(qa_bp)


@app.before_request
# 钩子函数
def before_request():
    ''' 在请求之前执行 '''
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个名为user的变量，传入值为user
            g.user = user
        except:
            g.user = None

# 请求 -> before_request -> 视图函数 -> 视图函数返回html模板 -> context_processor

@app.context_processor
# 上下文处理器
def context_processor():
    ''' 每个渲染的模板都得先执行此函数 '''
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        # 用户未登入
        return {}


if __name__ == '__main__':
    # 使用socketio启动项目
    app.run()
