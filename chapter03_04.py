# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 즁요
# 튜플 자료형(순서0, 중복0, 수정x, 삭제x, 연산은 허용)

# 선언
a = ()
b = (1, ) #원소가 하나일때는 뒤에 콤마를 무조건 붙여줘야 함
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1]))       #List로 형변환

#Expected Output
# >>>>>
# d -  1000
# d -  2100
# d -  Captain
# d -  ('Ace', 'Base', 'Captain')
# d -  Base
# d -  ['B', 'a', 's', 'e']

# 수정안되는지 확인
# d[0] = 1500

# Exptected Output
# Traceback (most recent call last):
#   File "D:/python_basic/chapter03_04.py", line 32, in <module>
#     d[0] = 1500
# TypeError: 'tuple' object does not support item assignment


#슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

#튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

#튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) #3의 인덱스(위치값)은 어디냐
print('a - ', a.count(2)) #2의 개수는 몇개가 있냐..

# 팩킹 & 언팩킹
# 팩킹
t = ('foo', 'bar', 'baz', 'qux') #4개의 원소를 하나로 묶었다. 이걸 팩킹이라고 해. 인덱스로 접근이 가능하지

# 언팩킹(Unpacking)
(x1, x2, x3, x4) = t  # 각각 순서에 맞게 원소들을 대입시키는거
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# Exptected Ouput
# <class 'str'> <class 'str'> <class 'str'> <class 'str'>
# foo bar baz qux


# 팩킹 & 언팩킹1
t2 = 1, 2, 3            #괄호가 없어도 튜플선언이 됨.
t3 = 4,                 #괄호는 생략가능
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

#Expeted Ouput
# (1, 2, 3)
# (4,)
# 1 2 3
# 4 5 6

