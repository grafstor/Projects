import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def nonlin(x,deriv=False):
    f  = sigmoid(x)
    if(deriv==True):
        return f*(1 - f)
    return f
    
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
                
y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
print(syn0)
print(syn1)
for j in range(60000):
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    l2_error = y - l2
    
    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error*nonlin(l2,True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1,True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)