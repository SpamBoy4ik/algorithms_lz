sorted_list = [1, 6, 21, 43, 68, 99, 101]
print(f"Список: {sorted_list}")
target = int(input("Искомый элемент: "))

# линейный поиск
'''for i in range(len(sorted_list)):
    if sorted_list[i] == target:
        print(f"Индекс элемента в списке: {i}")
        break
    if i == len(sorted_list) - 1:
        print(f"{target} нет в списке.")
        break'''

# бинарный поиск
working = True
mid_element = (len(sorted_list) -1) // 2
while working:
    if sorted_list[mid_element] > target:
        mid_element //= 2
    elif sorted_list[mid_element] < target:
        mid_element += mid_element // 2
    elif sorted_list[mid_element] == target:
        print(f"Индекс элемента в списке: {mid_element}")
        working = False
    else:
        print(f"{target} нет в списке.")
        working = False