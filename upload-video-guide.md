# 视频上传到GitHub Releases指南

## 步骤：

1. **访问你的GitHub仓库**
   - https://github.com/sandrohu/bosch

2. **创建新的Release**
   - 点击右侧的 "Releases"
   - 点击 "Create a new release"

3. **上传视频文件**
   - 填写版本号（如 v1.0.0-media）
   - 在底部的 "Attach binaries" 区域拖拽视频文件
   - 文件会自动上传（最大2GB）

4. **获取视频直链**
   - 发布Release后，右键视频文件
   - 复制链接地址

5. **在代码中使用**
   ```javascript
   // 替换本地路径为GitHub Release链接
   const videoUrl = 'https://github.com/sandrohu/bosch/releases/download/v1.0.0-media/whybosch.mp4'
   ```

## 注意事项：
- GitHub Releases不计入仓库大小
- 支持断点续传
- 全球CDN加速
- 无需额外注册账号