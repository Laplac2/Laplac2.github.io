# GRUB

- [1. 配置文件](#1-配置文件)
- [2. 参考文献](#2-参考文献)

## 1. 配置文件

```bash
sudo vim /boot/grub/grub.cfg  # grub所在的包 grub-common 配置文件由grub-mkconfig生成
sudo vim /etc/grub.d/xxx      # grub-mkconfig读取的模板文件
sudo vim /etc/default/grub    # grub-mkconfig读取的设置文件
# grub-mkconfig读取的个性化设置文件
sudo vim /etc/grub.d/40_custom    # edit
sudo vim /boot/grub/custom.cfg    # create
# grub界面个性化设置文件
sudo vim /boot/grub/themes/deepin/theme.txt
# 配置文件编辑好后
sudo grub-mkconfig
sudo update-grub
```

## 2. 参考文献

- [GNU](https://www.gnu.org/software/grub/manual/grub/grub.html#Configuration)
