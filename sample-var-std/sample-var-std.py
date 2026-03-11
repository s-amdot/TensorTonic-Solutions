import numpy as np

def sample_var_std(x):
    x=np.array(x)
    n=len(x)
    mean=sum(x)/n
    sqdiff=(x-mean)**2
    var=np.sum(sqdiff)/(n-1)
    std=np.sqrt(var)
    return var, std
    pass