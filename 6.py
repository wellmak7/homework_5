my_dict ={}

with open(r"C:\\Users\\moglodko\\PycharmProjects\\Five\\my_file_6.txt", encoding='utf-8') as f_obj:
    for line in f_obj:

        list_1 = line.split(":")
        name = list_1[0]
        list_2 = list_1[1].split(" ")

        try:
            list_3 = list_2[1].split("(")
            first_num = int(list_3[0])
        except IndexError:
            pass
        except ValueError:
            first_num = 0

        try:
            list_4 = list_2[2].split("(")
            second_num = int(list_4[0])
        except IndexError:
            pass
        except ValueError:
            second_num = 0

        try:
            list_5 = list_2[3].split("(")
            third_num = int(list_5[0])
        except IndexError:
            pass
        except ValueError:
            third_num = 0

        sum_list = first_num + second_num + third_num

        my_dict[name] = sum_list

print(my_dict)