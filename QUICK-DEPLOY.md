# 快速部署指南（测试环境）

## 最简单的部署方法

直接在服务器上执行以下命令：

```bash
# 1. 进入项目目录
cd /root/dev/bosch

# 2. 拉取最新部署脚本
git stash
git pull origin main

# 3. 执行简单部署
bash deploy-simple.sh
```

## 手动部署步骤

如果脚本执行失败，可以手动执行：

```bash
# 1. 停止占用80端口的Apache（如果有）
systemctl stop httpd
systemctl disable httpd

# 2. 进入项目并构建
cd /root/dev/bosch/frontend
npm install
npm run build

# 3. 部署到nginx
rm -rf /usr/share/nginx/html/*
cp -r dist/* /usr/share/nginx/html/

# 4. 创建简单的nginx配置
cat > /etc/nginx/conf.d/default.conf << 'EOF'
server {
    listen 80;
    server_name _;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
EOF

# 5. 启动nginx
nginx -t  # 测试配置
systemctl restart nginx
```

## 访问网站

部署成功后，直接通过服务器IP访问：
- http://你的服务器IP

## 常见问题解决

### 1. 端口80被占用
```bash
# 查看占用端口的进程
lsof -i :80

# 停止Apache
systemctl stop httpd
```

### 2. Nginx启动失败
```bash
# 查看错误
systemctl status nginx
journalctl -xe

# 检查配置
nginx -t
```

### 3. 页面404错误
确保nginx配置中有正确的try_files指令来支持Vue Router。

## 查看服务器IP
```bash
curl ifconfig.me
# 或
hostname -I
```