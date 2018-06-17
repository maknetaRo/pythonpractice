""" Write a program that takes any two lists L and M of the same size and adds
their elements together to form a new list N whose elements are sums of the
corresponding elements in L and M. For instance, if L=[3,1,4] and M=[1, 5, 9],
then N should equal [4, 6, 13]. """
L = [3, 1, 4]
M = [1, 5, 9]
N = [x + y for x, y in zip(L, M)]
print(N)
N = [sum(pair) for pair in zip(L, M)]
print(N)
