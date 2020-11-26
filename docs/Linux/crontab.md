# cron

## 简介

crond 是linux用来定期执行程序的命令。当安装完成操作系统之后，默认便会启动此任务调度命令。crond命令每分锺会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作。

```bash
/sbin/service crond start   # 启动服务
/sbin/service crond stop    # 关闭服务
/sbin/service crond restart # 重启服务
/sbin/service crond reload  # 重新载入配置
```

## Reference

-[linux定时任务的设置 crontab 配置指南](https://blog.csdn.net/xiyuan1999/article/details/8160998)
