# dd

## 简介

## 应用

```bash
dd if=/dev/sda1 of=/dev/sdb1
```

这里要注意的是拷贝的源和目标分别是 `/dev/sda1` 和 `/dev/sdb1` 这两个分区，而不是 `/dev/sda` 和 `/dev/sdb` 这两个硬盘名称。
最后更新一下硬盘信息（不然显示的大小信息等还是旧硬盘的信息）

```bash
umount /dev/sdb1　　　　　　　　　// 记得在操作之前先卸载所有挂载
e2fsck -f /dev/sdb1
resize2fs /dev/sdb1
```

dd 工具会将 uuid 也一起拷贝，所以拷贝完成之后，只要将旧的硬盘拆卸下来，替换上新的硬盘，不用修改 /etc/fstab 文件，就能按照你以前的设置自动挂载。

## 参考文献

- [把整个 Linux 系统迁移到另一个硬盘](https://www.jianshu.com/p/82b413ffc40c)
