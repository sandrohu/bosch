# 招聘网站项目

一个基于Vue 3 + Flask的前后端分离招聘网站，支持PC端和移动端自适应。

## 技术栈

### 前端
- Vue 3 + Vite
- Vue Router 4
- Element Plus UI组件库
- Axios HTTP客户端

### 后端
- Flask Web框架
- SQLAlchemy ORM
- SQLite数据库
- Flask-CORS跨域处理
- Flask-JWT-Extended认证

## 项目结构

```
.
├── backend/                # 后端Flask项目
│   ├── app.py             # 主应用入口
│   ├── models.py          # 数据模型
│   ├── routes.py          # API路由
│   ├── config.py          # 配置文件
│   └── requirements.txt   # Python依赖
│
└── frontend/              # 前端Vue项目
    ├── src/
    │   ├── api/          # API接口封装
    │   ├── views/        # 页面组件
    │   ├── router/       # 路由配置
    │   ├── App.vue       # 根组件
    │   └── main.js       # 入口文件
    └── package.json      # Node依赖
```

## 快速开始

### 后端启动

```bash
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行服务
python app.py
```

后端服务将在 http://localhost:5000 启动

### 前端启动

```bash
cd frontend

# 安装依赖
npm install

# 开发模式运行
npm run dev
```

前端服务将在 http://localhost:5173 启动

## 功能模块

### 已实现的基础框架
- ✅ 项目结构搭建
- ✅ 路由配置
- ✅ 数据模型定义
- ✅ API接口框架
- ✅ 页面组件框架

### 待开发功能
- ⏳ 用户注册登录
- ⏳ 职位发布与管理
- ⏳ 简历投递
- ⏳ 公司信息管理
- ⏳ 搜索筛选功能

## API接口

### 认证相关
- POST `/api/auth/register` - 用户注册
- POST `/api/auth/login` - 用户登录

### 职位相关
- GET `/api/jobs` - 获取职位列表
- GET `/api/jobs/:id` - 获取职位详情
- POST `/api/jobs` - 创建职位

### 公司相关
- GET `/api/companies` - 获取公司列表
- GET `/api/companies/:id` - 获取公司详情

### 申请相关
- POST `/api/applications` - 提交申请
- GET `/api/applications` - 获取申请列表

## 开发计划

- Day 1-2: 项目框架搭建 ✅
- Day 3-4: 核心API开发
- Day 5-6: 前端页面实现
- Day 7: 联调与部署

## 注意事项

1. 开发环境需要Python 3.8+和Node.js 16+
2. 前端开发时需要配置`.env`文件设置API地址
3. 生产环境部署时需要修改配置文件中的密钥

## License

MIT