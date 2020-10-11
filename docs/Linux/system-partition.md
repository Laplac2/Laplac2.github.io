# System Partition for Linux

- [1. 简介](#1-简介)
- [2. 迁移 home 目录至其它分区](#2-迁移-home-目录至其它分区)
- [3. 改变分区大小](#3-改变分区大小)

## 1. 简介

Linux 系统里所有东西都是文件，指定的文件对了，系统就可以正常启动。分区挂载的过程保证文件内容、权限和位置对于系统来说没变化就不会报错。所有文件都是在`/`路径下，第一次安装系统的时候，分区保证挂载`/`目录就可以了，加个`linux-swap`分区会更好，没有也没关系，理论只有这两个分区就足够了，但是在`UEFI`引导方式下，需要单独挂载`efi`分区，这个分区的格式是`atf32`,跟`/`的格式不同（`ext4`），同时为了用户数据的安全性，可以将`/home`目录放到其它分区（最好是其它硬盘），在系统挂了的时候，可以通过不影响挂载在`/home`路径下的数据重装系统，保证用户数据不丢失。

## 2. 迁移 home 目录至其它分区

先挂载`/dev/sdc`到`/mnt/tmp`（可以挂载到`/`下的任何一个目录中，只有挂载了才能访问到新分区中的数据），将原有的`/home`路径下的数据同步到新分区中。

```bash
sudo mkdir /mnt/tmp             # 新建目录
mount /dev/sdc /mnt/tmp         # 挂载新分区
sudo rsync -avx /home /mnt/tmp  # 同步原来home目录里的用户数据
```

数据同步完成后，可以选择删除原来`/home`路径下的数据，也可以选择保留，如果保留，在将其它分区挂载在`/home`路径后，原来的数据将不可访问，相当于隐藏了。

```bash
sudo rm -rf /home/*         # 删除原来的/home路径下的文件
sudo umount -l /home        # 取消原来挂载在/home路径下的分区
sudo mount /dev/sdc /home   # 将新分区挂载在/home路径下
```

到这一步已经基本完成了`/home`路径的挂载问题，但是重启了就不行了，如果需要开机自动挂载这个新分区到`/home`路径下，需要修改`/etc/fstab`配置文件，因为一开机，系统会先去读取这个文件，挂载相应的分区，再执行接下来的步骤，如果没有新分区相关的挂载信息，新分区是不会被挂载的。

```bash
sudo blkid  # 获取硬盘信息，UUID
# /dev/sdb1: UUID="xxxx" TYPE="ext3" PARTUUID="5b9f9d07-01"
# /dev/sdc: LABEL="YUNIFYSWAP" UUID="xxx" TYPE="ext4"
# /dev/sda1: UUID="xxx" TYPE="ext4" PARTUUID="d6ee97c2-01"
sudo vim /etc/fstab  # 编辑配置文件
# /dev/sdax
# UUID=XXXXXXXXX    /data    ext4    rw,relatime    0,0
# /data/home /home none defaults,bind 0 0
sudo mount -a   # mount all filesystems mentioned in fstab
df -h           # 查看所有挂载信息
```

## 3. 改变分区大小

当`/`所在分区比较小，想扩大时，由于在分区编辑器中无法卸载`/home`分区导致无法调整分区大小，这时可以在分区编辑器中，将最后面的`linux-swap`分区删除，新建为 ext4 格式的主分区（假设为/dev/sdd3），然后挂载在`/mnt/tmp`中，再新建一个用户（假设为 uos），仅将这个用户的信息迁移至这个分区中，再用这个用户登录系统，用分区编辑器即可操作原来的`/home`分区了。

```bash
sudo mkdir /mnt/tmp1                #新建目录
mount /dev/sdd3 /mnt/tmp1           #挂载新分区
sudo rsync -avx /home/uos /mnt/tmp1 #同步原来home目录里的用户数据
```

或者在`/etc/fstab`文件中注释`/home`分区的相关挂载配置项，重启电脑新建用户就可以卸载原来的`/home`分区了，然后再执行上面的操作就可以了。
