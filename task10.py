# Найти расстояние между двумя точками пространства
# Найти расстояние между двумя точками пространства

import os
os.system('cls')

print('Введите координату х1: ') 
x1 = int(input()) 
print('Введите координату х2: ') 
x2 = int(input()) 
print('Введите координату y1: ') 
y1 = int(input()) 
print('Введите координату y2: ') 
y2 = int(input()) 

i = 2       # степень

A = pow((x2-x1), i) 
B = pow((y2-y1), i) 


C = (A+B)**0.5
 
print('расстояние между 2х точек: ', C)