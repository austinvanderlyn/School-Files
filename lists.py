a_list = [1, 'hello', [1, 2, 3], 'True']
print(a_list)
var = a_list[1]
print(var)
var2 = a_list[1:4]
print(var2)
L = ['Michael Jackson', 10.1, 1982]
print(L)
sample_list = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
print(sample_list)
print(sample_list[3:5])
L = ["Michael Jackson", 10.2]
print(L)
L.extend(['pop', 10])
print(L)
L = ["Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
print('Before change:', A)
del(A[0])
print('After change:', A)
print('hard rock'.split())
print('A,B,C,D'.split(","))
A = ["disco", 10, 1.2]
B = A
print(A)
print(B)
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# clone list A
B = A[:]
print(A)
print(B)

# now change A without changing B
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
