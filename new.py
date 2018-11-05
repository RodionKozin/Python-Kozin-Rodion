def filter():
    unique=[]
    for element in arr:
        if func(element)=1:
		    unique.append(element)
		elif func(element)=0:
		    unique.remove(element)
		else:
		    write("Error")
	return unique
# функция filter(arr, func), которая получает массив arr и возвращает новый, в который входят только те элементы arr, для которых func возвращает true	
