numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_of_n1 = sum(numbers[:4])
sum_of_n2 = sum(numbers[5:])
sum_sum = sum_of_n1 + sum_of_n2
count_of_n = len(numbers)
average_of_n = round(sum_sum/count_of_n,2)
numbers[4] = average_of_n
print("Измененный список:", numbers)
