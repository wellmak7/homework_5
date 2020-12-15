my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []

with open(r"C:\Users\moglodko\PycharmProjects\Five\my_file_4.txt") as f_obj:
    with open("C:\\Users\\moglodko\\PycharmProjects\\Five\\new_file.txt", "w") as h_obj:
        for line in f_obj:
            el = line.split(" ")
            print(my_dict.get(el[0]), el[1], el[2], file=h_obj)