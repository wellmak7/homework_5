with open("C:\\Users\\moglodko\\PycharmProjects\\Five\\my_file_5.txt", "w") as h_obj:
    first_number = 25
    second_number = 36
    third_number = 47
    forth_number = 18
    five_number = 75

    print(first_number, second_number, third_number, forth_number, five_number, file=h_obj)

with open(r"C:\Users\moglodko\PycharmProjects\Five\my_file_5.txt") as f_obj:

    for line in f_obj:
        el = line.split(" ")
        el_count = len(el)
        el_sum = 0
        for i in range (0, el_count):
            el_sum = el_sum + int(el[i])
print("Сумма чисел: ", el_sum)