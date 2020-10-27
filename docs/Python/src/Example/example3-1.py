import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1' # 默认，显示所有信息 
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2' # 只显示 warning 和 Error 
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3' # 只显示 Error

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

#定义神经网络的隐藏层
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random.normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

#定义数据
x_data = np.linspace(-1,1,300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise
#y_data = np.sin(x_data) - 0.5 + noise

xs = tf.compat.v1.placeholder(tf.float32, [None, 1])
ys = tf.compat.v1.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

prediction = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

train_step = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)

# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.compat.v1.global_variables_initializer()  # 替换成这样就好

sess = tf.compat.v1.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)

