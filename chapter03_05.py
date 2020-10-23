# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복 허용x, 수정0,삭제0)
# 키와 밸류로 되어 있다.

# 선언방법
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '870514'}
b = {0 : 'Hello python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}

e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# Expetecd Output
# a -  <class 'dict'> {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}
# b -  <class 'dict'> {0: 'Hello python'}
# c -  <class 'dict'> {'arr': [1, 2, 3, 4]}
# d -  <class 'dict'> {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A', 'Status': True}
# e -  <class 'dict'> {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A', 'Status': True}
# f -  <class 'dict'> {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A', 'Status': True}

# 출력
print('a - ', a['name'])        # 키가 존재 하지 않으면 에러 발생
print('a - ', a.get('name'))    # 키가 존재 하지 않으면 None으로 처리됨. 에러 처리가 용이
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

#딕셔너리추가
a['adress'] = 'seoul'

print('a - ', a)

#Expeted Ouput
# a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '870514', 'adress': 'seoul'}

a['rank'] = [1,2,3]
print('a - ', a)
#Expeted Ouput
# a -  {'name': 'Kim', 'phone': '01033337777', 'birth': '870514', 'adress': 'seoul', 'rank': [1, 2, 3]}

print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

#Exptected Output
# a -  5
# b -  1
# c -  1
# d -  5

# 딕셔너리 함수
# dict_kyes, dict_values, dict_items : 반복문(__iter__)에서 사용 가능..

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))

print('a - ', a.items())
print('a - ', b.items())
print('a - ', list(a.items()))
print('a - ', list(b.items()))

print('a - ', a.pop('name'))
print('a -', a)
#Expected Ouput
# a -  Kim
# a - {'phone': '01033337777', 'birth': '870514', 'adress': 'seoul', 'rank': [1, 2, 3]}


print('c - ', c.pop('arr'))
print('c - ', c)
#Expected Ouput
# c -  [1, 2, 3, 4]
# c -  {}

print('f - ', f.popitem()) #임의의 키와 밸류를 호출하고 삭제
print('f - ', f)
#Expected Ouput
# f -  ('Status', True)
# f -  {'Name': 'Niceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A'}

print('a - ', 'birth' in a)  # 'birth'라는 키가 있는지를 조회
print('d - ', 'City' in d)
#Expected Ouput
# a -  True
# d -  True

# 수정
a.update(birth = '910904')
print('a - ', a)

temp = {'adress' : 'Busan'}
a.update(temp)
print('a - ', a)