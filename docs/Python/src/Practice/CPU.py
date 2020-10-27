import time
import tensorflow as tf

begin = time.time()

with tf.device('/cpu:0'):
    rand_t = tf.random.uniform([50,50],0,10,dtype=tf.float32,seed=0)
    a = tf.Variable(rand_t)
    b = tf.Variable(rand_t)
    c = tf.matmul(a,b)
    init = tf.compat.v1.global_variables_initializer()

sess = tf.compat.v1.Session()
sess.run(init)
print(sess.run(c))

end = time.time()
print(end-begin,'s')

