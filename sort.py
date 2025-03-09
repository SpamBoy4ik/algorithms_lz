from random import randint as ri

if int(input("Файли(0) или сгенерировать(1):")) == 0:
    file_name = input("Введите название файла: ")
    f = open(f"{file_name}.txt", "r+")
    text = f.read()
    NUMBERS = list(text)
    print(NUMBERS)


# NUMBERS = []
# for _ in range(100):
#     NUMBERS.append(ri(0, 1000))
# print(f"Исходный список:{NUMBERS}")

# print("Сортировка выборкой:")
# sample_count = 0
# sample_numbers = []
# temp_numbers = NUMBERS.copy() # вспом. список для сортировки
# for i in range(len(temp_numbers)):
#     sample_numbers.append(max(temp_numbers))
#     temp_numbers.remove(max(temp_numbers))
#     print(sample_numbers)
#     sample_count += 1
# print(f"Отсортированный список: {sample_numbers}.\nПонадобилось {sample_count} сравнений.")

# print("Сортировка пузырьком:")
# bubble_count = 0
# bubble_numbers = NUMBERS.copy()
# print(bubble_numbers)
# flag = True
# while flag:
#     flag = False
#     for i in range(len(bubble_numbers) - 1):
#         bubble_count += 1
#         if bubble_numbers[i] < bubble_numbers[i + 1]:
#             bubble_numbers[i], bubble_numbers[i + 1] = bubble_numbers[i + 1], bubble_numbers[i]
#             # temp = bubble_numbers[i]
#             # bubble_numbers[i] = bubble_numbers[i+1]
#             # bubble_numbers[i+1] = temp
#             flag = True
#             print(bubble_numbers)     
# print(f"Отсортированный список: {bubble_numbers}.\nПонадобилось {bubble_count} сравнений.")
