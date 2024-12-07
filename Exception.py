# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
 
    try:
        a, b = input().split()  
        result = int(a) // int(b)  
        print(result)
    except ZeroDivisionError as e:  
        print("Error Code:", e)
    except ValueError as e:  
        print("Error Code:", e)
