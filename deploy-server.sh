#!/bin/bash

# 博世项目服务器部署脚本
# 使用方法: 在服务器上执行 bash deploy-server.sh

echo "========================================="
echo "开始部署博世项目..."
echo "========================================="

# 进入项目目录
cd /root/dev/bosch || exit 1

# 保存本地修改（如果有）
echo "1. 保存本地修改..."
git stash

# 拉取最新代码
echo "2. 拉取最新代码..."
git pull origin main

# 进入前端目录
cd frontend || exit 1

# 安装依赖
echo "3. 安装依赖..."
npm install

# 构建项目
echo "4. 构建项目..."
npm run build

# 复制构建文件到nginx目录
echo "5. 部署到nginx..."
rm -rf /usr/share/nginx/html/*
cp -r dist/* /usr/share/nginx/html/

# 设置权限
echo "6. 设置文件权限..."
chown -R nginx:nginx /usr/share/nginx/html
chmod -R 755 /usr/share/nginx/html

# 重启nginx
echo "7. 重启nginx..."
systemctl restart nginx

# 检查nginx状态
echo "8. 检查nginx状态..."
systemctl status nginx --no-pager

echo "========================================="
echo "部署完成！"
echo "请访问: http://bos-china.com"
echo "========================================="