import time
import tensorflow as tf

begin = time.time()

with tf.device('/gpu:0'):
    rand_t = tf.random_uniform([50,50],0,10,dtype=tf.float32,seed=0)
    a = tf.Variable(rand_t)
    b = tf.Variable(rand_t)
    c = tf.matmul(a,b)
    init = tf.global_variables_initializer()

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True)) #强制使用GPU
sess.run(init)
print(sess.run(c))

end = time.time()
print(end-begin,'s')
