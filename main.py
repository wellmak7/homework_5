with open(r"C:\Users\moglodko\PycharmProjects\Five\my_file.txt", "w") as f_obj:
    for i in range(10000000000):
        el = input('Введите данные: ')
        print(el, file=f_obj)
        if el == "":
            print('Конец')
            break