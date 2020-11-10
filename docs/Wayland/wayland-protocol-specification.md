# 附录 A：Wayland 协议规范

- [wl_display - core global object](#wl_display---core-global-object)
  - [wl_display 提供的请求](#wl_display-提供的请求)
    - [wl_display::sync - asynchronous roundtrip](#wl_displaysync---asynchronous-roundtrip)
    - [wl_display::get_registry - get global registry object](#wl_displayget_registry---get-global-registry-object)
  - [wl_display 提供的事件](#wl_display-提供的事件)
    - [wl_display::error - fatal error event](#wl_displayerror---fatal-error-event)
    - [wl_display::delete_id - acknowledge object ID deletion](#wl_displaydelete_id---acknowledge-object-id-deletion)
  - [wl_display 提供的枚举](#wl_display-提供的枚举)
    - [wl_display::error - global error values](#wl_displayerror---global-error-values)
- [wl_registry - global registry object](#wl_registry---global-registry-object)
- [wl_callback - callback object](#wl_callback---callback-object)
- [wl_compositor - the compositor singleton](#wl_compositor---the-compositor-singleton)
- [wl_shm_pool - a shared memory pool](#wl_shm_pool---a-shared-memory-pool)
- [wl_shm - shared memory support](#wl_shm---shared-memory-support)
- [wl_buffer - content for a wl_surface](#wl_buffer---content-for-a-wl_surface)
- [wl_data_offer - offer to transfer data](#wl_data_offer---offer-to-transfer-data)
- [wl_data_source - offer to transfer data](#wl_data_source---offer-to-transfer-data)
- [wl_data_device - data transfer device](#wl_data_device---data-transfer-device)
- [wl_data_device_manager - data transfer interface](#wl_data_device_manager---data-transfer-interface)
- [wl_shell - create desktop-style surfaces](#wl_shell---create-desktop-style-surfaces)
- [wl_shell_surface - desktop-style metadata interface](#wl_shell_surface---desktop-style-metadata-interface)
- [wl_surface - an onscreen surface](#wl_surface---an-onscreen-surface)
- [wl_seat - group of input devices](#wl_seat---group-of-input-devices)
- [wl_pointer - pointer input device](#wl_pointer---pointer-input-device)
- [wl_keyboard - keyboard input device](#wl_keyboard---keyboard-input-device)
- [wl_touch - touchscreen input device](#wl_touch---touchscreen-input-device)
- [wl_output - compositor output region](#wl_output---compositor-output-region)
- [wl_region - region interface](#wl_region---region-interface)
- [wl_subcompositor - sub-surface compositing](#wl_subcompositor---sub-surface-compositing)
- [wl_subsurface - sub-surface interface to a wl_surface](#wl_subsurface---sub-surface-interface-to-a-wl_surface)

## wl_display - core global object

核心全局对象。这是一个特殊的单例对象，它用于 Wayland 内部协议功能。

### wl_display 提供的请求

#### wl_display::sync - asynchronous roundtrip

- callback
  同步请求的新 [`wl_callback`](#wl_callback---callback-object) 的 ID

同步请求要求服务器在返回的 [`wl_callback`](#wl_callback---callback-object) 对象上发出“完成”事件。由于请求是按顺序处理的，事件是按顺序传递的，因此可以将其用作确保所有先前请求和结果事件均已处理的障碍。

触发回调后，此请求返回的对象将被合成器破坏，因此客户端在此之后不得尝试使用它。

回调中传递的 [`callback_data`](#wl_callback---callback-object) 是事件序列。

#### wl_display::get_registry - get global registry object

- registry
  新 [`wl_registry`](#wl_registry---global-registry-object) 的 ID

该请求创建一个注册表对象，该注册表对象允许客户端列出和绑定可从合成器获得的全局对象。

应该注意的是，响应 [`get_registry`](#wl_displayget_registry---get-global-registry-object) 请求而消耗的服务器端资源只能在客户端断开连接时释放，而在客户端代理销毁时不能释放。因此，客户端应尽可能少地调用 [`get_registry`](#wl_displayget_registry---get-global-registry-object) 以避免浪费内存。

### wl_display 提供的事件

#### wl_display::error - fatal error event

- object_id
  object - 发生错误的对象
- code
  uint - 错误代码
- message
  string - 错误说明

当发生致命（不可恢复）错误时，将发出错误事件。`object_id` 是发生错误的对象，通常是响应对该对象的请求。`code` 标识错误，并由对象接口定义。这样，每个接口都定义了自己的错误代码集。`message` 是错误的简短描述，以方便调试。

#### wl_display::delete_id - acknowledge object ID deletion

- id
  uint - 删除的对象 ID

对象 ID 管理逻辑在内部使用此事件。客户端删除对象时，服务器将发送此事件以确认它已看到删除请求。当客户端收到此事件时，它将知道它可以安全地重用对象 ID。

### wl_display 提供的枚举

#### wl_display::error - global error values

这些错误是全局错误，可以响应任何服务器请求而发出。

- invalid_object
  0 - 服务器找不到对象
- invalid_method
  1 - 指定的接口上不存在该方法
- no_memory
  2 - 服务器内存不足

## wl_registry - global registry object

## wl_callback - callback object

## wl_compositor - the compositor singleton

## wl_shm_pool - a shared memory pool

## wl_shm - shared memory support

## wl_buffer - content for a wl_surface

## wl_data_offer - offer to transfer data

## wl_data_source - offer to transfer data

## wl_data_device - data transfer device

## wl_data_device_manager - data transfer interface

## wl_shell - create desktop-style surfaces

## wl_shell_surface - desktop-style metadata interface

## wl_surface - an onscreen surface

## wl_seat - group of input devices

## wl_pointer - pointer input device

## wl_keyboard - keyboard input device

## wl_touch - touchscreen input device

## wl_output - compositor output region

## wl_region - region interface

## wl_subcompositor - sub-surface compositing

## wl_subsurface - sub-surface interface to a wl_surface
