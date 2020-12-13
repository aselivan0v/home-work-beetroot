#List comprehension exercise
#Use a list comprehension to make a list containing tuples (i, j) where `i`
#goes from 1 to 10 and `j` is corresponding to `i` squared.


#for i in range (1, 11):
#    j = i * i
#    print(i,'*', i, '=', j)
w = [(i, i * i) for i in range (1, 11)]
print(w)