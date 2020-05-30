import tensorflow as tf
import numpy as np

X = np.arange(-10, 11) 
#[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

y = 2*X+1              
#[-19,-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21]

l1 = tf.keras.layers.Dense(units=1, input_shape=[1])

model = tf.keras.Sequential([l1])

model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(X, y, epochs=30, verbose=False) # epochs=30, 100 or 300

l1_weight = l1.get_weights()

w = l1_weight[0]
print("w = ", w)

b = l1_weight[1]
print("b = ", b)

result = model.predict([-2]) # f(-2)=?
print("f(-2) = ", result)











