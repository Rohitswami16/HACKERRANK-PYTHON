# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())

s1 = set(map(int, input().split(" ")))

n2 = int(input())

s2 = set(map(int, input().split(" ")))

print(len(s1.intersection(s2)))
