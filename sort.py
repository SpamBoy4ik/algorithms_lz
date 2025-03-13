from random import randint as ri

choise = input("Прочитать файл(0) или сгенерировать список(1): ")
if choise == "0":
    input_file = open("sort_input.txt")
    input_data = input_file.read()
    input_list = input_data.split(", ")
    for index in range(len(input_list)):
        input_list[index] = int(input_list[index])
    input_file.close()

    output_file = open("sort_output.txt", 'w')
    output_file.write(f"Unsorted list: {input_list}\n")

    output_file.write("Sorting by selection:\n") # сортировка выборкой
    sample_counter = 0
    sample_numbers = []
    temp_numbers = input_list.copy() # вспомогательный список для сортировки
    while len(temp_numbers) > 0:
        min = temp_numbers[0]
        for index in range(len(temp_numbers)):
            sample_counter += 1
            if min > temp_numbers[index]:
                min = temp_numbers[index]
        sample_numbers.append(min)
        temp_numbers.remove(min)
        output_file.write(f"{sample_numbers}\n")
    output_file.write(f"Sorted list: {sample_numbers}.\nNeeded {sample_counter} comparisons.\n")

    output_file.write("Bubble sorting:\n") # сорт. пузырьком 
    bubble_count = 0
    bubble_numbers = input_list.copy()
    flag = True
    while flag:
        flag = False
        for i in range(len(bubble_numbers) - 1):
            bubble_count += 1
            if bubble_numbers[i] < bubble_numbers[i + 1]:
                bubble_numbers[i], bubble_numbers[i + 1] = bubble_numbers[i + 1], bubble_numbers[i]
                # temp = bubble_numbers[i]
                # bubble_numbers[i] = bubble_numbers[i+1]
                # bubble_numbers[i+1] = temp
                flag = True
                output_file.write(str(bubble_numbers) + "\n")     
    output_file.write(f"Sorted list: {bubble_numbers}.\nNeeded {bubble_count} comparisons.\n")
    output_file.close()

else:
    NUMBERS = []
    for _ in range(20):
        NUMBERS.append(ri(0, 1000))
    print(f"Исходный список: {NUMBERS}")

    print("Сортировка выборкой:")
    sample_counter = 0
    sample_numbers = []
    temp_numbers = NUMBERS.copy() # вспом. список для сортировки
    while len(temp_numbers) > 0:
        min = temp_numbers[0]
        for index in range(len(temp_numbers)):
            sample_counter += 1
            if min > temp_numbers[index]:
                min = temp_numbers[index]
        sample_numbers.append(min)
        temp_numbers.remove(min)
        print(f"{sample_numbers}")
    print(f"Отсортированный список: {sample_numbers}.\n Понадобилось {sample_counter} сравнений.\n")

    print("Сортировка пузырьком:")
    bubble_numbers = NUMBERS.copy()
    bubble_count = 0
    flag = True
    while flag:
        flag = False
        for i in range(len(bubble_numbers) - 1):
            bubble_count += 1
            if bubble_numbers[i] < bubble_numbers[i + 1]:
                bubble_numbers[i], bubble_numbers[i + 1] = bubble_numbers[i + 1], bubble_numbers[i]
                # temp = bubble_numbers[i]
                # bubble_numbers[i] = bubble_numbers[i+1]
                # bubble_numbers[i+1] = temp
                flag = True
                print(bubble_numbers)     
    print(f"Отсортированный список: {bubble_numbers}.\n Понадобилось {bubble_count} сравнений.")
