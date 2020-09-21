# pluseaudio

灵活运用 amixer, alsamixer 命令

查看声卡的 index 编号：

```bash
cat /proc/asound/cards
```

比如结果是：

```bash
 0 [I82801AAICH    ]: ICH - Intel 82801AA-ICH
                      Intel 82801AA-ICH with AD1980 at irq 21
```

这个声卡 Intel 82801AA-ICH 的 index 为 0， name 为 `I82801AAICH`。

查看这个声卡的控制内容：

```bash
amixer -c 0 contents
# 或
amixer -c I82801AAICH  contents
```

alsamixer 进入 TUI 环境后，按 F6 选择声卡。

把 pulseaudio 的日志打开，就能看到很多相关日志。

```bash
systemctl --user edit --full pulseaudio.service
```

打开编辑器，然后修改 ExecStart 命令为 `/usr/bin/pulseaudio --daemonize=no --log-level=debug`

`/usr/share/pulseaudio/alsa-mixer` 文件夹下

paths 文件夹内的 `.conf` 定义了 path，每个 path 和选项们组合就能形成 port。

profile-sets 内的文件定义了 profile，比如常见的 analog-stereo 模拟立体声。

## 扬声器与模拟耳机

端口 analog-output-speaker 被称为扬声器，端口 analog-output-headphones 被称为模拟耳机。在插入模拟耳机时，扬声器就能被自动禁用， 由于耳机孔 `Jack Headphone` 的状态 state 发生了改变，从拔出（unplugged）变成插入（plugged）。

`paths/analog-output-speaker.conf` 中有定义如果耳机孔 `Jack Headphone` 插入，则此 path 的状态变为不可用。

```bash
[Jack Headphone]
state.plugged = no
state.unplugged = unknown
```

当把扬声器了设置为活跃端口时，禁用模拟耳机。

```bash
; This profile path is intended to control the speaker, let's mute headphones
; else there will be a spike when plugging in headphones
[Element Headphone]
switch = off
volume = off
```

而在 `paths/analog-output-headphones.conf` 中有定义如果耳机孔 `Jack Headphone` 插入，则此 path 的状态变为可用。
由于 state.plugged 默认是 yes 而 state.unplugged 默认是 no 就省略了没有写出来。

当把模拟耳机设置为活跃端口时，禁用扬声器。

```bash
[Element Speaker]
switch = off
volume = off
```

如果没有把扬声器识别为 analog-output-speaker 或没有把耳机识别为 analog-output-headphones 就会出现插入耳机，但是扬声器和耳机同时能听到音乐。
