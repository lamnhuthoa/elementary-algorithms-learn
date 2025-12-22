# Text File IO
try:
    file = './input.txt'
    with open(file, mode='r') as file:
        line = file.readline()
        arr = line.split()
        a = int(arr[0])
        b = int(arr[1])
        
        line = file.readline()
        c = float(line)
        
        s = file.readline()
        
        print(a,b,c,s)
except FileNotFoundError:
    print("Error")