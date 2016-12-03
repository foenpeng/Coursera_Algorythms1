import csv
import random
import copy
with open("kargerMinCut.txt") as txt:
  value = csv.reader(txt, delimiter = "\t")  
  data = list(value)
[item.remove(item[-1]) for item in data]
dlist = [[int(i) for i in line] for line in data]


def contraction(data): 
  if len(data) > 2:    
    #[target1,target2] = random.sample(xrange(1,len(data)+1),2)
    #print(target1,target2)
    target1 = random.randint(1,len(data))
    t2v = data[target1-1][random.randint(2,len(data[target1-1]))-1] 
    t1v = data[target1-1][0]
    #t2v = data[target2-1][0]
    target2 = ([i[0] for i in data]).index(t2v) + 1
    #print(data)
    #print(t1v,t2v) 
    data[target1-1].extend(data[target2-1][1:])
    #print(data[target1-1])
    data[target1-1][1:] =[ x for x in data[target1-1][1:] if x != t1v and x != t2v]
    #print(data[target1-1])
    data.remove(data[target2-1])
    data = [[t1v if i == t2v else i for i in j ] for j in data]
    
    #print(data)
    return contraction(data)
  else:
    #print(data)
    return len(data[0])-1

i = 0
min = contraction(copy.deepcopy(dlist))
while i < 1000:
  result = contraction(copy.deepcopy(dlist))
  #print(0)
  if result < min: 
    min = result
  i += 1
print(min)

  