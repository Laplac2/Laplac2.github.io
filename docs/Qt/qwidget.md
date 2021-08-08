# QWidget

- [update()](https://doc.qt.io/qt-5/qwidget.html#update-1)
  普普通通的 update，调用时会重绘一下界面。

- [adjuest()](https://doc.qt.io/qt-5/qwidget.html#adjustSize)
  主角是父控件，当调用 adjuest()时，父控件去扫一遍子控件的范围，找出一个包含所有子控件的矩形范围作为自己的大小，然后调整大小（这即为根据内容调整大小的意思），猜测不会影响布局（文档未提及布局的事情，后续验证一下）。

- [updateGeometry()](https://doc.qt.io/qt-5/qwidget.html#updateGeometry)
  通知布局管理系统，当前 widget 发生变化了，可能需要改变几何形状（geometry）。可以理解为主角是子控件，当子控件内容或大小发生变化，通知父控件去刷新一下布局。当 [sizeHint()](https://doc.qt.io/qt-5/qwidget.html#sizeHint-prop) 或 [sizePolicy()](https://doc.qt.io/qt-5/qwidget.html#sizePolicy-prop) 发生变化后需要调用这个方法。
  当 widget 显式隐藏时，调用这个方法不会产生任何操作，但是只要 widget 显示出来，布局系统就会被通知刷新布局。（widget 隐藏时调用 updateGeometry，然后显示，会自动刷新布局？）

- [rect()](https://doc.qt.io/qt-5/qwidget.html#rect-prop)
  这个方法返回的是 widget 内部几何形状的大小（不包含菜单栏、工具栏、状态栏等窗口框架），返回值包含坐标，但始终为 0，即 QRect(0, 0, width(), height())。返回的几何范围就相当于 MainWindow 控件最中间的部分，不包含周围的菜单栏（QMenuBar）、工具栏（QToolBar）和状态栏（QStatusBar）等类似的东西。

- [geometry()](https://doc.qt.io/qt-5/qwidget.html#geometry-prop)
  这个方法返回的是 widget 内部几何形状的大小（不包含菜单栏、工具栏、状态栏等窗口框架），返回值是 QRect 包含坐标，这个坐标是相对于 widget（包含菜单栏、工具栏、状态栏等窗口框架）左上角的坐标，即 QRect(x, y, width(), height())。图参考 [Window Geometry](https://doc.qt.io/qt-5/application-windows.html#window-geometry)
