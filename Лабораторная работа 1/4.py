users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
count_users_all = len(users)
set_of_list = set(users)
count_users_unique = len(set_of_list)

describe = {"Общее количество": 0 , "Уникальные посещения": 0}
describe["Общее количество"] = count_users_all
describe["Уникальные посещения"] = count_users_unique
print(describe)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

