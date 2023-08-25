import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.") 
    array = np.array(list)
    array1 = array.reshape(3,3)
    calculation = dict()
    mean= [array1.mean(axis=0).tolist()] + [array1.mean(axis=1).tolist()] + [array.mean().tolist()]
    var = [array1.var(axis=0).tolist()] + [array1.var(axis=1).tolist()] + [array.var().tolist()]
    std = [array1.std(axis=0).tolist()] + [array1.std(axis=1).tolist()] + [array.std().tolist()]
    max = [array1.max(axis=0).tolist()] + [array1.max(axis=1).tolist()] + [array.max().tolist()]
    min = [array1.min(axis=0).tolist()] + [array1.min(axis=1).tolist()] + [array.min().tolist()]
    sum = [array1.sum(axis=0).tolist()] + [array1.sum(axis=1).tolist()] + [array.sum().tolist()]
    calculations = {
      'mean' : mean,
      'variance' : var,
      'standard deviation': std,
      'max' : max,
      'min' : min,
      'sum' : sum
    }

    return calculations