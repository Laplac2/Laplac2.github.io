# TensorFlow

## 配置环境

1. 检查是否已配置 Python 环境

   ```bash
   python --version
   pip --version
   virtualenv --version
   ```

2. 安装 virtualenv 虚拟环境工具

   ```bash
   pip3 install -U pip virtualenv
   ```

3. 创建一个新的虚拟环境

   ```bash
   # 选择 Python 解析器并创建一个 .\venv 目录来存放虚拟环境
   virtualenv --system-site-packages -p python ./venv
   ```

4. 激活虚拟环境

   ```bash
   .\venv\Scripts\activate
   ```

5. 在虚拟环境中安装软件包

   ```bash
   pip install --upgrade pip    # 首先升级 pip
   pip list                     # show packages installed within the virtual environment
   pip show [packages]          # show the specific information of packages
   ```

6. 安装 TensorFlow

   ```bash
   pip install --upgrade tensorflow
   ```

7. 验证安装效果

   ```bash
   python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   ```

8. 退出虚拟环境

   ```bash
   deactivate # don't exit until you're done using TensorFlow
   ```

## QA

- 问题：`import tensorflow as tf` 执行出错

  原因：numpy 版本太高，不支持

  解决办法：卸载 numpy 1.17.0，安装 numpy 1.16.0

  命令：`pip uninstall numpy，pip install numpy==1.16.0`

- 问题：`import matplotlib.pyplot as plt` 出错

  原因：matplotlib 版本较低，可以通过安装新版本 matplotlib 解决(3.0.x)

  命令：`pip install -U matplotlib`

- 问题：提示 Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2

  原因：<https://blog.csdn.net/zhaohaibo_/article/details/80573676>

  解决办法：意思是你的 CPU 支持 AVX AVX2 （可以加速 CPU 计算），但你安装的 TensorFlow 版本不支持，在代码最开始加上下面命令改变 `os.environ['TF_CPP_MIN_LOG_LEVEL']` 的值，不提示这个问题

  ```bash
  import os
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
  #os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1' # 默认，显示所有信息
  #os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2' # 只显示 warning 和 Error
  #os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3' # 只显示 Error
  ```
