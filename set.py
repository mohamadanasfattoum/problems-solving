#Set Methods
#add
n = list(int(input()))
#l = list(n.split())
m = list(int(input()))
#k = list(m.split())
s1 = set(n)
s2 = set(m)
print(len(s1.add(s2)))
'''
# union
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
s1 = set(l)
s2 = set(k)
print(len(s1.union(s2)))

# difference
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
s1 = set(l)
s2 = set(k)
print(len(s1.difference(s2)))

# intersection
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
s1 = set(l)
s2 = set(k)
print(len(s1.intersection(s2)))

#symmetric_difference

n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())
s1 = set(l)
s2 = set(k)
print(len(s1.symmetric_difference(s2)))

'''