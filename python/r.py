def largest_list(list):
	if(len(list)< 1):
        return list
    else:
        x = largest_list(list)
        max = list[1]
        if list[x] > max:
            list[x] = max
        else:
            continue
        return largest_list(list+1)
            

print(largest_list(list = [5, 6, 7, 13, 2]))
	
	