# SSH

- [生成密钥](#生成密钥)
- [配置密钥](#配置密钥)
- [添加密钥](#添加密钥)
- [备注](#备注)

## 生成密钥

```bash
ssh-keygen -t rsa -C "xxx@xx.xxx"  # 配置的邮箱。
```

在按下第一个回车的时候会出现提示让你指定 rsa 文件存放的位置，此时如果你要添加 github 的密钥可以输入：`id_rsa_github`（gitlab 同理)。
后面直接按下二个回车，这样密钥就会生成到 .ssh 目录下，存放名为`id_rsa_github.pub`这里。
将 pub 里面的内容全部复制到 github、gitlab 中的 SSH 中。

## 配置密钥

在`~/.ssh/config`中编辑如下内容：

```bash
# gitlab
Host gitlab.deepin.io
HostName gitlab.deepin.io
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_gitlab
# github
Host github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_github
```

## 添加密钥

默认情况下只会读取 id_rsa 文件，如果想将二个公钥 github、gitlab 一起读取需要使用命令：`ssh-add ~/.ssh/id_rsa_github`（gitlab 同理)可以使用`ssh-add -l`查看秘钥。

## 备注

在 UOS 中不需要执行`ssh-add ~/.ssh/id_rsa_gitlab`命令，但是在 Windows 中需要。
在 Windows 中提示“Could not open a connection to your authentication agent.”时，先执行`ssh-agent bash`即可。
