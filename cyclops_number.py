def is_cyclops(n):
    if n == 0:
        return True
    
    if len(str(n)) % 2 == 0:
        return False
    
    middle = (len(str(n)) // 2)
    
    if str(n)[middle] != '0':
        return False

    nn = str(n)
    
    nn = nn[:middle] + nn[(middle+1):]
    for i in nn:
        if i == '0':
            return False
        
    return True   
        
print(is_cyclops(675409820))
