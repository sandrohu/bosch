#!/bin/bash

# 简单部署脚本 - 用于测试环境
echo "========================================="
echo "开始简单部署..."
echo "========================================="

# 1. 检查并停止占用80端口的服务
echo "1. 检查80端口..."
if lsof -Pi :80 -sTCP:LISTEN -t >/dev/null ; then
    echo "端口80被占用，尝试停止Apache..."
    systemctl stop httpd 2>/dev/null || true
    systemctl disable httpd 2>/dev/null || true
fi

# 2. 进入项目目录
cd /root/dev/bosch || exit 1

# 3. 拉取最新代码（忽略本地修改）
echo "2. 拉取最新代码..."
git stash
git pull origin main --force

# 4. 构建前端
echo "3. 构建前端..."
cd frontend
npm install
npm run build

# 5. 部署文件
echo "4. 部署文件到nginx目录..."
rm -rf /usr/share/nginx/html/*
cp -r dist/* /usr/share/nginx/html/

# 6. 配置nginx（使用简单配置）
echo "5. 配置nginx..."
cat > /etc/nginx/conf.d/default.conf << 'EOF'
server {
    listen 80;
    server_name _;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|webp|mp4|m4v)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# 7. 设置权限
echo "6. 设置权限..."
chown -R nginx:nginx /usr/share/nginx/html
chmod -R 755 /usr/share/nginx/html

# 8. 测试nginx配置
echo "7. 测试nginx配置..."
nginx -t

# 9. 启动nginx
echo "8. 启动nginx..."
systemctl restart nginx || systemctl start nginx

# 10. 检查状态
echo "9. 检查nginx状态..."
if systemctl is-active --quiet nginx; then
    echo "✅ Nginx运行正常"
    SERVER_IP=$(curl -s ifconfig.me 2>/dev/null || hostname -I | awk '{print $1}')
    echo "========================================="
    echo "部署成功！"
    echo "访问地址: http://$SERVER_IP"
    echo "========================================="
else
    echo "❌ Nginx启动失败，请检查错误："
    systemctl status nginx --no-pager
    journalctl -xe | tail -20
fi