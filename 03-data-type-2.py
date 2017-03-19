# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print ("list")
list_a = [1, 2, 3]
print(list_a)
print (type([1.2,3]))
# index 는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
# slice 리스트를 자른다는 의미 : 2번째 자료까지, but 마지막은 출력 X
print(list_a[0:2])
list_a.append(4)
print(list_a)
list_a.remove(2)
print(list_a)
list_a.clear()
print(list_a)

# tuple (1,  )  숫자+쉼표+
print("tuple")
tuple_a=(1,2,3)
print(tuple_a)
print(type(tuple_a))
# tuple_a.append(4)    *tuple 은 append 기능 XX

# dict (map) {}
# key & value   {"key" : "value"}
dict_a = {
"apple" : "a type of fruits",
"pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value     *변경하고싶을 때
dict_a["pen"]= "something to write"
print(dict_a)

# set set([])     *중복이 자동으로 제거, 중복이 없음
set_a = set([1, 2, 3, 3, 3, 2])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 집합(set) - 교집합, 합집합, 차집합, 여집합
# 중복 제거
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
