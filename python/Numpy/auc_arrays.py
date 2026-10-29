import numpy

def arrays(arr):
    a = numpy.array(arr)
    return a[::-1].astype(float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)