numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_of_none = 4
new_numbers = numbers[: index_of_none] + [0] + numbers [index_of_none+1 : ]
sum_numbers = sum(new_numbers)
count_numbers = len(new_numbers)
averange = sum_numbers/count_numbers
new_numbers[index_of_none]= averange
print("Измененный список:", new_numbers)
