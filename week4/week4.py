import copy
import csv

with open("scc.txt") as txt:
  value = csv.reader(txt, delimiter = "\t")  
  data = list(value)
del data[1::2]

x = [[int(i) for i in line[0].split()] for line in data]
#x = [[1,2],[2,1],[1,3],[3,2],[3,4],[2,4]]


# create the list and reverse list
max_i = max(map(max,x))
graph = [[i+1] for i in range(max_i)]
graph_rev = copy.deepcopy(graph)
for item in x:
  graph[item[0]-1].append(item[1])
  graph_rev[item[1]-1].append(item[0])

t = 0
time = []
X = []
print("list reversed")

      
def dfs(G,v):
  global t,time,X
  #if len(G[v-1])>1:
  for i in G[v-1][1:]:
      if i not in X:
        X.append(i)
        dfs(G,i)
  t += 1
  time.append([v,t])
  if v not in X:
    X.append(v)
    
def dfs2(G,v):
  global t,time
  S = [v]
  while S != []:
    lenS = len(S)
    vert = S[-1]
    unexpld = list(set(G[vert-1][1:])-set(X))
    if unexpld != []:
      X.append(unexpld[0])
      S.append(unexpld[0])
    else:
      S.pop()
      t += 1
      time.append([vert,t])
    

def replace(G, reference):
  G_r = copy.deepcopy(G)
  for i in reference:
    for n,row in enumerate(G):
      for m,element in enumerate(row):
        if element == i[0]:
          G_r[n][m] = i[1] 
  return G_r

for i in xrange(1,len(graph)):
  if i not in X:
    X.append(i)
    dfs2(graph,i)

print("first dfs done")

graph_sec = replace(graph_rev, time) 
graph_sort = sorted(graph_sec, key = lambda x: x[0])

length = []
X = []
for i in reversed(xrange(1,len(graph_sort)+1)):
  if i not in X:    
    X.append(i)
    dfs2(graph_sort,i)
    m = len(X)
    length.append(m)



length.insert(0,0)
length_new = [y-x for x,y in zip(length,length[1:])]
print(sorted(length_new, reverse = True)[:4])