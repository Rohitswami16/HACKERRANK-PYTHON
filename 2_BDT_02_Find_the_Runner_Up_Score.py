def find_runner_up(n, arr):
     li = list(set(arr))
     li.sort()
     return li[-2]
     
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res = find_runner_up(n,arr)
    print(res)
    
