 Enter your code here. Read input from STDIN. Print output to STDOUT

set1 = set(map(int, input().split()))

n = int(input())
issuper = True
for _ in range(n):
    
    set2 = set(map(int, input().split()))
    if not(set1.issuperset(set2) and set1 != set2):
        issuper = False
        break
        
print(issuper)
    
