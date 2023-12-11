# TODO Найдите количество книг, которое можно разместить на дискете
size_Mb = 1.44
pages = 100
lines = 50
simv = 25
size_one = 4
size_bites = size_Mb*1024*1024
count_simv = (pages*lines*simv*size_one)
count_books = int(size_bites//count_simv)

print("Количество книг, помещающихся на дискету:", count_books)
