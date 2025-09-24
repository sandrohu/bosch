#!/bin/bash

# 部署脚本 - 在阿里云服务器上执行

echo "===== 开始部署Bosch应用 ====="

# 设置变量
PROJECT_DIR="/opt/bosch"
FRONTEND_DEPLOY_DIR="/var/www/bosch-frontend"
BACKEND_DEPLOY_DIR="/var/www/bosch-backend"

# 1. 克隆或更新代码
if [ -d "$PROJECT_DIR" ]; then
    echo ">>> 更新代码..."
    cd $PROJECT_DIR
    git pull origin main
else
    echo ">>> 克隆代码..."
    cd /opt
    git clone https://github.com/sandrohu/bosch.git
    cd $PROJECT_DIR
fi

# 2. 部署前端
echo ">>> 部署前端应用..."
cd $PROJECT_DIR/frontend

# 安装依赖
echo "  - 安装前端依赖..."
npm install

# 构建生产版本
echo "  - 构建生产版本..."
npm run build

# 创建部署目录并复制文件
echo "  - 部署前端文件..."
sudo mkdir -p $FRONTEND_DEPLOY_DIR
sudo rm -rf $FRONTEND_DEPLOY_DIR/*
sudo cp -r dist/* $FRONTEND_DEPLOY_DIR/
sudo chown -R nginx:nginx $FRONTEND_DEPLOY_DIR

# 3. 部署后端（如果需要）
# echo ">>> 部署后端应用..."
# cd $PROJECT_DIR/backend
# sudo mkdir -p $BACKEND_DEPLOY_DIR
# sudo cp -r * $BACKEND_DEPLOY_DIR/
# cd $BACKEND_DEPLOY_DIR
# pip3 install -r requirements.txt
# # 可以使用systemd或supervisor来管理后端服务

# 4. 重启服务
echo ">>> 重启Nginx..."
sudo systemctl reload nginx

echo "===== 部署完成！ ====="
echo "前端访问地址: http://你的服务器IP/"
echo "如需HTTPS，请配置Cloudflare或Let's Encrypt"