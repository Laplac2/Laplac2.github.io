# 移动系统所在分区

- [概述](#概述)
- [准备知识](#准备知识)
- [开始操作](#开始操作)
- [参考文献](#参考文献)

## 概述

Linux 系统中的某个文件改变存储位置，只要权限不变，并重新指定调用者的读取地址，系统并不会有什么异常。

这就是本操作实现的前提。

## 准备知识

需要对 Linux 手动分区了解，如果不会，接下来的操作可能让你的系统直接凉凉。

> 参考 [Linux 系统分区](system-partition.md)

## 开始操作

这里演示的是 EFI 引导的方式，传统 BISO 类似。

- 新系统与原系统在同一块硬盘的情况

  1. 原来的硬盘中至少有一个空白的分区。提前准备好，大小应至少能放下你原来的系统。
  2. 制作好一个启动盘。在空白的分区上安装一遍系统，安装的时候不需要重新指定 EFI 引导分区，安装成功后重启进入原系统正式开始操作。
  3. 将原系统根分区和 HOME 分区的文件复制到新分区中：

     ```bash
     blkid                                  # 查看所有分区
     mkdir /mnt/newroot /mnt/newhome        # 创建挂载目录
     mount /dev/nvme0n1pX /mnt/newroot      # 挂载新根分区
     mount /dev/nvme0n1pY /mnt/newhome      # 挂载新 HOME 分区
     sudo rsync -avx / /mnt/newroot/        # 复制根分区，注意 rsync 用法
     sudo rsync -avx /home/ /mnt/newhome/   # 复制 HOME 分区
     sudo vim /mnt/newroot/etc/fstab        # 修改开机挂载分区为新分区，仅修改 UUID 即可
     sudo update-grub2                      # 更新 grub，注意关注引导项
     reboot                                 # 确认上述步骤无误，重启选择引导新系统
     ```

  4. 不出意外的话，即可成功进入新系统。确认 `/etc/fstab` 文件内容无误，多重启几次，保证你进入的是新系统，删除或安装一些大文件，看你新系统所在分区的使用率是否发生变化。
  5. 确认新系统开机一切正常后，就可以着手删除原系统挂载项了：

     ```bash
     blkid                                  # 查看所有分区
     mkdir /mnt/oldroot                     # 创建挂载目录
     mount /dev/nvme0n1pX /mnt/oldroot      # 挂载原系统根分区
     sudo vim /mnt/newroot/etc/fstab        # 注释文件中所有的挂载项
     sudo update-grub2                      # 更新 grub 后，就只有一个引导项了
     reboot                                 # 确认上述步骤无误，重启选择引导新系统
     ```

  6. 如果第 5 步执行完，成功进入新系统，那么恭喜你，操作成功。接下来享受新系统的同时可以放心删除原系统，将原来的空间再利用了。

- 新系统与原系统在不同硬盘的情况

  1. 新硬盘中至少有一个空白的分区。提前准备好，大小应至少能放下你原来的系统。
  2. 制作好一个启动盘。在空白的分区上安装一遍系统，安装的时候要重新指定 EFI 引导分区，安装成功后重启进入原系统正式开始操作。
  3. 将原系统根分区和 HOME 分区的文件复制到新分区中：

     ```bash
     blkid                                  # 查看所有分区
     mkdir /mnt/newroot /mnt/newhome        # 创建挂载目录
     mount /dev/nvme0n1pX /mnt/newroot      # 挂载新根分区
     mount /dev/nvme0n1pY /mnt/newhome      # 挂载新 HOME 分区
     sudo rsync -avx / /mnt/newroot/        # 复制根分区，注意 rsync 用法
     sudo rsync -avx /home/ /mnt/newhome/   # 复制 HOME 分区
     sudo vim /mnt/newroot//etc/fstab       # 修改开机挂载分区为新分区，仅修改 UUID 即可
     sudo update-grub2                      # 更新 grub，注意关注引导项
     reboot                                 # 确认上述步骤无误，重启选择引导新系统
     ```

  4. 不出意外的话，即可成功进入新系统。确认 `/etc/fstab` 文件内容无误，打开分区管理器，卸载原来的 EFI 分区，并更新 grub。

     ```bash
     sudo grub-install /dev/nvme0n1pX   # 在新硬盘上的 EFI 分区重新安装 grub
     sudo update-grub2                  # 更新 grub
     ```

  5. 多重启几次，保证你进入的是新系统，删除或安装一些大文件，看你新系统所在分区的使用率是否发生变化。
  6. 确认新系统开机一切正常后，就可以着手删除原系统挂载项了：

     ```bash
     blkid                                  # 查看所有分区
     mkdir /mnt/oldroot                     # 创建挂载目录
     mount /dev/nvme0n1pX /mnt/oldroot      # 挂载原系统根分区
     sudo vim /mnt/newroot/etc/fstab        # 注释文件中所有的挂载项
     sudo update-grub2                      # 更新 grub 后，就只有一个引导项了
     reboot                                 # 确认上述步骤无误，重启选择引导新系统
     ```

  7. 如果第 6 步执行完，成功进入新系统，那么恭喜你，操作成功。接下来享受新系统的同时可以放心删除原系统，将原来的空间再利用了。

## 参考文献

- [deepin wiki 修复启动](<[修复启动](https://wiki.deepin.org/wiki/%E4%BF%AE%E5%A4%8D%E5%90%AF%E5%8A%A8#EFI.2BGPT.E6.A8.A1.E5.BC.8F.E4.B8.8B.E4.BF.AE.E5.A4.8DGRUB2.E5.8F.8C.E7.B3.BB.E7.BB.9F.E5.BC.95.E5.AF.BC)>)
