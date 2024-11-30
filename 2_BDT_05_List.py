if __name__ == '__main__':
    N = int(input())
    
    li = [];
    for i in range(N):
        command = input().split()  
        if command[0] == "insert":
            index = int(command[1])
            value = int(command[2])
            li.insert(index, value)
        elif command[0] == "print":
            print(li)
        elif command[0] == "remove":
            value = int(command[1])
            li.remove(value)
        elif command[0] == "append":
            value = int(command[1])
            li.append(value)
        elif command[0] == "sort":
            li.sort()
        elif command[0] == "pop":
            li.pop()
        elif command[0] == "reverse":
            li.reverse()
