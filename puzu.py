def sorti(li):
    n = 1 
    while n < len(li):
        for i in range(len(li)-n):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
        n += 1
    return li
			   
print(sorti([1,3,5,7]))