#    과제 2 - 회사 조직도 만들기
#
# 구현 내용
#
# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
# 힌트
#
# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서, 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.
# 마감시간

name1 = "Tim"
race1 = "Human"
age1 = "32"
sex1 = "M"


name2 = "Hara"
race2 = "Human"
age2 = "52"
sex2 = "F"

name3 = "Ocram"
race3 = "Human"
age3 = "72"
sex3 = "M"

class Employee:
    race = "Human"

    def __init__(self, name, age, sex):
            self.name = name
            self.age = age
            self.sex = sex
    def race(self):
            self.Human

employee1 = Employee("Tim","32","M")
employee2 = Employee("Hara","52","F")
employee3 = Employee("Ocram","72","M")

print(employee1)

class NewEmployee(Employee):
    source = "대리"
#
    def __init__(self, name, age, sex)
            self.name = name
            self.age = age
            self.sex = sex

new_employee=NewEmployee("Soonoh","20","M""대리"")
print(new_employee.name)
print(new_employee.age)
print(new_employee.sex)
print(new_employee.source)






#상속
# class NewEmployee(Employee):
#     source="대리"
#
# new_person = NewEmployee("Soonoh","20","M")
# print(new_person.source)
# print(new_person.name)
# print(new_person.age)
# print(new_person.sex)



        # employee_position=NewEmployee("Soonh","20","M")
        # print("employee {}입니다. 저는{}세 건강한 {}입니다. 타이틀은 {}입니다")
