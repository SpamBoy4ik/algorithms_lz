choise = input("Прочитать файл(0) или работать в терминале(1): ")
target = int(input("Искомый элемент: "))

if choise == "0":
    input_file = open("search_input.txt")
    input_data = input_file.read()
    input_list = input_data.split(", ")
    for index in range(len(input_list)):
        input_list[index] = int(input_list[index])
    input_file.close()
    output_file = open("search_output.txt", "w")

    output_file.write(f"Sorted list: {input_list}\n Target: {target}\n")
    
    if target in input_list:
        # бинарный поиск (требует список, отсортированный в порядке убывания)
        output_file.write("Binary search:\n")
        flag = True
        first_index = 0
        last_index = len(input_list) - 1
        counter = 0
        while flag:
            mid_index = (first_index + last_index) // 2
            if input_list[mid_index] == target:
                output_file.write(f"The index of the item in the list: {mid_index}\n It took {counter} comparisons.\n")
                flag = False
                counter += 1
            elif input_list[mid_index] < target:
                last_index = mid_index - 1
                counter += 2
            elif input_list[mid_index] > target:
                first_index = mid_index + 1
                counter += 3

        # линейный поиск
        counter = 0
        output_file.write("Linear search:\n")
        for i in range(len(input_list)):
            counter += 1
            if input_list[i] == target:
                output_file.write(f"The index of the item in the list: {i}\n It took {counter} comparisons.\n")
                break
    else:
        output_file.write(f"{target} is not in the list.\n")
    output_file.close()

else:
    sorted_list = [999, 713, 412, 321, 201, 199, 178, 98, 49, 2]
    print(f"Список: {sorted_list}")
    if target in sorted_list:
        # бинарный поиск (требует список, отсортированный в порядке убывания)
        print("Бинарный поиск:")
        flag = True
        first_index = 0
        last_index = len(sorted_list) - 1
        counter = 0
        while flag:
            mid_index = (first_index + last_index) // 2
            if sorted_list[mid_index] == target:
                 print(f"Индекс искомого элемента: {mid_index}\n Понадобилось {counter} сравнений.")
                 flag = False
                 counter += 1
            elif sorted_list[mid_index] < target:
                last_index = mid_index - 1
                counter += 2
            elif sorted_list[mid_index] > target:
                first_index = mid_index + 1
                counter += 3

        # линейный поиск
        counter = 0
        print("Линейный поиск:")
        for i in range(len(sorted_list)):
            counter += 1
            if sorted_list[i] == target:
                print(f"Индекс искомого элемента: {i}\n Понадобилось {counter} сравнений.")
                break
    else:
        print(f"{target} нет в списке.")