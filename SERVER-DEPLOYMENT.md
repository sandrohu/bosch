# 服务器部署指南

## 服务器信息
- 域名: bos-china.com
- 服务器: 阿里云 ECS
- 系统: Linux
- Web服务器: Nginx

## 快速部署

在服务器上执行以下命令解决冲突并部署：

```bash
# 1. 进入项目目录
cd /root/dev/bosch

# 2. 保存本地修改并拉取最新代码
git stash
git pull origin main

# 3. 进入前端目录并构建
cd frontend
npm install
npm run build

# 4. 部署到nginx
rm -rf /usr/share/nginx/html/*
cp -r dist/* /usr/share/nginx/html/
chown -R nginx:nginx /usr/share/nginx/html
chmod -R 755 /usr/share/nginx/html

# 5. 重启nginx
systemctl restart nginx
```

## 使用自动部署脚本

也可以使用自动部署脚本：

```bash
# 下载并执行部署脚本
curl -O https://raw.githubusercontent.com/sandrohu/bosch/main/deploy-server.sh
bash deploy-server.sh
```

## 常见问题

### 1. Git冲突问题
如果遇到 `package-lock.json` 冲突：
```bash
git stash  # 保存本地修改
git pull   # 拉取最新代码
```

### 2. 端口占用
如果80端口被占用：
```bash
lsof -i :80  # 查看占用进程
systemctl stop httpd  # 停止Apache（如果存在）
```

### 3. Nginx配置
确保nginx配置正确：
```bash
nginx -t  # 测试配置
systemctl reload nginx  # 重载配置
```

## 视频文件处理

大视频文件不要直接提交到Git，建议：
1. 使用云存储服务（如阿里云OSS）
2. 或直接上传到服务器的指定目录

上传视频到服务器：
```bash
# 在本地执行
scp whybosch.mp4 root@服务器IP:/usr/share/nginx/html/videos/
```

## 维护命令

```bash
# 查看nginx日志
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# 查看系统资源
df -h  # 磁盘空间
free -m  # 内存使用
top  # CPU使用
```