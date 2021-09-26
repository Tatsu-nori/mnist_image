import pickle
import gzip
import numpy as np

def load_data():
    f = gzip.open('mnist.pkl.gz', 'rb')
    data0, data1, data2 = pickle.load(f, encoding="latin1")
    f.close()
    return (data0)

def load_data_wrapper():
    d = load_data()
    img = [np.reshape(x, (784, 1)) for x in d[0]]
    num = d[1]
    return (img, num)


