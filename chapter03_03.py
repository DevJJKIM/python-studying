# chapter03-03
# 파이썬 리스트
# 자료구조에서 중요
# 리스트자료형(순서있고, 중복허용, 수정가능, 삭제 가능)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# Expected Output
# d -  <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captain']
# d -  10000
# d -  21000
# e -  Base
# e -  ['B', 'a', 's', 'e']

# 슬라이싱
print('>>>>>>')
print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])

#Expected Output
# d - [1000, 10000, 'Ace']
# d - ['Ace', 'Base', 'Captain']
# e - ['Base', 'Captain']

# 리스트 연산
print('>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print('Test + c[0]', 'Test' + str(c[0]))

# Expected Output
# c + d [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captain']
# c * 3 [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
# Test + c[0] Test70

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

#Expected Output
# [70, 75, 80, 85] [70, 75, 80, 85]
# 2407450002368
# 2407450002368

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

#Expected Output
# >>>>>>
# c -  [4, 75, 80, 85]
# c -  [4, 'a', 'b', 'c', 80, 85]
# c -  [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]
# c -  [4, 'c', 80, 85]
# c -  [4, 'c', 85]

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6]
# print('a - ', a)
a.remove(10)
print('a - ', a)
print('a - ', a.pop()) # 리스트의 마지막 값을 뺌
print('a - ', a)

print('a - ', a.pop())
print('a - ', a)

print('a - ', a.count(4)) #4가몇개있는지
ex = [8,9]
a.extend(ex)
print('a - ', a)
print()

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)

#Expeted Output
# a -  [5, 2, 3, 1, 4]
# a -  [5, 2, 3, 1, 4, 10]
# a -  [1, 2, 3, 4, 5, 10]
# a -  [10, 5, 4, 3, 2, 1]
# a -  3 3
# a -  [10, 5, 7, 4, 3, 2, 1]
# a -  [1, 2, 3, 4, 7, 5, 10]
# a -  [1, 2, 3, 4, 7, 5]
# a -  5
# a -  [1, 2, 3, 4, 7]
# a -  7
# a -  [1, 2, 3, 4]
# a -  1
# a -  [1, 2, 3, 4, 8, 9]