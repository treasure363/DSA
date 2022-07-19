s = input()
total = 0
o, c = 0, 0
for i in s:
    if i == '(':
        o += 1
    if i == ')':
        c += 1
dp = [0, 0, 1, 2]
for i in range(4, c+1):
    pass
win = 0
for i in s:
    if i == '(':
        win += 1
    if i == ')':
        c -= 1
    if win == 2:
        win -= 1
        total += 


'''
(()         0           f(1)=0
(())        1           f(2)=1
(()))       2           f(3)=2
(())))      6           f(4)=6
(()))))     10          f(5)=10
(())))))    15          f(6)=15
(()))))))   
'''