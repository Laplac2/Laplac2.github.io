# UnionTech Operate System

- [命令](#命令)
- [依赖](#依赖)
- [DBUS](#dbus)
- [gsettings](#gsettings)
- [抓取控制中心 coredump 文件](#抓取控制中心-coredump-文件)
- [dde-daemon 调试方式](#dde-daemon-调试方式)
- [startdde 调试方式](#startdde-调试方式)
- [显卡驱动](#显卡驱动)
- [QA](#qa)
- [参考资料](#参考资料)

## 命令

```bash
sudo libinput debug-events
sudo journalctl -b 0 /usr/lib/deepin-daemon/dde-session-daemon > texx.txt
systemd-inhibit
sudo apt install libinput-tools
cat /boot/efi/version.txt
dde_wloutput get
sudo apt-get update --fix-missing
hexdump /dev/input/eventN
libgles2-mesa-dev
sudo find / -name "gl2.h"
git remote prune upstream
git remote show origin
sudo apt install libgtk-3-dev
sudo dpkg -i startdde_5.3.0.2-1_arm64.deb
dbus-mintior "interface=com.deepin.dde.osd"
xev
sudo coredumpctl
ps -ef | grep startdde
ps -aux | grep startdde
sudo journalctl _PID=<startdde>
sudo journalctl /usr/bin/startdde
sudo vim /usr/bin/kwin_wayland_helper
tail -f kwin.log
sudo journalctl -b 0
sudo chmod a+x <>
pstree
strace
export DISPLAY=:0
xprop -root
ltrace
xwininfo xxx
xdotool selectwindow
xprop
sudo chvt 2    # 命令行切tty
rmdir -p *     # 批量删除当前目录下的空文件夹
sudo lshw -numeric -C display    # 查看显卡信息
dmesg
```

## 依赖

- libdde-network-utils-dev
- qtmultimedia5-dev

## DBUS

```bash
dbus-send --print-reply --dest=com.deepin.daemon.Network /com/deepin/daemon/Network com.deepin.daemon.Network.GetActiveConnectionInfo
```

## gsettings

```bash
gsettings set com.deepin.dde.watchdog dde-dock false
```

## 抓取控制中心 coredump 文件

1. 抓取控制中心 coredump 文件
   `sudo apt install systemd-coredump`
2. 安装控制中心调试符号信息
   `sudo apt install dde-control-center-dbgsym`
3. 配置`/etc/profile` 中加上 `ulimit -c unlimited` 生成 coredump 文件
4. 复现问题等崩溃后马上使用 coredumpctl dump 可以查看堆栈信息

## dde-daemon 调试方式

1. 替换新编译的 dde-session-daemon 二进制文件

   1. 备份旧的 dde-session-daemon

      ```bash
      sudo mv /usr/lib/deepin-daemon/dde-session-daemon
      /usr/lib/deepin-daemon-bak dde-session-daemon
      ```

   2. 进入到 dde-daemon 目录，再将新生成的 dde-session-daemon 拷贝到/usr/lib/deepin-daemon/

      ```bash
      cd xxx/dde-daemon
      sudo cp out/bin/dde-session-daemon /usr/lib/deepin-daemon/
      ```

2. 调试 dde-daemon 中的 dde-session-daemon
   DDE_DEBUG_MATCH 表示模块
   DDE_DEBUG_LEVEL 表示 log 等级
   杀掉旧的 dde-session-daemon 进程，再启动新的 dde-session-daemon 进程
   以下是一个举例：
   调试 dde-session-daemon 的 session power 模块

   ```bash
   export DDE_DEBUG_MATCH=power
   export DDE_DEBUG_LEVEL="debug"
   pkill -ef dde-session-daemon;/usr/lib/deepin-daemon/dde-session-daemon
   ```

3. 使用脚本调用命令
   可以将这 3 条命令放入一个　.sh 文件，比如叫 power.sh

   1. 新建脚本`touch power.sh`
   2. 给脚本赋权限`chmod +x power.sh`
   3. 将命令拷贝到脚本
      直接打开 power.sh 脚本，将命令拷贝进去

      ```bash
      export DDE_DEBUG_MATCH=power
      export DDE_DEBUG_LEVEL="debug"
      pkill -ef dde-session-daemon;/usr/lib/deepin-daemon/dde-session-daemon
      ```

   4. 在终端执行脚本`./power`

## startdde 调试方式

1. 进入到 startdde 代码目录，安装编译后的生成文件
   `sudo make install`
   一般调试也可以直接将 startdde 拷贝到`/usr/bin/`目录(前提要先删除，或者重命名旧的 startdde)

2. 打开`/etc/X11/Xsession.d/00deepin-dde-env`，添加 log 等级，模块
   　即在这个文件的开头写入：

   ```bash
   export DDE_DEBUG_MATCH=display
   export DDE_DEBUG_LEVEL="debug"
   ```

3. 注销系统
   　说明：startdde 只有注销或者重启后才能生效，若 startdde 不存在,则桌面环境会崩溃

4. 查看 startdde 进程

   ```bash
   ps -ef|grep startdde # 假如进程 id 为：1111
   ```

5. 查看 startdde 的日志

   ```bash
   sudo journalctl _PID ＝ 1111
   sudo journalctl /usr/bin/startdde
   ```

6. 查看关机 log

   ```bash
   journalctl --user -b-1 /usr/bin/startdde
   ```

## 显卡驱动

- NVIDIA

  ```bash
  sudo apt install nvidia-driver -y # 安装 NVIDIA 驱动
  sudo apt-get install nvidia-driver nvidia-smi
  ```

## QA

- 输入法异常

  ```bash
  sudo apt remove fcitx --purge  # 完全卸载，包含配置文件
  sudo apt install dde fcitx-googlepinyin
  ```

- 编译时提示系统时间不对

  ```bash
  find . -type f -exec touch {} \;
  ```

## 参考资料

- [Git 操作整理-基础篇](https://mp.weixin.qq.com/s/XW0x59Arw3Qqpl4G5ORWmw)
- [深度操作系统通用性规范](https://shimo.im/docs/J9hVdDGKdxtCKytj/read)
- [DDE 桌面需求](https://wikidev.uniontech.com/index.php?title=DDE%E6%A1%8C%E9%9D%A2%E9%9C%80%E6%B1%82%E5%9C%B0%E5%9D%80)
- [Wayland 及相关概念介绍](https://wikidev.uniontech.com/index.php?title=Wayland%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%A6%82%E5%BF%B5%E4%BB%8B%E7%BB%8D)
- [多点手势测试用例](https://pms.uniontech.com/zentao/testcase-browse-11--byModule-843.html)
- [查看日志的方式](https://wikidev.uniontech.com/index.php?title=%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8journalctl%E5%91%BD%E4%BB%A4%E8%8E%B7%E5%8F%96Linux%E6%97%A5%E5%BF%97)
