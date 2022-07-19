T = int(input())

for t in range(T):
  h = list(map(int, input().strip().split()))
  fig = {}
  for i in h:
    if i not in fig.keys():
      fig[i] = 1
    else:
      fig[i] += 1
  keys = list(fig.keys())
  l = len(fig.keys())
  if l==1:
    if fig[keys[0]] == 12:
      print("yes")
    else:
      print("no")
  elif l==2:
    a, b = fig[keys[0]], fig[keys[1]]
    if (a==8 and b==4) or (a==4 and b==8):
      print("yes")
    else:
      print("no")
  elif l==3:
    a, b, c = fig[keys[0]], fig[keys[1]], fig[keys[2]]
    if a==b==c:
      print("yes")
    else:
      print("no")
  else:
    print("no")