from flask import Flask, jsonify
from datetime import datetime
import os
from extensions import db, cors

# 初始化Flask应用
app = Flask(__name__)

# 配置
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化扩展
db.init_app(app)
cors.init_app(app)

# 导入路由
from routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# 测试路由
@app.route('/')
def index():
    return jsonify({
        'status': 'success',
        'message': '招聘网站后端API服务运行中',
        'time': datetime.now().isoformat()
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'database': 'connected',
        'time': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # 创建数据库表
    with app.app_context():
        db.create_all()

    # 启动应用
    app.run(debug=True, host='0.0.0.0', port=5000)