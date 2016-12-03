## merger sort

import numpy as np

with open("IntegerArray.txt", "r") as txt:
  list = txt.readlines()
  array = [float(item.strip('\r\n')) for item in list]


def mergy(a,b):
  i = 0;
  j = 0;
  c = [];
  d = 0;
  while len(c) < len(a) + len(b) -1:
    if a[i] <= b[j]:
      c.append(a[i])
      if i < len(a)-1:
        i+=1 
      else:
        c.extend(b[j:])       
    else:
      if j < len(b) - 1:        
        c.append(b[j])
        d+=len(a[i:])
        j+= 1
      else:
        c.append(b[j])
        c.extend(a[i:]) 
        d+=len(a[i:])    
  return c,d

def mergy_recurs(list):
  global count
  result = []
  length = len(list)
  if length == 1:
    return count
  else:
    for i in range(length/2):
      [element,d] = mergy(list[2*i],list[2*i+1])
      result.append(element)
      count += d
    if length % 2 != 0:
      [result[-1],d] =  mergy(result[-1],list[-1])
      count += d
    mergy_recurs(result)


count = 0
mergy_recurs(divide_outcome)
print(count)
