C = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '40']
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
B = [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ls = []
for a,b in zip(A, B):
    ls.append(a * b)
print(ls)
total_price = sum(ls)
print(total_price)
av_price = total_price/sum(A)
print(av_price)
how_many = max(A)
x = C[A.index(how_many)]
print(x)