# LightDM

- [1. 简介](#1-简介)
- [2. 原理](#2-原理)
- [3. 源码分析](#3-源码分析)
  - [3.1 代码执行流程](#31-代码执行流程)
  - [3.2 LightDM 启动过程中与用户管理有关的初始化](#32-lightdm-启动过程中与用户管理有关的初始化)
  - [3.3 LightDM 管理的 Seat 与系统的 PAM 的关联](#33-lightdm-管理的-seat-与系统的-pam-的关联)
    - [3.3.1 LightDM 的核心类型：Seat 和 Session](#331-lightdm-的核心类型seat-和-session)
    - [3.3.2 主要的 Seat 对象以及其关联的 Session 的产生过程](#332-主要的-seat-对象以及其关联的-session-的产生过程)
  - [3.4 各部分含义](#34-各部分含义)
- [4. 参考文献](#4-参考文献)

## 1. 简介

- LightDM 是跨桌面显示管理器。其主要特点是：
  - 跨桌面-支持不同的桌面技术。
  - 支持不同的显示技术（X，Mir，Wayland ...）。
  - 轻量级-低内存使用率和高性能。
  - 支持访客会话。
  - 支持远程登录（传入-XDMCP，VNC，传出-XDMCP，可插入）。
  - 全面的测试套件。
  - 低代码复杂度。

## 2. 原理

## 3. 源码分析

- [https://github.com/Laplac2/lightdm](https://github.com/Laplac2/lightdm)

### 3.1 代码执行流程

- 加载默认配置并创建 run、log、cache 文件夹
- 初始化日志系统
  - 读取`/etc/lightdm/lightdm.conf`配置节`LightDM`的配置`log-directory`，返回配置文件中写的日志记录路径。
  - 读取`/etc/lightdm/lightdm.conf`配置节`LightDM`的配置`backup-logs`，如果返回`ture`，代表打开日志文件前先将旧文件重命名为`*.old`。
- 日志文件创建好后，将消息队列中的消息记录在日志中。
- 创建显示管理器，并建立`display_manager_stopped_cb`和`display_manager_seat_removed_cb`信号槽连接。
- 读取`/etc/lightdm/lightdm.conf`配置节`LightDM`的配置`dbus-service`，如果返回`TRUE`，代表有 dbus 服务，建立`service_add_xlocal_seat_cb`、`service_ready_cb`、`service_name_lost_cb`信号槽连接，并启动`display_manager_service`；如果返回`FALSE`，则直接启动`display_manager_service`。
- 监视用户目录，如果用户目录被删除，则执行删除用户的操作。
- ...

### 3.2 LightDM 启动过程中与用户管理有关的初始化

- 读取配置`/etc/lightdm/lightdm.conf`并初始化`lightdm.conf`没有赋值的配置节。这里重点关注与登录有关的配置
  - `start-default-seat`默认值`true`
  - `greeter-user`默认值`lightdm`
  - `sessions-directory`默认值`/usr/share/lightdm/sessions:/usr/share/xsessions:/usr/share/wayland-sessions`
  - `remote-sessions-directory`默认值`/usr/share/lightdm/remote-sessions`
  - `greeters-directory`默认值`$XDG_DATA_DIRS/lightdm/greeters:$XDG_DATA_DIRS/xgreeters`
  - `pam-service`默认值`lightdm`
  - `pam-autologin-service`默认值`lightdm-autologin`
  - `pam-greeter-service`默认值`lightdm-greeter`。
  - `dbus-service`默认值`true`
- `display_manager_new`函数初始化`display_manager`，此函数的主要作用是在 C 开发环境模拟单例模式
- `display_manager_stopped_cb`监听 DisplayManager 的`DISPLAY_MANAGER_SIGNAL_STOPPED`信号。此信号为停止 DisplayManager 的信息。监听函数调用`g_main_loop_quit`函数中断主程序`loop`循环，将程序正常退出。
- `display_manager_seat_removed_cb`监听`DISPLAY_MANAGER_SIGNAL_SEAT_REMOVED`信号。此信号由用户注销引发。监听函数要为下一次登录作准备。如果发生异常（通用由用户注销异常引发），它会停止`display_manager`的运行，间接引发程序退出。
- 读取`lightdm.conf`配置节`LightDM`的配置`dbus-service`
  - 如果为`true`
    - 通过`display_manager_service_new`函数创建`display_manager_service`服务。此函数的主要作用是在 C 开发环境模拟单例模式
    - `service_add_xlocal_seat_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_ADD_XLOCAL_SEAT`信号，此信号由用户登录成功触发，此监听函数准备专属于此用户的 D-Bus 服务。
    - `service_ready_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_READY`信号。此信号在专属于此用户的的 D-Bus 服务准备就绪后触发
    - `service_name_lost_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_NAME_LOST`信号。此监听函数会在不正常停止`display_manager`的运行的情况下直接将程序退出，而且没有输出日志，需要关注。
    - `display_manager_service_start`启动 DisplayManager 的 D-Bus 服务。如果启动身份是 root 则注册到系统 Bus，否则注册到用户 Bus。
  - 如果为`false`
    - 执行`start_display_manager`函数。此函数会检测用户是否启用了`XDMCPServer`服务、`VNCServer`服务。如果启用了就会把这些服务启动。
- 执行`shared_data_manager_start`函数。此函数会遍历`home`目录，监听子目录的删除事件。如果发生删除事件就引发`USER_LIST_SIGNAL_USER_REMOVED`信号，执行`user_removed_cb`监听函数。监听函数进一步执行删除用户操作。
- 执行`login1_service_connect`函数。此函数获取`Login1Service`的单例模式，调用`g_bus_get_sync`连接系统 D-Bus，连上`org.freedesktop.login1`，立即请求`ListSeats`服务，返回结果保存到用户列表。
  - 如果为`true`
    - 读取配置节`LightDM`下`start-default-seat`配置。此配置指示默认登录的用户。
      - 如果读取成功
        - `login1_service_seat_added_cb`函数监听`LOGIN1_SERVICE_SIGNAL_SEAT_ADDED`信号，此信号由用户登录成功触发
        - `login1_service_seat_removed_cb`函数监听`LOGIN1_SERVICE_SIGNAL_SEAT_REMOVED`信号，此信号由用户注销触发。
      - 如果读取失败
        - 不做任何事情。
  - 如果为`false`
    - 读取配置节`LightDM`下`start-default-seat`配置。
      - 如果读取成功
        - 读取配置节`Seat:*`下`type`配置，保存到`types`
        - 遍历`types`，保存到`type`。调用`create_seat`，保存到`seat`。如果`seat`不为空则停止遍历。
        - 如果`seat`不为空则执行`display_manager_add_seat`函数，注册`seat`提供登录服务
        - 如果注册`seat`失败就直接退出程序。此过程没有输出日志，需要关注。
      - 如果读取失败
        - 不做任何事情。
- 执行`g_main_loop_run`，此函数的主要作用是内存驻留。
- 清理用户列表，断开 D-Bus 连接
- 释放`display_manager_service`和`display_manager`的内存
- 退出。

### 3.3 LightDM 管理的 Seat 与系统的 PAM 的关联

#### 3.3.1 LightDM 的核心类型：Seat 和 Session

&emsp;&emsp;`Seat`和`Session`都是一个派生自[`GObject`](https://developer.gnome.org/gobject/stable/)类型的对象。`GObject`是 GLibC 用 C 语言模拟的类，它在 C 语言上实现了 OOP。它是 GLibC 运行时下对象的基类型，与 Qt 的`QObject`在设计思想有许多相似之处。比如在对象的内存管理方面都有一个内存池的设计、对象的引用也有强引用和弱引用之分，对象或模块之间的通信都有一个信号槽的设计、在对象的存储结构方面都提供了一个 Variant 类型的设计用于动态增加、修改、删除对象的属性等等。举例说明，Qt 支持用户把不想管理内存的对象可以通过继承 QObject 交给 Qt 运行时管理，使用的时候只管 new 一个出来，不必使用智能指针包装。GLibC 也有类似的想法。不过它是基于 C 语言设计的框架，没有 C++的类、构造、析构等语法，但它通过 C 函数的包装制造出来了类似的概念。

&emsp;&emsp;举例说明，GLibC 提供了宏定义`G_DEFINE_TYPE_WITH_PRIVATE`，它基于一个结构体`struct1`注册两个类型`struct1`和`struct1Private`，同时定义了`struct1_class_init`作为构造函数的角色，`struct1_class_finalize`作为析构函数的角色。`struct1.h`文件中定义 public 方法和属性，`struct1.c`文件定义 private 方法和属性。与 C++不同的是对象的构造与析构都必须放在 c 文件里，不允许其它类型直接引用，否则破坏了 GLibC 的内存管理机制。GLibC 提供了`g_type_create_instance`函数用于构造一个类型的对象,提供了`g_type_free_instance`用于手动释放一个类型的对象。GLibC 类的命名遵循大驼峰规范，方法的命名、局部变量的命名、函数的命名都遵循 boost 规范。

&emsp;&emsp;第 1 部分列举的重要数据结构都完全遵循此命名规范。_下文为方便描述，以对象的构造函数、析构函数描述对象的重要函数以及其实现的功能_。

&emsp;&emsp;`Seat`和`Session`是一对多的关系，而`Session`是用 GLibC 做出来的虚类，实现者是`GreeterSession`。`Session`上增加了许多函数指针类型的成员变量，其中最重要的是`gboolean (*)(Session *)`类型的`start`成员变量和`void (*)(Session *)`类型的`stop`成员变量。`start`最终启动了位于`seat.c`中的`session_real_start`函数。

&emsp;&emsp;`Seat`主要有 3 种派生类型，对应的实现分别在`seat-local.c`、`seat-unity.c`、`seat-xremote.c`。`seat.c`是它们的基类型。第一个是 LightDM 默认使用的 Seat 类型。Seat 必须至少实现`setup`、`create_display_server`、`create_greeter_session`、`create_session`、`run_script`这 4 个函数，并将函数的指针赋值到 Seat 对象对应的成员变量上。

#### 3.3.2 主要的 Seat 对象以及其关联的 Session 的产生过程

- 连接`org.freedekstop.login1`服务，`signal_cb`监听此服务的信号
- `login1_service_seat_added_cb`方法监听`LOGIN1_SERVICE_SIGNAL_SEAT_ADDED`信号
- 执行`login1_service_get_seats`方法，遍历 Login1Seat 列表，对每个 Login1Seat 都调用`login1_add_seat`方法调用`display_manager_get_seat`方法判断是否已经给此 Seat 分配了显示资源。如果没有则调用`add_login1_seat`方法。如果发现此 Login1Seat 不具有显示资源的权限则调用`remove_login1_seat`方法，把它移除。
- `add_login1_seat`执行的是有显示资源却还未分配的 Login1Seat。此时产生 LightDM 管理的 Seat。随后调用`display_manager_add_seat`方法。
- `display_manager_add_seat`调用了`seat_start`方法，并触发了`DISPLAY_MANAGER_SIGNAL_SEAT_ADDED`信号。订阅此信号的是 dispmay-manager-service。它是`org.freedesktop.DisplayManager`这个系统 D-Bus 服务的实现。
- `seat_start`获取 Seat 关联的`SeatClass`对象的`setup`成员变量和`start`成员变量。这 2 个成员变量都是函数指针，`setup`指向的方法是`seat_local_setup`，此函数什么事都没做。`start`指向了`seat_local_start`函数首先读取自动登录配置。如果没有自动登录或者登录失败则启动 greeter 会话。
- `create_greeter_session`函数实现了启动 greeter 会话。会话就是 Session。此 Session 是`GreeterSession`类型，关联了`GreeterSessionClass`类型。此函数获取 seat 对象的`create_greeter_session`成员变量。特别需要注意的是这个成员变量与`seat.c`定义的`create_greeter_session`不是同一个东西，它是一个函数指针，但本身是变量，不是函数。对于 LightDM 默认的 Seat 类型，它指向了`seat_local_create_greeter_session`函数。这个方法得到了父类型的`create_greeter_session`成员，实际上调用了`seat_real_create_greeter_session`方法。接下来又调用了`greeter_session_new`方法。这个方法返回了一个`GreeterSession`类型的对象指针。这就是 Session，它的`start`成员变量也是个函数指针，指向了`greeter_session_start`方法。
- `seat`对象`create_greeter_session`成员变量指向的函数创建了`greeter_session`。此方法监听了`greeter_session`的`SESSION_SIGNAL_AUTHENTICATION_COMPLETE`信号。当用户单次登录操作完成时触发此信号。同时继续监听`GREETER_SIGNAL_CREATE_SESSION`信号和`GREETER_SIGNAL_START_SESSION`信号，分别由`greeter_create_session_cb`和`greeter_start_session_cb`函数处理。
- `seat_real_start`函数得到`greeter_session`后调用`create_display_server`方法。`create_display_server`找到 Seat 对象上的`create_display_server`成员变量。这个成员变量是个函数指针。调用`create_display_server`指向的函数得到`display_server`

### 3.4 各部分含义

- `DisplayManager`结构体类型，位于`display-manager.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`DisplayManagerPrivate*`类型，`DisplayManager`的封装，保护私有数据
- `DisplayManagerPrivate`结构体类型，位于`display-manager.c`
  - `seats`成员，`GList`类型，管理登录的用户会话列表
  - `stopping`成员，`gboolean`类型，指示是否正在停止会话
  - `stopped`成员，`gboolean`类型，指示会话是否已停止
- `DisplayManagerService`结构体类型，位于`display-manager-service.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`DisplayManagerServicePrivate*`类型，`DisplayManagerService`的封装，保护私有数据
- `DisplayManagerServicePrivate`结构体类型，位于`display-manager-service.c`
  - `manager`成员，`DisplayManager*`类型，在 D-Bus 上暴露的 DisplayManager 服务
  - `bus`成员，`GDBusConnection*`类型，Bus connected to
  - `bus_id`成员，`guint`类型，Handle for D-Bus name
  - `reg_id`成员，`guint`类型，Handle for display manager D-Bus object
  - `seat_info`成员，`GDBusNodeInfo *`类型，D-Bus interface information
  - `session_info`成员，`GDBusNodeInfo *`类型，
  - `seat_index`成员，`guint`类型，Next index to use for seat / session entries
  - `session_index`成员，`guint`类型，会话索引，也就是加到 Seat 字符串后面的数字
  - `seat_bus_entries`成员，`GHashTable*`类型，用户与 D-Bus 服务的映射，Bus entries for seats / session
  - `session_bus_entries`成员，`GHashTable *`类型，会话与 D-Bus 服务的映射
- `SharedDataManager`结构体类型，位于`shared-data-manager.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`SharedDataManagerPrivate*`类型，`SharedDataManager`的封装，保护私有数据
- `SharedDataManagerPrivate`结构体类型，位于`shared-data-manager.c`
  - `greeter_user`成员，`gchar*`类型，登录用户名
  - `greeter_gid`成员，`guint32`类型，登录用户组 ID
  - `starting_dirs`, `GHashTable *`类型，
- `Login1Service`结构体类型，位于`login1.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`SharedDataManagerPrivate*`类型，`SharedDataManager`的封装，保护私有数据
- `Login1ServicePrivate`结构体类型，位于`login1.c`
  - `connection`成员，`GDBusConnection *`类型，用于访问`org.freedesktop.login1`服务，Connection to bus service is running on
  - `connected`成员，`gboolean`类型， 指示`connection`是否已经连接
  - `seats`， `GList*`类型， 当前机器上的用户席位列表，与用户一一对应，Seats the service is reporting
  - `signal_id`成员，`guint`类型， 指示监听的信号， Handle to signal subscription
- `User`结构体类型，位于`accounts.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`UserPrivate*`类型，`User`的封装，保护私有数据
- `UserPrivate`结体体类型，位于`accounts.c`
  - `common_user`成员，`CommonUser*`类型，内部用户数据结构
- `CommonUser`结构体类型，位于`user-list.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
- `CommonUserPrivate`结构体类型，位于`user-list.c`
  - `loaded_dmrc`成员，`gboolean`类型，指示是否加载了 DMRC 文件，TRUE if have loaded the DMRC file
  - `bus`成员，`GDBusConnection*`类型，用于连接用户帐号服务并监听对方发出的信号，Bus we are listening for accounts service on
  - `path`成员，`gchar*`类型，帐号服务路径，Accounts service path
  - `changed_signal`成员，`guint`类型，帐号服务的信号，Update signal from accounts service
  - `name`成员，`gchar*`类型，用户名，Username
  - `real_name`成员，`gchar*`类型，真实名字，用于展示，可以是中文，Descriptive name for user
  - `home_directory`成员，`gchar*`类型，用户的主目录，包含文档、音乐、图像等等文件夹。Home directory of user
  - `shell`成员，`gchar*`类型，用户登录时运行的 shell 程序，Shell for user
  - `image`成员，`gchar*`类型，用户头像的路径，Image for user
  - `background`成员，`gchar*`类型，用户登录时界面背景图片路径，Background image for users
  - `has_messages`成员，`gboolean`类型，是否存在可用的消息，通常是其它用户发给这个用户的消息，TRUE if this user has messages available
  - `uid`成员，`guint64`类型，用户的 UNIX 唯一标识，UID of user
  - `gid`成员，`guint64`类型，用户直接隶属的组的 UNIX 唯一标识，GID of user
  - `language`成员，`gchar*`类型，用户选择的语言，ser chosen language
  - `layouts`成员，`gchar**`类型，User layout preferences
  - `session`成员，`gchar*`类型，默认的用户会话名称，User default session
- `CommonUserListPrivate`结构体类型，位于`user-list.c`
  - `bus` ，`GDBusConnection*`类型，Bus connection being communicated on
  - `user_added_signal`成员，`guint`类型，新增用户信号
  - `user_removed_signal`成员，`guint`类型，删除用户信号
  - `session_added_signal`成员，`guint`类型，用户登录信号
  - `session_removed_signal`成员，`guint`类型，用户注销信号，包括被管理员踢出
  - `passwd_monitor`成员，`GFileMonitor *`类型，监控用户密码文件，监听用户密码变更。
  - `have_users`成员，`gboolean`类型，当前用户列表是否存在用户
  - `users`成员，`GList *`类型，所有用户列表
  - `sessions`成员，`GList *`类型，所有登录的用户列表
- `Login1Seat`结构体类型，位于`login1.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`Login1SeatPrivate*`类型，`Login1Seat`的封装，保护私有数据
- `Login1SeatPrivate`结构体类型，位于`login1.c`
  - `connection`成员，`GDBusConnection *`类型，维护对外提供 D-Bus 的服务的连接，Connection to bus seat is running on
  - `id`成员，`gchar *`类型，LightDM 管理的用户席位标识，Seat Id
  - `path`成员，`gchar *`类型，对外提供 D-Bus 服务的路径，D-Bus path for this seat
  - `signal_id`成员，`guint`类型，Handle to signal subscription
  - `can_graphical`成员，`gboolean`类型，TRUE if can run a graphical display on this seat
  - `can_multi_session`成员，`gboolean`类型，TRUE if can do session switching
- `Session`结构体类型，位于`session.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`SessionPrivate*`类型，`Session`的封装，保护私有数据
- `SessionPrivate`结构体类型，位于`session.c`
  - `config`成员，`SessionConfig`类型，Configuration for this session
  - `display_server`成员，`DisplayServer`类型，Display server running on
  - `pid`成员，`GPid`类型，PID of child process
  - `to_child_input`成员，`int`类型，Pipes to talk to child
  - `from_child_output`成员，`int`类型，
  - `from_child_channel`成员，`GIOChannel *`类型，
  - `from_child_watch`成员，`guint`类型，
  - `child_watch`成员，`guint`类型，
  - `username`成员，`gchar *`类型，User to authenticate as
  - `is_guest`成员，`gboolean`类型，TRUE if is a guest account
  - `user`成员，`User`类型，User object that matches the current username
  - `pam_service`成员，`gchar *`类型，PAM service to use
  - `do_authenticate`成员，`gboolean`类型，TRUE if should run PAM authentication phase
  - `is_interactive`成员，`gboolean`类型，TRUE if can handle PAM prompts
  - `messages_length`成员，`int`类型，Messages being requested by PAM
  - `messages`成员，`struct pam_message *`类型，
  - `authentication_started`成员，`gboolean`类型，Authentication result from PAM
  - `authentication_complete`成员，`gboolean`类型，
  - `authentication_result`成员，`int`类型，
  - `authentication_result_string`成员，`gchar *`类型，
  - `log_filename`成员，`gchar *`类型，File to log to
  - `log_mode`成员，`LogMode`类型，
  - `tty`成员，`gchar *`类型，tty this session is running on
  - `xdisplay`成员，`gchar *`类型，X display connected to
  - `x_authority`成员，`XAuthority *`类型，
  - `x_authority_use_system_location`成员，`gboolean`类型，
  - `greeter_socket`成员，`GreeterSocket *`类型，Socket to allow greeters to connect to (if allowed)
  - `remote_host_name`成员，`gchar *`类型，Remote host this session is being controlled from
  - `console_kit_cookie`成员，`gchar *`类型，Console kit cookie
  - `login1_session_id`成员，`gchar *`类型，login1 session ID
  - `env`成员，`GList *`类型，Environment to set in child
  - `argv`成员，`gchar **`类型，Command to run in child
  - `command_run`成员，`gboolean`类型，True if have run command
  - `stopping`成员，`gboolean`类型，TRUE if stopping this session
- `SessionConfig`结构体类型，位于`session-config.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`SessionConfigPrivate*`类型，`SessionConfig`的封装，保护私有数据
- `SessionConfigPrivate`结构体类型，位于`session-config.c`
  - `session_type`成员，`gchar *`类型，Session type
  - `desktop_names`成员，`gchar **`类型，桌面环境列表，比如 XFCE、LCDE 等等。Desktop names
  - `command`成员，`gchar *`类型，目标 greeter 可执行文件路径以及参数。Command to run
  - `allow_greeter`成员，`gboolean`类型，TRUE if can run a greeter inside the session
- `DisplayServer`结构体类型，位于`display-server.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`DisplayServerPrivate*`类型，`DisplayServer`的封装，保护私有数据
- `DisplayServerPrivate`结构体类型，位于`display-server.c`
  - `is_ready`成员，`gboolean`类型，TRUE when started
  - `stopping`成员，`gboolean`类型，TRUE when being stopped
  - `stopped`成员，`gboolean`类型，TRUE when the display server has stopped
- `XAuthority`结构体类型，位于`x-authority.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`XAuthorityPrivate*`类型，`XAuthority`的封装，保护私有数据
- `XAuthorityPrivate`结构体类型，位于`x-authority.c`
  - `family`成员，`guint16`类型，Protocol family
  - `address`成员，`guint8 *`类型，Address of the X server (format dependent on family)
  - `address_length`成员，`gsize`类型，指示`address`的长度
  - `number`成员，`gchar *`类型，Display number of X server
  - `authorization_name`成员，`gchar *`类型，Authorization scheme
  - `authorization_data`成员，`guint8 *`类型，Authorization data
  - `authorization_data_length`成员，`gsize`类型，指示`authorization_data`的长度
- `Greeter`结构体类型，位于`greeter.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`GreeterPrivate*`类型，`Greeter`的封装，保护私有数据
- `GreeterPrivate`结构体类型，位于`greeter.c`
  - `pam_service`成员，`gchar *`类型，PAM service to authenticate with
  - `autologin_pam_service`成员，`gchar *`类型，
  - `read_buffer`成员，`guint8 *`类型，Buffer for data read from greeter
  - `n_read`成员，`gsize`类型，
  - `use_secure_memory`成员，`gboolean`类型，
  - `hints`成员，`GHashTable *`类型，Hints for the greeter
  - `default_session`成员，`gchar *`类型，Default session to use
  - `authentication_sequence_number`成员，`guint32`类型，Sequence number of current PAM session
  - `remote_session`成员，`gchar *`类型，Remote session name
  - `active_username`成员，`gchar *`类型，Currently selected user
  - `authentication_session`成员，`Session*`类型，PAM session being constructed by the greeter
  - `api_version`成员，`guint32`类型，API version the client can speak
  - `resettable`成员，`gboolean`类型，TRUE if a the greeter can handle a reset; else we will just kill it instead
  - `start_session`成员，`gboolean`类型，TRUE if a user has been authenticated and the session requested to start
  - `allow_guest`成员，`gboolean`类型，TRUE if can log into guest accounts
  - `guest_account_authenticated`成员，`gboolean`类型，TRUE if logging into guest session
  - `to_greeter_input`成员，`int`类型，Communication channels to communicate with
  - `from_greeter_output`成员，`int`类型，
  - `to_greeter_channel`成员，`GIOChannel *`类型，
  - `from_greeter_channel`成员，`GIOChannel *`类型，
  - `from_greeter_watch`成员，`guint`类型，
- `GreeterClass`结构体类型，位于`greeter.h`
  - `parent_class`成员，`GObjectClass`类型
  - `connected`成员，`void (*)(Greeter *)`类型，函数指针
  - `disconnected`成员，`void (*)(Greeter *)`类型，函数指针
  - `create_session`成员，`Session * (*)(Greeter *)`类型，函数指针
  - `start_session`成员，`gboolean (*)(Greeter *, SessionType, const gchar *)`类型，函数指针
- `SessionClass`结构体类型，位于`session.h`
  - `parent_class`成员，`GObjectClass`类型
  - `start`成员，`gboolean (*)(Session *)`类型，函数指针
  - `run`成员，`void (*)(Session *)`类型，函数指针
  - `stop`成员，`void (*)(Session *)`类型，函数指针
  - `create_greeter`成员，`Greeter *(*)(Session *)`类型，函数指针
  - `got_messages`成员，`void (*)(Session *)`类型，函数指针
  - `authentication_complete`成员，`void (*)(Session *session)`类型，函数指针
  - `stopped`成员，`void (*)(Session *session)`类型，函数指针
- `SeatClass`结构体类型，位于`seat.h`
  - `parent_class`成员，`GObjectClass`类型
  - `setup`成员，`void (*)(Seat *)`类型，函数指针
  - `start`成员，`gboolean (*)(Seat *)`类型，函数指针
  - `create_display_server`成员，`DisplayServer *(*) (Seat *, Session *)`类型，函数指针
  - `display_server_is_used`成员，`gboolean (*) (Seat *, DisplayServer *)`类型，函数指针
  - `create_greeter_session`成员，`GreeterSession *(*) (Seat *)`类型，函数指针
  - `create_session`成员，`Session *(*) (Seat *)`类型，函数指针
  - `set_active_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
  - `set_next_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
  - `get_active_session`成员，`Session *(*)(Seat *)`类型，函数指针
  - `run_script`成员，`void (*)(Seat *, DisplayServer *, Process *)`类型，函数指针
  - `stop`成员，`void (*)(Seat *)`类型，函数指针
  - `session_added`成员，`void (*)(Seat *, Session *)`类型，函数指针
  - `running_user_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
  - `session_removed`成员，`void (*)(Seat *, Session *)`类型，函数指针
  - `stopped`成员，`void (*)(Seat *)`类型，函数指针
- `Seat`结构体类型，位于`seat.h`
  - `parent_instance`成员，`GObject`类型，管理对象的生命周期
  - `priv`成员，`SeatPrivate*`类型，`Seat`的封装，保护私有数据
- `SeatPrivate`结构体类型，位于`seat.c`
  - `name`成员，`gchar *`类型，XDG name for this seat
  - `properties`成员，`GHashTable *`类型，Configuration for this seat
  - `supports_multi_session`成员，`gboolean`类型，TRUE if this seat can run multiple sessions at once
  - `share_display_server`成员，`gboolean`类型，TRUE if display server can be shared for sessions
  - `display_servers`成员，`GList *`类型，The display servers on this seat
  - `sessions`成员，`GList *`类型，The sessions on this seat
  - `active_session`成员，`Session *`类型，The last session set to active
  - `next_session`成员，`Session *`类型，The session belonging to the active greeter user
  - `session_to_activate`成员，`Session *`类型，The session to set active when it starts
  - `started`成员，`gboolean`类型，TRUE once we have started
  - `stopping`成员，`gboolean`类型，TRUE if stopping this seat (waiting for displays to stop)
  - `stopped`成员，`gboolean`类型，TRUE if stopped
  - `replacement_greeter`成员，`GreeterSession *`类型，The greeter to be started to replace the current one

## 4. 参考文献

- [archlinux.org](https://wiki.archlinux.org/index.php/LightDM)
- [freedesktop.org](https://www.freedesktop.org/wiki/Software/LightDM/Design/)
