# wget

## 概述

## 应用

```bash
wget url
wget --spider url           # 测试下载链接
wget -c url                 # 断点续传
wget -b url                 # 后台下载，下载过程输出的日志保存在当前目录 wget-log 文件中
wget -O filename.zip url    # 指定下载文件保存名称，如果不指定，默认以 url 最后一个 / 后面的字符串作为文件名
wget --limit-rate=300k url  # 限制下载速度
wget --tries=40 URL         # 指定重试次数，0代表无限制
wget -i filelist.txt        # 下载多个文件
```

- FTP 下载

  ```bash
  wget ftp-url                                          # 使用 wget 匿名 ftp 下载
  wget --ftp-user=USERNAME --ftp-password=PASSWORD url  # 使用 wget 用户名和密码认证的ftp下载
  ```

## Reference

- [wget 命令](https://man.linuxde.net/wget)
- [每天一个 linux 命令（61）：wget 命令](https://www.cnblogs.com/peida/archive/2013/03/18/2965369.html)
