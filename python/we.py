def recursive_lines(n):
    c = 1
    if c > n:
        return 0
    else:
        return " * " * c 
        c +=1
        recursive_lines(n-1)
    
print(recursive_lines(9))
   
