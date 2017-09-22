import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


x = tf.placeholder(tf.float32,[None,784])	#inputs
W = tf.Variable(tf.zeros([784,10]))	#W
b = tf.Variable(tf.zeros([10]))	#b
y = tf.nn.softmax(tf.matmul(x,W)+b)	
yc = tf.placeholder(tf.float32,[None,10])	#corrext values
cross_entropy = tf.reduce_mean(-tf.reduce_sum(yc * tf.log(y), reduction_indices=[1])) #error

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
# writer = tf.summary.FileWriter('./logs', sess.graph)
tf.global_variables_initializer().run()
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, yc: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(yc,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, yc: mnist.test.labels}))


