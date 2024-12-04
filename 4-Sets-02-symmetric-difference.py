# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())

set1 = set(map(int, input().split()))

n2 = int(input())

set2 = set(map(int, input().split()))

sd = set(set1.symmetric_difference(set2))

s = sorted(sd)
for i in s:
    print(f"{i}", end="\n")
