import tensorflow as tf
hello_constant = tf.constant('hello word!')
A = tf.constant(123)
B = tf.constant([123,456,789])
C = tf.constant([[123],[465]])
with tf.compat.v1.Session() as sess:
    output = sess.run(hello_constant)
    print(output)
    outputA = sess.run(A)
    print(outputA)
    outputB = sess.run(B)
    print(outputB)