<ol>
<h1><li>重要的数据结构</li></h1>

   1. #### `DisplayManager`结构体类型，位于`display-manager.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`DisplayManagerPrivate*`类型，`DisplayManager`的封装，保护私有数据

   1. ## `DisplayManagerPrivate`结构体类型，位于`display-manager.c`
      1. `seats`成员，`GList`类型，管理登录的用户会话列表
      1. `stopping`成员，`gboolean`类型，指示是否正在停止会话
      1. `stopped`成员，`gboolean`类型，指示会话是否已停止

   1. ## `DisplayManagerService`结构体类型，位于`display-manager-service.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`DisplayManagerServicePrivate*`类型，`DisplayManagerService`的封装，保护私有数据

   1. ## `DisplayManagerServicePrivate`结构体类型，位于`display-manager-service.c`
      1. `manager`成员，`DisplayManager*`类型，在D-Bus上暴露的DisplayManager服务
      1. `bus`成员，`GDBusConnection*`类型，Bus connected to
      1. `bus_id`成员，`guint`类型，Handle for D-Bus name
      1. `reg_id`成员，`guint`类型，Handle for display manager D-Bus object
      1. `seat_info`成员，`GDBusNodeInfo *`类型，D-Bus interface information
      1. `session_info`成员，`GDBusNodeInfo *`类型，
      1. `seat_index`成员，`guint`类型，Next index to use for seat / session entries
      1. `session_index`成员，`guint`类型，会话索引，也就是加到Seat字符串后面的数字
      1. `seat_bus_entries`成员，`GHashTable*`类型，用户与D-Bus服务的映射，Bus entries for seats / session
      1. `session_bus_entries`成员，`GHashTable *`类型，会话与D-Bus服务的映射

   1. ## `SharedDataManager`结构体类型，位于`shared-data-manager.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`SharedDataManagerPrivate*`类型，`SharedDataManager`的封装，保护私有数据

   1. ## `SharedDataManagerPrivate`结构体类型，位于`shared-data-manager.c`
      1. `greeter_user`成员，`gchar*`类型，登录用户名
      1. `greeter_gid`成员，`guint32`类型，登录用户组ID
      1. `starting_dirs`, `GHashTable *`类型，

   1. ## `Login1Service`结构体类型，位于`login1.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`SharedDataManagerPrivate*`类型，`SharedDataManager`的封装，保护私有数据

   1. ## `Login1ServicePrivate`结构体类型，位于`login1.c`
      1. `connection`成员，`GDBusConnection *`类型，用于访问`org.freedesktop.login1`服务，Connection to bus service is running on
      1. `connected`成员，`gboolean`类型， 指示`connection`是否已经连接
      1. `seats`， `GList*`类型， 当前机器上的用户席位列表，与用户一一对应，Seats the service is reporting
      1. `signal_id`成员，`guint`类型， 指示监听的信号， Handle to signal subscription

   1. ## `User`结构体类型，位于`accounts.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`UserPrivate*`类型，`User`的封装，保护私有数据

   1. ## `UserPrivate`结体体类型，位于`accounts.c`
      1. `common_user`成员，`CommonUser*`类型，内部用户数据结构

   1. ## `CommonUser`结构体类型，位于`user-list.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期

   1. ## `CommonUserPrivate`结构体类型，位于`user-list.c`
      1. `loaded_dmrc`成员，`gboolean`类型，指示是否加载了DMRC文件，TRUE if have loaded the DMRC file
      1. `bus`成员，`GDBusConnection*`类型，用于连接用户帐号服务并监听对方发出的信号，Bus we are listening for accounts service on
      1. `path`成员，`gchar*`类型，帐号服务路径，Accounts service path
      1. `changed_signal`成员，`guint`类型，帐号服务的信号，Update signal from accounts service
      1. `name`成员，`gchar*`类型，用户名，Username
      1. `real_name`成员，`gchar*`类型，真实名字，用于展示，可以是中文，Descriptive name for user
      1. `home_directory`成员，`gchar*`类型，用户的主目录，包含文档、音乐、图像等等文件夹。Home directory of user
      1. `shell`成员，`gchar*`类型，用户登录时运行的shell程序，Shell for user
      1. `image`成员，`gchar*`类型，用户头像的路径，Image for user
      1. `background`成员，`gchar*`类型，用户登录时界面背景图片路径，Background image for users
      1. `has_messages`成员，`gboolean`类型，是否存在可用的消息，通常是其它用户发给这个用户的消息，TRUE if this user has messages available
      1. `uid`成员，`guint64`类型，用户的UNIX唯一标识，UID of user
      1. `gid`成员，`guint64`类型，用户直接隶属的组的UNIX唯一标识，GID of user
      1. `language`成员，`gchar*`类型，用户选择的语言，ser chosen language
      1. `layouts`成员，`gchar**`类型，User layout preferences
      1. `session`成员，`gchar*`类型，默认的用户会话名称，User default session

   1. ## `CommonUserListPrivate`结构体类型，位于`user-list.c`
      1. `bus` ，`GDBusConnection*`类型，Bus connection being communicated on
      1. `user_added_signal`成员，`guint`类型，新增用户信号
      1. `user_removed_signal`成员，`guint`类型，删除用户信号
      1. `session_added_signal`成员，`guint`类型，用户登录信号
      1. `session_removed_signal`成员，`guint`类型，用户注销信号，包括被管理员踢出
      1. `passwd_monitor`成员，`GFileMonitor *`类型，监控用户密码文件，监听用户密码变更。
      1. `have_users`成员，`gboolean`类型，当前用户列表是否存在用户
      1. `users`成员，`GList *`类型，所有用户列表
      1. `sessions`成员，`GList *`类型，所有登录的用户列表

   1. ## `Login1Seat`结构体类型，位于`login1.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`Login1SeatPrivate*`类型，`Login1Seat`的封装，保护私有数据

   1. ## `Login1SeatPrivate`结构体类型，位于`login1.c`
      1. `connection`成员，`GDBusConnection *`类型，维护对外提供D-Bus的服务的连接，Connection to bus seat is running on
      1. `id`成员，`gchar *`类型，LightDM管理的用户席位标识，Seat Id
      1. `path`成员，`gchar *`类型，对外提供D-Bus服务的路径，D-Bus path for this seat
      1. `signal_id`成员，`guint`类型，Handle to signal subscription
      1. `can_graphical`成员，`gboolean`类型，TRUE if can run a graphical display on this seat
      1. `can_multi_session`成员，`gboolean`类型，TRUE if can do session switching

   1. ## `Session`结构体类型，位于`session.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`SessionPrivate*`类型，`Session`的封装，保护私有数据

   1. ## `SessionPrivate`结构体类型，位于`session.c`
      1. `config`成员，`SessionConfig`类型，Configuration for this session
      1. `display_server`成员，`DisplayServer`类型，Display server running on
      1. `pid`成员，`GPid`类型，PID of child process
      1. `to_child_input`成员，`int`类型，Pipes to talk to child
      1. `from_child_output`成员，`int`类型，
      1. `from_child_channel`成员，`GIOChannel *`类型，
      1. `from_child_watch`成员，`guint`类型，
      1. `child_watch`成员，`guint`类型，
      1. `username`成员，`gchar *`类型，User to authenticate as
      1. `is_guest`成员，`gboolean`类型，TRUE if is a guest account
      1. `user`成员，`User`类型，User object that matches the current username
      1. `pam_service`成员，`gchar *`类型，PAM service to use
      1. `do_authenticate`成员，`gboolean`类型，TRUE if should run PAM authentication phase
      1. `is_interactive`成员，`gboolean`类型，TRUE if can handle PAM prompts
      1. `messages_length`成员，`int`类型，Messages being requested by PAM
      1. `messages`成员，`struct pam_message *`类型，
      1. `authentication_started`成员，`gboolean`类型，Authentication result from PAM
      1. `authentication_complete`成员，`gboolean`类型，
      1. `authentication_result`成员，`int`类型，
      1. `authentication_result_string`成员，`gchar *`类型，
      1. `log_filename`成员，`gchar *`类型，File to log to
      1. `log_mode`成员，`LogMode`类型，
      1. `tty`成员，`gchar *`类型，tty this session is running on
      1. `xdisplay`成员，`gchar *`类型，X display connected to
      1. `x_authority`成员，`XAuthority *`类型，
      1. `x_authority_use_system_location`成员，`gboolean`类型，
      1. `greeter_socket`成员，`GreeterSocket *`类型，Socket to allow greeters to connect to (if allowed)
      1. `remote_host_name`成员，`gchar *`类型，Remote host this session is being controlled from
      1. `console_kit_cookie`成员，`gchar *`类型，Console kit cookie
      1. `login1_session_id`成员，`gchar *`类型，login1 session ID
      1. `env`成员，`GList *`类型，Environment to set in child
      1. `argv`成员，`gchar **`类型，Command to run in child
      1. `command_run`成员，`gboolean`类型，True if have run command
      1. `stopping`成员，`gboolean`类型，TRUE if stopping this session

   1. ## `SessionConfig`结构体类型，位于`session-config.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`SessionConfigPrivate*`类型，`SessionConfig`的封装，保护私有数据

   1. ## `SessionConfigPrivate`结构体类型，位于`session-config.c`
      1. `session_type`成员，`gchar *`类型，Session type
      1. `desktop_names`成员，`gchar **`类型，桌面环境列表，比如XFCE、LCDE等等。Desktop names
      1. `command`成员，`gchar *`类型，目标greeter可执行文件路径以及参数。Command to run
      1. `allow_greeter`成员，`gboolean`类型，TRUE if can run a greeter inside the session

   1. ## `DisplayServer`结构体类型，位于`display-server.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`DisplayServerPrivate*`类型，`DisplayServer`的封装，保护私有数据

   1. ## `DisplayServerPrivate`结构体类型，位于`display-server.c`
      1. `is_ready`成员，`gboolean`类型，TRUE when started
      1. `stopping`成员，`gboolean`类型，TRUE when being stopped
      1. `stopped`成员，`gboolean`类型，TRUE when the display server has stopped

   1. ## `XAuthority`结构体类型，位于`x-authority.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`XAuthorityPrivate*`类型，`XAuthority`的封装，保护私有数据

   1. ## `XAuthorityPrivate`结构体类型，位于`x-authority.c`
      1. `family`成员，`guint16`类型，Protocol family
      1. `address`成员，`guint8 *`类型，Address of the X server (format dependent on family)
      1. `address_length`成员，`gsize`类型，指示`address`的长度
      1. `number`成员，`gchar *`类型，Display number of X server
      1. `authorization_name`成员，`gchar *`类型，Authorization scheme
      1. `authorization_data`成员，`guint8 *`类型，Authorization data
      1. `authorization_data_length`成员，`gsize`类型，指示`authorization_data`的长度

   1. ## `Greeter`结构体类型，位于`greeter.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`GreeterPrivate*`类型，`Greeter`的封装，保护私有数据

   1. ## `GreeterPrivate`结构体类型，位于`greeter.c`
      1. `pam_service`成员，`gchar *`类型，PAM service to authenticate with
      1. `autologin_pam_service`成员，`gchar *`类型，
      1. `read_buffer`成员，`guint8 *`类型，Buffer for data read from greeter
      1. `n_read`成员，`gsize`类型，
      1. `use_secure_memory`成员，`gboolean`类型，
      1. `hints`成员，`GHashTable *`类型，Hints for the greeter
      1. `default_session`成员，`gchar *`类型，Default session to use
      1. `authentication_sequence_number`成员，`guint32`类型，Sequence number of current PAM session
      1. `remote_session`成员，`gchar *`类型，Remote session name
      1. `active_username`成员，`gchar *`类型，Currently selected user
      1. `authentication_session`成员，`Session*`类型，PAM session being constructed by the greeter
      1. `api_version`成员，`guint32`类型，API version the client can speak
      1. `resettable`成员，`gboolean`类型，TRUE if a the greeter can handle a reset; else we will just kill it instead
      1. `start_session`成员，`gboolean`类型，TRUE if a user has been authenticated and the session requested to start
      1. `allow_guest`成员，`gboolean`类型，TRUE if can log into guest accounts
      1. `guest_account_authenticated`成员，`gboolean`类型，TRUE if logging into guest session
      1. `to_greeter_input`成员，`int`类型，Communication channels to communicate with
      1. `from_greeter_output`成员，`int`类型，
      1. `to_greeter_channel`成员，`GIOChannel *`类型，
      1. `from_greeter_channel`成员，`GIOChannel *`类型，
      1. `from_greeter_watch`成员，`guint`类型，

   1. ## `GreeterClass`结构体类型，位于`greeter.h`
      1. `parent_class`成员，`GObjectClass`类型
      1. `connected`成员，`void (*)(Greeter *)`类型，函数指针
      1. `disconnected`成员，`void (*)(Greeter *)`类型，函数指针
      1. `create_session`成员，`Session * (*)(Greeter *)`类型，函数指针
      1. `start_session`成员，`gboolean (*)(Greeter *, SessionType, const gchar *)`类型，函数指针

   1. ## `SessionClass`结构体类型，位于`session.h`
      1. `parent_class`成员，`GObjectClass`类型
      1. `start`成员，`gboolean (*)(Session *)`类型，函数指针
      1. `run`成员，`void (*)(Session *)`类型，函数指针
      1. `stop`成员，`void (*)(Session *)`类型，函数指针
      1. `create_greeter`成员，`Greeter *(*)(Session *)`类型，函数指针
      1. `got_messages`成员，`void (*)(Session *)`类型，函数指针
      1. `authentication_complete`成员，`void (*)(Session *session)`类型，函数指针
      1. `stopped`成员，`void (*)(Session *session)`类型，函数指针

   1. ## `SeatClass`结构体类型，位于`seat.h`
      1. `parent_class`成员，`GObjectClass`类型
      1. `setup`成员，`void (*)(Seat *)`类型，函数指针
      1. `start`成员，`gboolean (*)(Seat *)`类型，函数指针
      1. `create_display_server`成员，`DisplayServer *(*) (Seat *, Session *)`类型，函数指针
      1. `display_server_is_used`成员，`gboolean (*) (Seat *, DisplayServer *)`类型，函数指针
      1. `create_greeter_session`成员，`GreeterSession *(*) (Seat *)`类型，函数指针
      1. `create_session`成员，`Session *(*) (Seat *)`类型，函数指针
      1. `set_active_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
      1. `set_next_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
      1. `get_active_session`成员，`Session *(*)(Seat *)`类型，函数指针
      1. `run_script`成员，`void (*)(Seat *, DisplayServer *, Process *)`类型，函数指针
      1. `stop`成员，`void (*)(Seat *)`类型，函数指针
      1. `session_added`成员，`void (*)(Seat *, Session *)`类型，函数指针
      1. `running_user_session`成员，`void (*)(Seat *, Session *)`类型，函数指针
      1. `session_removed`成员，`void (*)(Seat *, Session *)`类型，函数指针
      1. `stopped`成员，`void (*)(Seat *)`类型，函数指针

   1. ## `Seat`结构体类型，位于`seat.h`
      1. `parent_instance`成员，`GObject`类型，管理对象的生命周期
      1. `priv`成员，`SeatPrivate*`类型，`Seat`的封装，保护私有数据

   1. ## `SeatPrivate`结构体类型，位于`seat.c`
      1. `name`成员，`gchar *`类型，XDG name for this seat
      1. `properties`成员，`GHashTable *`类型，Configuration for this seat
      1. `supports_multi_session`成员，`gboolean`类型，TRUE if this seat can run multiple sessions at once
      1. `share_display_server`成员，`gboolean`类型，TRUE if display server can be shared for sessions
      1. `display_servers`成员，`GList *`类型，The display servers on this seat
      1. `sessions`成员，`GList *`类型，The sessions on this seat
      1. `active_session`成员，`Session *`类型，The last session set to active
      1. `next_session`成员，`Session *`类型，The session belonging to the active greeter user
      1. `session_to_activate`成员，`Session *`类型，The session to set active when it starts
      1. `started`成员，`gboolean`类型，TRUE once we have started
      1. `stopping`成员，`gboolean`类型，TRUE if stopping this seat (waiting for displays to stop)
      1. `stopped`成员，`gboolean`类型，TRUE if stopped
      1. `replacement_greeter`成员，`GreeterSession *`类型，The greeter to be started to replace the current one


<h1><li> LightDM启动过程中与用户管理有关的初始化</li></h1>

   1. 读取配置`/etc/lightdm/lightdm.conf`并初始化`lightdm.conf`没有赋值的配置节。这里重点关注与登录有关的配置
      1. `start-default-seat`默认值`true`
      1. `greeter-user`默认值`lightdm`
      1. `sessions-directory`默认值`/usr/share/lightdm/sessions:/usr/share/xsessions:/usr/share/wayland-sessions`
      1. `remote-sessions-directory`默认值`/usr/share/lightdm/remote-sessions`
      1. `greeters-directory`默认值`$XDG_DATA_DIRS/lightdm/greeters:$XDG_DATA_DIRS/xgreeters`
      1. `pam-service`默认值`lightdm`
      1. `pam-autologin-service`默认值`lightdm-autologin`
      1. `pam-greeter-service`默认值`lightdm-greeter`。
      1. `dbus-service`默认值`true`
   1. `display_manager_new`函数初始化`display_manager`，此函数的主要作用是在C开发环境模拟单例模式
   1. `display_manager_stopped_cb`监听DisplayManager的`DISPLAY_MANAGER_SIGNAL_STOPPED`信号。此信号为停止DisplayManager的信息。监听函数调用`g_main_loop_quit`函数中断主程序`loop`循环，将程序正常退出。
   1. `display_manager_seat_removed_cb`监听`DISPLAY_MANAGER_SIGNAL_SEAT_REMOVED`信号。此信号由用户注销引发。监听函数要为下一次登录作准备。如果发生异常（通用由用户注销异常引发），它会停止`display_manager`的运行，间接引发程序退出。
   1. 读取`lightdm.conf`配置节`LightDM`的配置`dbus-service`
      1. 如果为`true`
         1. 通过`display_manager_service_new`函数创建`display_manager_service`服务。此函数的主要作用是在C开发环境模拟单例模式
         1. `service_add_xlocal_seat_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_ADD_XLOCAL_SEAT`信号，此信号由用户登录成功触发，此监听函数准备专属于此用户的D-Bus服务。
         1. `service_ready_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_READY`信号。此信号在专属于此用户的的D-Bus服务准备就绪后触发
         1. `service_name_lost_cb`函数监听`DISPLAY_MANAGER_SERVICE_SIGNAL_NAME_LOST`信号。此监听函数会在不正常停止`display_manager`的运行的情况下直接将程序退出，而且没有输出日志，需要关注。
         1. `display_manager_service_start`启动DisplayManager的D-Bus服务。如果启动身份是root则注册到系统Bus，否则注册到用户Bus。
      1. 如果为`false`
         1. 执行`start_display_manager`函数。此函数会检测用户是否启用了`XDMCPServer`服务、`VNCServer`服务。如果启用了就会把这些服务启动。
   1. 执行`shared_data_manager_start`函数。此函数会遍历`home`目录，监听子目录的删除事件。如果发生删除事件就引发`USER_LIST_SIGNAL_USER_REMOVED`信号，执行`user_removed_cb`监听函数。监听函数进一步执行删除用户操作。
   1. 执行`login1_service_connect`函数。此函数获取`Login1Service`的单例模式，调用`g_bus_get_sync`连接系统D-Bus，连上`org.freedesktop.login1`，立即请求`ListSeats`服务，返回结果保存到用户列表。
      1. 如果为`true`
         1. 读取配置节`LightDM`下`start-default-seat`配置。此配置指示默认登录的用户。
            1. 如果读取成功
               1. `login1_service_seat_added_cb`函数监听`LOGIN1_SERVICE_SIGNAL_SEAT_ADDED`信号，此信号由用户登录成功触发
               1. `login1_service_seat_removed_cb`函数监听`LOGIN1_SERVICE_SIGNAL_SEAT_REMOVED`信号，此信号由用户注销触发。
            1. 如果读取失败
               1. 不做任何事情。
      1. 如果为`false`
         1. 读取配置节`LightDM`下`start-default-seat`配置。
            1. 如果读取成功
               1. 读取配置节`Seat:*`下`type`配置，保存到`types`
               1. 遍历`types`，保存到`type`。调用`create_seat`，保存到`seat`。如果`seat`不为空则停止遍历。
               1. 如果`seat`不为空则执行`display_manager_add_seat`函数，注册`seat`提供登录服务
                  1. 如果注册`seat`失败就直接退出程序。此过程没有输出日志，需要关注。
            1. 如果读取失败
               1. 不做任何事情。
   1. 执行`g_main_loop_run`，此函数的主要作用是内存驻留。
   1. 清理用户列表，断开D-Bus连接
   1. 释放`display_manager_service`和`display_manager`的内存
   1. 退出。


<h1><li> LightDM管理的Seat与系统的PAM的关联 </li></h1>

   1. ### LightDM的核心类型：`Seat`和`Session`

      `Seat`和`Session`都是一个派生自[`GObject`](https://developer.gnome.org/gobject/stable/)类型的对象。`GObject`是GLibC用C语言模拟的类，它在C语言上实现了OOP。它是GLibC运行时下对象的基类型，与Qt的`QObject`在设计思想有许多相似之处。比如在对象的内存管理方面都有一个内存池的设计、对象的引用也有强引用和弱引用之分，对象或模块之间的通信都有一个信号槽的设计、在对象的存储结构方面都提供了一个Variant类型的设计用于动态增加、修改、删除对象的属性等等。举例说明，Qt支持用户把不想管理内存的对象可以通过继承QObject交给Qt运行时管理，使用的时候只管new一个出来，不必使用智能指针包装。

      GLibC也有类似的想法。不过它是基于C语言设计的框架，没有C++的类、构造、析构等语法，但它通过C函数的包装制造出来了类似的概念。举例说明，GLibC提供了宏定义`G_DEFINE_TYPE_WITH_PRIVATE`，它基于一个结构体`struct1`注册两个类型`struct1`和`struct1Private`，同时定义了`struct1_class_init`作为构造函数的角色，`struct1_class_finalize`作为析构函数的角色。`struct1.h`文件中定义public方法和属性，`struct1.c`文件定义private方法和属性。与C++不同的是对象的构造与析构都必须放在c文件里，不允许其它类型直接引用，否则破坏了GLibC的内存管理机制。GLibC提供了`g_type_create_instance`函数用于构造一个类型的对象,提供了`g_type_free_instance`用于手动释放一个类型的对象。

      GLibC类的命名遵循大驼峰规范，方法的命名、局部变量的命名、函数的命名都遵循boost规范。第1部分列举的重要的数据结构都完全遵循此命名规范。*下文为方便描述，以对象的构造函数、析构函数描述对象的重要函数以及其实现的功能*。

      `Seat`和`Session`是一对多的关系，而`Session`是一用GLibC做出来的虚类，实现者是`GreeterSession`。`Session`上增加了许多函数指针类型的成员变量，其中最重要的是`gboolean (*)(Session *)`类型的`start`成员变量和`void (*)(Session *)`类型的`stop`成员变量。`start`最终启动了位于`seat.c`中的`session_real_start`函数

      `Seat`主要有3种派生类型，对应的实现分别在`seat-local.c`、`seat-unity.c`、`seat-xremote.c`。`seat.c`是它们的基类型。第一个是LightDM默认使用的Seat类型。Seat必须至少实现`setup`、`create_display_server`、`create_greeter_session`、`create_session`、`run_script`这4个函数，并将函数的指针赋值到Seat对象对应的成员变量上。

   2. ###  主要的Seat对象以及其关联的Session的产生过程
      1. 连接`org.freedekstop.login1`服务，`signal_cb`监听此服务的信号
      2. `login1_service_seat_added_cb`方法监听`LOGIN1_SERVICE_SIGNAL_SEAT_ADDED`信号
      3. 执行`login1_service_get_seats`方法，遍历Login1Seat列表，对每个Login1Seat都调用`login1_add_seat`方法调用`display_manager_get_seat`方法判断是否已经给此Seat分配了显示资源。如果没有则调用`add_login1_seat`方法。如果发现此Login1Seat不具有显示资源的权限则调用`remove_login1_seat`方法，把它移除。
      4. `add_login1_seat`执行的是有显示资源却还未分配的Login1Seat。此时产生LightDM管理的Seat。随后调用`display_manager_add_seat`方法。
      5. `display_manager_add_seat`调用了`seat_start`方法，并触发了`DISPLAY_MANAGER_SIGNAL_SEAT_ADDED`信号。订阅此信号的是dispmay-manager-service。它是`org.freedesktop.DisplayManager`这个系统D-Bus服务的实现。
      6. `seat_start`获取Seat关联的`SeatClass`对象的`setup`成员变量和`start`成员变量。这2个成员变量都是函数指针，`setup`指向的方法是`seat_local_setup`，此函数什么事都没做。`start`指向了`seat_local_start`函数首先读取自动登录配置。如果没有自动登录或者登录失败则启动greeter会话。
      7. `create_greeter_session`函数实现了启动greeter会话。会话就是Session。此Session是`GreeterSession`类型，关联了`GreeterSessionClass`类型。此函数获取seat对象的`create_greeter_session`成员变量。特别需要注意的是这个成员变量与`seat.c`定义的`create_greeter_session`不是同一个东西，它是一个函数指针，但本身是变量，不是函数。对于LightDM默认的Seat类型，它指向了`seat_local_create_greeter_session`函数。这个方法得到了父类型的`create_greeter_session`成员，实际上调用了`seat_real_create_greeter_session`方法。接下来又调用了`greeter_session_new`方法。这个方法返回了一个`GreeterSession`类型的对象指针。这就是Session，它的`start`成员变量也是个函数指针，指向了`greeter_session_start`方法。
      8. `seat`对象`create_greeter_session`成员变量指向的函数创建了`greeter_session`。此方法监听了`greeter_session`的`SESSION_SIGNAL_AUTHENTICATION_COMPLETE`信号。当用户单次登录操作完成时触发此信号。同时继续监听`GREETER_SIGNAL_CREATE_SESSION`信号和`GREETER_SIGNAL_START_SESSION`信号，分别由`greeter_create_session_cb`和`greeter_start_session_cb`函数处理。
      9. `seat_real_start`函数得到`greeter_session`后调用`create_display_server`方法。`create_display_server`找到Seat对象上的`create_display_server`成员变量。这个成员变量是个函数指针。调用`create_display_server`指向的函数得到`display_server`

   3. ## PAM验证过程
      1. 当`greeter_session`启动后

   4. ## 方法调用先后顺序
<svg width="45cm" height="55cm" viewBox="-2641 -450 1785 2091" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs/>
  <g id="背景">
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2620" y="980" width="540" height="280" rx="0" ry="0"/>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2000" y="-400" width="1033.91" height="945.533" rx="0" ry="0"/>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1280" y="-214.468" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1148" y="-171.618">
        <tspan x="-1148" y="-171.618">create_greeter_session</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1663.19" y="37.5238" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1531.19" y="80.3738">
        <tspan x="-1531.19" y="80.3738">switch_to_greeter_from_failed_session</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1399.19,73.5238 -1340,73.5238 -1340,-178.468 -1289.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,-178.468 -1292.24,-173.468 -1289.74,-178.468 -1292.24,-183.468 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1660" y="165.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1528" y="208.382">
        <tspan x="-1528" y="208.382">seat_switch_to_greeter</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1396,201.532 -1340,201.532 -1340,-178.468 -1289.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,-178.468 -1292.24,-173.468 -1289.74,-178.468 -1292.24,-183.468 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1663.19" y="-354.828" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1531.19" y="-311.978">
        <tspan x="-1531.19" y="-311.978">seat_lock</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1660" y="-214.468" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1528" y="-171.618">
        <tspan x="-1528" y="-171.618">seat_real_start</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1396,-178.468 -1338,-178.468 -1338,-178.468 -1289.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,-178.468 -1292.24,-173.468 -1289.74,-178.468 -1292.24,-183.468 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1976" y="37.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1844" y="80.382">
        <tspan x="-1844" y="80.382">seat_class_init</tspan>
      </text>
    </g>
    <g>
      <path style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" fill-rule="evenodd" d="M -1880 -74.468 L -1832.1,-74.468 L -1832.1,-28.868 C -1841.68,-36.468 -1846.47,-36.468 -1856.05,-28.868 C -1865.63,-21.268 -1870.42,-21.268 -1880,-28.868 L -1880,-74.468z"/>
      <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1856.05" y="-56.268">
        <tspan x="-1856.05" y="-56.268">Seat </tspan>
        <tspan x="-1856.05" y="-40.268">start</tspan>
      </text>
    </g>
    <g>
      <line style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" x1="-1848.35" y1="36.5257" x2="-1854.91" y2="-19.1987"/>
      <polygon style="fill: #ff0000; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" fill-rule="evenodd" points="-1855.79,-26.6473 -1849.65,-17.3001 -1854.91,-19.1987 -1859.59,-16.1314 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1980" y="-214.468" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1848" y="-171.618">
        <tspan x="-1848" y="-171.618">seat_start</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1399.19,-318.828 -1339.59,-318.828 -1339.59,-178.468 -1289.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,-178.468 -1292.24,-173.468 -1289.74,-178.468 -1292.24,-183.468 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1280" y="285.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1148" y="328.382">
        <tspan x="-1148" y="328.382">start_session</tspan>
      </text>
    </g>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-1720" y="1000" width="776.55" height="640" rx="0" ry="0"/>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1720" y="1000">
      <tspan x="-1720" y="1000">session.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1250" y="1480" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1118" y="1522.85">
        <tspan x="-1118" y="1522.85">session_start</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1280" y="405.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1148" y="448.382">
        <tspan x="-1148" y="448.382">seat_switch_to_user</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1016,321.532 -880,321.532 -880,1516 -976.264,1516 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-983.764,1516 -973.764,1511 -976.264,1516 -973.764,1521 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1016,441.532 -880,441.532 -880,1516 -976.264,1516 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-983.764,1516 -973.764,1511 -976.264,1516 -973.764,1521 "/>
    </g>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2000" y="-400">
      <tspan x="-2000" y="-400">seat.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1660" y="405.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1528" y="448.382">
        <tspan x="-1528" y="448.382">display_server_ready_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1396,441.532 -1300,441.532 -1300,321.532 -1289.74,321.532 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,321.532 -1292.24,326.532 -1289.74,321.532 -1292.24,316.532 "/>
    </g>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2620" y="320" width="380" height="620" rx="0" ry="0"/>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2620" y="320">
      <tspan x="-2620" y="320">display-manager.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="360" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="402.85">
        <tspan x="-2428" y="402.85">display_manager_add_seat</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,396 -2296,396 -2080,396 -2080,-178.468 -1989.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1982.24,-178.468 -1992.24,-173.468 -1989.74,-178.468 -1992.24,-183.468 "/>
    </g>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2620" y="980">
      <tspan x="-2620" y="980">display-manager-service.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="1000" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="1042.85">
        <tspan x="-2428" y="1042.85">seat_added_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,396 -2220,396 -2220,1036 -2286.26,1036 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2293.76,1036 -2283.76,1031 -2286.26,1036 -2283.76,1041 "/>
    </g>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2620" y="-420" width="380" height="660" rx="0" ry="0"/>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2620" y="-420">
      <tspan x="-2620" y="-420">lightdm.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="-380" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="-337.15">
        <tspan x="-2428" y="-337.15">main</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,-344 -2160,-344 -2160,280 -2581,280 -2581,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="-280" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="-237.15">
        <tspan x="-2428" y="-237.15">add_login1_seat</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="-180" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="-137.15">
        <tspan x="-2428" y="-137.15">vnc_connection_cb</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="-80" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="-37.15">
        <tspan x="-2428" y="-37.15">xdmcp_session_cb</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="20" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="62.85">
        <tspan x="-2428" y="62.85">display_manager_seat_removed_cb</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2560" y="120" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2428" y="162.85">
        <tspan x="-2428" y="162.85">service_add_xlocal_seat_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,-244 -2160,-244 -2160,280 -2580,280 -2580,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,-144 -2160,-144 -2160,280 -2580,280 -2580,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,-44 -2296,-44 -2160,-44 -2160,280 -2580,280 -2580,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,56 -2160,56 -2160,280 -2580,280 -2580,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-2296,156 -2160,156 -2160,280 -2580,280 -2580,396 -2569.74,396 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2562.24,396 -2572.24,401 -2569.74,396 -2572.24,391 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1716,-178.468 -1688,-178.468 -1688,-178.468 -1669.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1662.24,-178.468 -1672.24,-173.468 -1669.74,-178.468 -1672.24,-183.468 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1396" y="-196.468">
      <tspan x="-1396" y="-196.468">auto logon</tspan>
    </text>
    <g>
      <path style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" d="M -1219.7 -335.194 L -1075.55,-335.194 L -1075.55,-289.594 C -1104.38,-297.194 -1118.8,-297.194 -1147.63,-289.594 C -1176.46,-281.994 -1190.87,-281.994 -1219.7,-289.594 L -1219.7,-335.194z"/>
      <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1147.63" y="-316.994">
        <tspan x="-1147.63" y="-316.994">SeatClass</tspan>
        <tspan x="-1147.63" y="-300.994">create_greeter_session</tspan>
      </text>
    </g>
    <line style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" x1="-1147.63" y1="-289.594" x2="-1148" y2="-214.468"/>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1279.7" y="-75.1936" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1147.7" y="-32.3436">
        <tspan x="-1147.7" y="-32.3436">session_authentication_complete_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1148,-142.468 -1148,-108.831 -1147.7,-108.831 -1147.7,-84.9297 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1147.7,-77.4297 -1152.7,-87.4297 -1147.7,-84.9297 -1142.7,-87.4297 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1147.85" y="-108.831">
      <tspan x="-1147.85" y="-108.831">SESSION_SIGNAL_AUTHENTICATION_COMPLETE</tspan>
    </text>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1015.7" y="-39.1936">
      <tspan x="-1015.7" y="-39.1936">logon</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1279.7" y="44.8064" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1147.7" y="87.6564">
        <tspan x="-1147.7" y="87.6564">find_user_session</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1147.7,-3.1936 -1147.7,20.8064 -1147.7,20.8064 -1147.7,35.0703 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1147.7,42.5703 -1152.7,32.5703 -1147.7,35.0703 -1142.7,32.5703 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1980" y="225.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1848" y="268.382">
        <tspan x="-1848" y="268.382">create_display_server</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1848,297.532 -1848,471.674 -1663.88,471.674 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1656.38,471.674 -1666.38,476.674 -1663.88,471.674 -1666.38,466.674 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1848" y="384.604">
      <tspan x="-1848" y="384.604">DISPLAY_SERVER_SIGNAL_READY</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1240" y="1040" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1108" y="1082.85">
        <tspan x="-1108" y="1082.85">session_real_start</tspan>
      </text>
    </g>
    <g>
      <path style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" d="M -1143.9 1339.55 L -1092.1,1339.55 L -1092.1,1404.35 C -1102.46,1393.55 -1107.64,1393.55 -1118,1404.35 C -1128.36,1415.15 -1133.54,1415.15 -1143.9,1404.35 L -1143.9,1339.55z"/>
      <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1118" y="1357.75">
        <tspan x="-1118" y="1357.75">Session</tspan>
        <tspan x="-1118" y="1373.75">start</tspan>
        <tspan x="-1118" y="1389.75">run</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1660" y="1480" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1528" y="1522.85">
        <tspan x="-1528" y="1522.85">session_class_init</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" points="-1118,1470.26 -1118,1442.18 -1118,1442.18 -1118,1404.35 "/>
      <polygon style="fill: #ff0000; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" fill-rule="evenodd" points="-1118,1477.76 -1123,1467.76 -1118,1470.26 -1113,1467.76 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1250" y="1200" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1118" y="1242.85">
        <tspan x="-1118" y="1242.85">session_run</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1250,1516 -1320,1516 -1320,1106.14 -1243.88,1106.14 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1236.38,1106.14 -1246.38,1111.14 -1243.88,1106.14 -1246.38,1101.14 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1640" y="1200" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1508" y="1242.85">
        <tspan x="-1508" y="1242.85">session_real_run</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1250,1236 -1313,1236 -1313,1236 -1366.26,1236 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1373.76,1236 -1363.76,1231 -1366.26,1236 -1363.76,1241 "/>
    </g>
    <g>
      <line style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" x1="-1856.05" y1="-74.468" x2="-1849.14" y2="-132.799"/>
      <polygon style="fill: #ff0000; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" fill-rule="evenodd" points="-1848.26,-140.247 -1844.47,-129.729 -1849.14,-132.799 -1854.4,-130.905 "/>
    </g>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2000" y="600" width="1033.91" height="320" rx="0" ry="0"/>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2000" y="600">
      <tspan x="-2000" y="600">greeter.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1272.29" y="640" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1140.29" y="682.85">
        <tspan x="-1140.29" y="682.85">handle_authenticate</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1273.08" y="780" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1141.08" y="822.85">
        <tspan x="-1141.08" y="822.85">handle_authenticate_remote</tspan>
      </text>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1640" y="640" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1508" y="682.85">
        <tspan x="-1508" y="682.85">read_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1376,676 -1324.15,676 -1324.15,676 -1282.03,676 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1274.53,676 -1284.53,681 -1282.03,676 -1284.53,671 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1980" y="640" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1848" y="682.85">
        <tspan x="-1848" y="682.85">greeter_set_file_descriptors</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1716,676 -1678,676 -1678,676 -1649.74,676 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1642.24,676 -1652.24,681 -1649.74,676 -1652.24,671 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1483.04" y="760">
      <tspan x="-1483.04" y="760"></tspan>
    </text>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1716" y="694">
      <tspan x="-1716" y="694">GIO</tspan>
    </text>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1008.29,676 -1008.29,676 -880,676 -880,1516 -975.29,1516 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-982.79,1516 -972.79,1511 -975.29,1516 -972.79,1521 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1009.08,816 -1009.08,816 -880,816 -880,1516 -976.264,1516 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-983.764,1516 -973.764,1511 -976.264,1516 -973.764,1521 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1280" y="165.532" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1148" y="208.382">
        <tspan x="-1148" y="208.382">run_session</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1016,201.532 -1016,200 -860,200 -860,1236 -976.264,1236 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-983.764,1236 -973.764,1231 -976.264,1236 -973.764,1241 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1396,423.532 -1310,423.532 -1310,219.532 -1289.74,219.532 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,219.532 -1292.24,224.532 -1289.74,219.532 -1292.24,214.532 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1401.86" y="411.39">
      <tspan x="-1401.86" y="411.39">logon</tspan>
    </text>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1396" y="459.532">
      <tspan x="-1396" y="459.532">login</tspan>
    </text>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1147.7" y="8.8064">
      <tspan x="-1147.7" y="8.8064">repeat login</tspan>
    </text>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1015.7,-21.1936 -994.702,-21.1936 -994.702,145.532 -1301,145.532 -1301,201.532 -1289.74,201.532 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,201.532 -1292.24,206.532 -1289.74,201.532 -1292.24,196.532 "/>
    </g>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1643.45" y="1040" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1511.45" y="1082.85">
        <tspan x="-1511.45" y="1082.85">from_child_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1240,1076 -1309.72,1076 -1309.72,1076 -1369.71,1076 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1377.21,1076 -1367.21,1071 -1369.71,1076 -1367.21,1081 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1309.72" y="1076">
      <tspan x="-1309.72" y="1076">GIO</tspan>
    </text>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1385.31,1045.86 -1320,1045.86 -1320,-39.1936 -1289.44,-39.1936 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1281.94,-39.1936 -1291.94,-34.1936 -1289.44,-39.1936 -1291.94,-44.1936 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1511.45" y="1132">
      <tspan x="-1511.45" y="1132">session-child emit</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-1676.75" y="285.532" width="297.5" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-1528" y="328.382">
        <tspan x="-1528" y="328.382">seat_lockswitch_authentication_complete_cb</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" points="-1379.25,321.532 -1340,321.532 -1340,-178.468 -1289.74,-178.468 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-1282.24,-178.468 -1292.24,-173.468 -1289.74,-178.468 -1292.24,-183.468 "/>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" points="-1528,1480 -1528,1371.95 -1153.64,1371.95 "/>
      <polygon style="fill: #ff0000; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" fill-rule="evenodd" points="-1146.14,1371.95 -1156.14,1376.95 -1153.64,1371.95 -1156.14,1366.95 "/>
    </g>
    <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e5e5e5" x="-2640" y="1360" width="776.55" height="280" rx="0" ry="0"/>
    <text font-size="25.2194" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2640" y="1360">
      <tspan x="-2640" y="1360">session-child.c</tspan>
    </text>
    <g>
      <rect style="fill: #ffffff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #e6e6fa" x="-2580" y="1404.63" width="264" height="72" rx="20" ry="20"/>
      <text font-size="12.8" style="fill: #000000; fill-opacity: 1; stroke: none;text-anchor:middle;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2448" y="1447.48">
        <tspan x="-2448" y="1447.48">session_child_run</tspan>
      </text>
    </g>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke-dasharray: 4; stroke: #1e90ff" points="-976,1076 -940,1076 -940,1440 -2040,1440 -2040,1440.63 -2306.26,1440.63 "/>
      <polygon style="fill: #1e90ff; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #1e90ff" fill-rule="evenodd" points="-2313.76,1440.63 -2303.76,1435.63 -2306.26,1440.63 -2303.76,1445.63 "/>
    </g>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-976" y="1094">
      <tspan x="-976" y="1094">pipe</tspan>
    </text>
    <text font-size="12.8" style="fill: #1e90ff; fill-opacity: 1; stroke: none;text-anchor:start;font-family:sans-serif;font-style:normal;font-weight:normal" x="-2316" y="1458.63">
      <tspan x="-2316" y="1458.63">from main function</tspan>
      <tspan x="-2316" y="1474.63">--session-child</tspan>
    </text>
    <g>
      <polyline style="fill: none; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" points="-1118,1339.55 -1118,1296 -1118,1296 -1118,1281.74 "/>
      <polygon style="fill: #ff0000; fill-opacity: 1; stroke-opacity: 1; stroke-width: 2; stroke: #ff0000" fill-rule="evenodd" points="-1118,1274.24 -1113,1284.24 -1118,1281.74 -1123,1284.24 "/>
    </g>
  </g>
</svg>



<h1><li>Markdown嵌套svg以及UML软件dia对svg的支持</li></h1>

   1. ## SVG参考文档
      1. [所有的SVG元素属性API](https://www.runoob.com/svg/svg-reference.html)
      1. [W3School教程](https://www.w3school.com.cn/svg/index.asp)
      1. [SVG代码在线预览](https://www.bejson.com/ui/svg_editor/)
      1. [其它图像格式与SVG互转在线工具](https://www.aconvert.com/cn/format/svg/)
      1. [在线设计工具1](https://c.runoob.com/more/svgeditor/)
      1. [在线设计工具2](http://www.86y.org/demo/svg/)

   1. ## UML工具Dia

</ol>
