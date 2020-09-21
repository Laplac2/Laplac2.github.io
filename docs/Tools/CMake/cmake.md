# CMake

- [概述](#概述)
- [入门](#入门)
- [进阶](#进阶)
- [参考文献](#参考文献)

## 概述

CMake 是一个跨平台的开源构建工具，使用 CMake 能够方便地管理依赖多个库的目录层次结构并生成 makefile 和使用 GNU make 来编译和连接程序。

## 入门

CMakeLists.txt 内容如下：

```bash
cmake_minimum_required(VERSION 3.18)    # 设置cmake的最低版本
project(UnionTech)                      # 设置项目名字
add_executable(main main.cpp)           # 设定编译生成的二进制文件名字
```

上面这三个命令是必须的，有这三行就可以编译最简单的一个 main.cpp 了。

## 进阶

如果一个项目中有多个 `*.cpp` 文件，建议在项目的最外层放一个 `CMakeLists.txt` 文件，用于指定全局配置，在源文件目录的根目录再写一个 `CMakeLists.txt`。

- `add_library`
  - 构建静态链接库 `add_library(mathfunction STATIC mathfunction.cpp)`
  - 构建动态链接库 `add_library(mathfunction SHARED mathfunction.cpp)`
- `add_executable`
  - 构建可执行文件 `add_executable(main main.cpp)`
- `configure_file`
  - 配置文件 `configure_file(projectconfig.h.in projectconfig.h)`
- `aux_source_directory`
  - 搜索当前目录下的所有.cpp文件 `aux_source_directory(. SRC_LIST)`
- `set`
- `find_package`
- `target_link_libraries`
- `file`

## 参考文献

- [CMake多模块的构建方式](https://www.leadroyal.cn/?p=781)
- [CMake 入门](https://zhuanlan.zhihu.com/p/149828002)
