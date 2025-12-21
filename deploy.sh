#!/bin/sh

# 如果发生错误，立即停止脚本
set -e

# 1. 打印提示
printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# 2. 清理旧的生成文件 (防止旧样式残留)
rm -rf public

# 3. 重新生成静态网站
# 如果你的主题在 themes/PaperMod，通常不需要额外参数，直接 hugo
hugo

# 4. 进入 public 文件夹 (如果你是把 public 文件夹部署到 gh-pages 或 master)
# 注意：如果你是把整个项目源码推上去用 GitHub Actions 构建，请跳过这一步，直接看“方法二”
# 假设你是手动部署 public 文件夹：
cd public

# 5. 添加更改到 git
git add .

# 6. 提交更改
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# 7. 强制推送到远程仓库 (Force Push)
# 这里的 master 可能是 main，根据你的仓库分支名修改
git push origin master --force

# 8. 回到根目录
cd ..

# 9. (可选) 把源码也推送到 source 分支 (好习惯)
# git add .
# git commit -m "$msg"
# git push origin source