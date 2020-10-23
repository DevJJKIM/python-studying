# Chater03-6
# 집합(set)특징
# 집합(set) 자료형 (순서x, 중복 허용x, 추가0, 삭제0)

#선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'pen', 'cap', 'plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}              #키가 없이 원소만 있으면 집합형임
f = {42, 'foo', (1,2,3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)    # 중복을 허용 하지 않음.
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

#Expected Output
# a -  <class 'set'> set()
# b -  <class 'set'> {1, 2, 3, 4}
# c -  <class 'set'> {1, 4, 5, 6}
# d -  <class 'set'> {1, 2, 'plate', 'cap', 'pen'}
# e -  <class 'set'> {'foo', 'qux', 'bar', 'baz'}
# f -  <class 'set'> {3.14159, 'foo', 42, (1, 2, 3)}

#튜플변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)

#Expected Ouput
# t -  <class 'tuple'> (1, 2, 3, 4)

#리스트변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l - ', l2)

#Expected Output
# l -  [1, 4, 5, 6]
# l -  ['baz', 'qux', 'bar', 'foo']

#길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
#Expected Output
# 0
# 4
# 4
# 5
# 4
# 4

#집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2', s1 & s2)               # s1,s2 교집합
print('s1 & s2', s1.intersection(s2))   # s1,s2 교집합
print('s1 | s2', s1 | s2)               # s1,s2 합집합
print('s1 | s2', s1.union(s2))          # s1,s2 합집합
print('s1 | s2', s1 - s2)               # s1,s2 차집합
print('s1 | s2', s1.difference(s2))     # s1,s2 차집합

#Expected Output
# s1 & s2 {4, 5, 6}
# s1 & s2 {4, 5, 6}
# s1 | s2 {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s1 | s2 {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s1 | s2 {1, 2, 3}
# s1 | s2 {1, 2, 3}

#중복 원소 확인
print('s1 & s2 ', s1.isdisjoint(s2))        #False가 되면 교집합 있다는 뜻

#Expected Output
# s1 & s2  False

# 부분집합 확인
print(s1.issubset(s2))  # 부분집합 관계를 확인
print(s1.issuperset(s2))

#Expected Output
# False
# False

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
s1.remove(2)
print('s1 - ', s1)
s1.discard(3)
print('s1 - ', s1)
# s1.remove(7)      #remove 없는 값을 삭제 하면 에러 발생
# s1.discard(7)     #discard 없는 값을 삭제하면 에러 발생 안함.

s1.clear()          #전부다 삭제
print('s1 - ', s1)

