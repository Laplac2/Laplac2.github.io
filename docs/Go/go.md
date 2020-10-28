# Go

## 环境配置

1. 方法一

   ```bash
   sudo apt build-dep startdde dde-daemon
   sudo apt install golang-go
   ```

2. 方法二

   - 下载 go

     Go 官网下载地址：<https://golang.org/dl/>

     Go 官方镜像站（推荐）：<https://golang.google.cn/dl/>

   - 修改 `/etc/profile` 或 `~/.bashrc` 文件

     ```bash
     export GOROOT=/usr/local/go               # Tools environment 这里存放的是安装的依赖包
     export PATH=$PATH:$GOROOT/bin             # 添加 go 可执行文件路径到环境变量中
     export GOPROXY=https://goproxy.cn,direct  # 添加代理
     ```

## 参考文献

- [从零开始搭建 Go 语言开发环境](https://www.liwenzhou.com/posts/Go/install_go_dev/)
