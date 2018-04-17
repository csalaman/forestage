import numpy as np

#NeuNet: Linear Regression
#ASSUMING ONLY 3 Params: YOUNG,MIDDLE,OLD
def gradient(data,theta,prox):
    activation = theta[0]*data[0]+theta[1]*data[1]+theta[2]*data[2]+theta[3]
    w_young = 2*(activation-prox)*data[0]
    w_middle = 2*(activation-prox)*data[1]
    w_old = 2*(activation-prox)*data[2]
    bias = 2*(activation-prox)
    result = np.array([w_young,w_middle,w_old,bias],dtype=np.float64)
    return result
def ln_train(data,k,eta,prox):
    theta = np.array([],dtype=np.float64);
    for i in range(len(data)):
        theta = np.append(theta,np.random.normal(0,1))
    theta= np.append(theta, np.random.normal(0,1))
    # for i in range(k):
    # theta = theta-eta*\
    for i in range(0,k):
        # print "Before :"+str(theta)+" Ite:"+str(i)
        theta = theta-eta*gradient(data,theta,prox)
        # print "After :" + str(theta) + " Ite:" + str(i)
    return theta

def ln_test(theta,data):
    return theta[0]*data[0]+theta[1]*data[1]+theta[2]*data[2]+theta[3]