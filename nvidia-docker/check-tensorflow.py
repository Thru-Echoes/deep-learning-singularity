import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
print(tf.__version__)
print(tf.test.is_gpu_available())
