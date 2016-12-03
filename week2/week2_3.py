# quick sort _ first element as pivot
with open("QuickSort.txt") as txt:
  out = txt.readlines()
  array = [float(item.strip("/r/n")) for item in out]
#array = [5,1,4,8,2,9,6,7,3,14,20,11,10]

def swap(a, b):
  t = a
  a = b
  b = t
  return a,b


def sort(array):
  print(array)
  global count
  length = len(array)
  if length > 1:
    if length % 2 == 0:
        middle = array[length/2-1]
    else:
        middle = array[length/2]
    pivot  = sorted([array[0],array[-1],middle])[1]
    print(pivot)
    p_index = array.index(pivot)
    [array[0],array[p_index]] = swap(array[0], array[p_index])
    i = 1
    j = 0
    while i <= length-1:
      
      if array[i] < pivot:
        [array[j+1],array[i]] = swap(array[j+1],array[i])
        j += 1
      i += 1
    [array[0],array[j]] = swap(array[0],array[j])

    count+= length - 1
    print(array)
    sort(array[:j])
    sort(array[j+1:]) 

count = 0
sort(array)
print(count)