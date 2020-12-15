my_list = []
words_amount = []

with open(r"C:\Users\moglodko\PycharmProjects\Five\my_file_2.txt") as f_obj:
    for line in f_obj:
        my_list.append(line)
        words_amount.append(len(line.split(" ")))

lines_amount = len(my_list)

# lines_amount - количество строк
# words_amount - количество слов построчно