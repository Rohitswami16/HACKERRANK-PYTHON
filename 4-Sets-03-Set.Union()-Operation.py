# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

set1 = set(map(int, input().split(" ")))

n2 = int(input())

set2 = set(map(int, input().split()))

set3 = set(set1.union(set2))

print(len(set3))
