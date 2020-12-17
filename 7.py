import json

profit_list = []
my_dict ={}
final_list = []

with open(r"C:\\Users\\moglodko\\PycharmProjects\\Five\\my_file_7.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        list_1 = line.split(" ")
        name = list_1[0]
        income = list_1[2]
        costs = list_1[3]
        profit = int(income) - int(costs)

        if profit > 0:
            profit_list.append(profit)

        my_dict[name] = profit

average_profit = sum(profit_list) / len(profit_list)
average_dict = {}
average_dict['average_profit'] = average_profit
final_list = [my_dict, average_dict]

print(final_list)

with open("json_file.json", "w") as write_f:
    json.dump(final_list, write_f)
