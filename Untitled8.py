#!/usr/bin/env python
# coding: utf-8

# ### программа на вход которой даются четыре числа a, b, c и d, каждое в своей строке. 
# ### Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
# 
# Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.
# 
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

# In[3]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print (' ')
for j in range (c, d+1):
    if j == c:
        print (' ', j, end=" " )
    else:    
        print (j, end=" " )
print('\t')
for i in range(a, b+1):
    print (i, end=" " )
    for j in range(c, d+1):
        
        
        if i*j < 10:
            print (" ",end="")
 
        print (i*j,end=" " )
 
    
    print()


# In[ ]:




