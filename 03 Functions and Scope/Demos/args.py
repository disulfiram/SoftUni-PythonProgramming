def sum_numbers(*args):   # args ще бъде tuple, който ще съдържа стойностите на всички подадени позиционни параметри
    total = 0
    for n in args:
        total += n
    return total

# ... и да - знаем, че в Python има много по-кратък начин да свършим същата работа :о)

print(sum_numbers())
print(sum_numbers(4))
print(sum_numbers(5, 1, 49, 26, 45, 34, 3, 81))