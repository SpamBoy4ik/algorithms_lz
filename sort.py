from random import randint as ri

choise = input("Прочитать файл(0) или сгенерировать список(1): ")
if choise == "0":
    file_name = input("Введите название файла: ")
    input_file = open(f"{file_name}.txt")
    input_data = input_file.read()
    input_list = input_data.split(", ")
    for index in range(len(input_list)):
        input_list[index] = int(input_list[index])
    input_file.close()

    output_file = open("out.txt", 'w')
    output_file.write(f"Unsorted list: {input_list}\n")
    output_file.write("Sorting by selection:\n") # сорт. выборкой
    sample_count = 0
    sample_numbers = []
    temp_numbers = input_list.copy() # вспом. список для сортировки
    for i in range(len(temp_numbers)):
        sample_numbers.append(max(temp_numbers))
        temp_numbers.remove(max(temp_numbers))
        output_file.write(str(sample_numbers) + "\n")
        sample_count += 1
    output_file.write(f"Sorted List: {sample_numbers}.\n")

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
    for _ in range(10):
        NUMBERS.append(ri(0, 1000))
    print(f"Исходный список: {NUMBERS}")

    print("Сортировка выборкой:")
    sample_count = 0
    sample_numbers = []
    temp_numbers = NUMBERS.copy() # вспом. список для сортировки
    for i in range(len(temp_numbers)):
        sample_numbers.append(max(temp_numbers))
        temp_numbers.remove(max(temp_numbers))
        print(sample_numbers)
        sample_count += 1
    print(f"Отсортированный список: {sample_numbers}.")

    print("Сортировка пузырьком:")
    bubble_count = 0
    bubble_numbers = NUMBERS.copy()
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
