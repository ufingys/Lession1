"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

def my_func(x, y):
  if y == 0:
      return 1 / x
  return my_func(x, y+1) / x

while True:
    print("Программа возведения положительного числа в отрицательную степень (для завершения ввода введите 'q')")
    try:
        numb1 = float(input("Введите число: "))
        numb2 = int(input("Введите степень: "))
        if numb2 > 0:
            numb2 = -numb2
        if numb2 == 0:
            print('Степень = 1')
        print(f"Степень = {my_func(numb1, numb2+1)}")
    except ValueError:
        print("end")
        break