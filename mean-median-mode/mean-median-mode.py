import numpy as np
from collections import Counter

def mean_median_mode(x):
    x=np.array(x)
    n=len(x)
    if n<=0:
        print("Invalid argument")
    mean=sum(x)/n
    sorted_x=np.sort(x)
    mid=n//2
    median=sorted_x[mid] if n%2!=0 else (sorted_x[mid-1]+sorted_x[mid])/2
    values, counts = np.unique(x, return_counts=True)
    mode = values[np.argmax(counts)]
    return mean, median, mode
    pass