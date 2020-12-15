surnames = []
salary = []

with open(r"C:\Users\moglodko\PycharmProjects\Five\my_file_3.txt") as f_obj:
    for line in f_obj:
        el = line.split(" ")
        if int(el[1]) < 20000:
            surnames.append(el[0])
        else:
            pass
        salary.append(int(el[1]))

print("Фамилии тех, кто получает менее 20 тыс.: ", surnames)
print("Средняя величина дохода сотрудников: ", sum(salary) / len(salary))