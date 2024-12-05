# Enter your code here. Read input from STDIN. Print output to STDOUT

sets = set()

n = int(input())
for _ in range(n):
    country = input().strip()
    sets.add(country)
    
print(len(sets))

