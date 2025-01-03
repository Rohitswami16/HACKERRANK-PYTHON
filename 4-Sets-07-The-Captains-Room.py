# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

rooms = list(map(int, input().split()))

room = set(rooms)

c = (sum(room)*n-sum(rooms))//(n-1)
print(c)

