# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44 * 1024 * 1024
count_page = 100
count_line = 50
count_sim = 25
bt = 4
all_sim = count_page * count_line * count_sim
all_bt = all_sim * bt
count_book = round(V//all_bt)
print("Количество книг, помещающихся на дискету:", count_book)
