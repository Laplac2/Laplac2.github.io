import tensorflow as tf
import numpy as np
# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3
# create model
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
# calculate error
loss = tf.reduce_mean(tf.square(y-y_data))
#用梯度下降法反向传播误差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
#训练
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好

sess = tf.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))