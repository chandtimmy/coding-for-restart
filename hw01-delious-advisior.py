# 구현 내용
#
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트
#
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.
# 마감시간
#
# 이번 주 일요일 24:00
import random

today = input("1.한식,2.일식,3.중식+중 번호를 눌러주세요~ ")


if today == "1":
    today_List = ['김치', '된장찌개', '육개장']
    print(random.choice(today_List))
if today == "2":
    today_List = ['연어초밥', '참치초밥', '돈부리']
    print(random.choice(today_List))
if today == "3":
    today_List = ['사천볶음밥', '짬뽕', '탕수육']
    print(random.choice(today_List))

# 수시간의 시행착오..
    # randomList = getRandom(korean,1)
#

        # from random import randrange
        # random_index = randrange (0,len(korean))
        # print_korean[random_index]


# title1 = "메뉴"
# menu1="한식"
# list1=['김치', '된장찌개', '육개장']
# title2 = "메뉴"
# menu2="일식"
# list2=
# title3 = "메뉴"
# menu3=("중식")
# list3=
# choice = menu1,menu2,menu3
# input(choice + "중 어느 것으로 할래요?")
# print(input(choice + "중 어느 것으로 할래요?"))
    # for choice in menu1:
    #     import random
    #     한식 = ['김치', '된장찌개', '육개장']
    #     secure_random = random.SystemRandom()
    #     print(secure_random.choice(한식))
    #
    # for menu in range ("일식"):
    #     import random
    #     일식 = ['연어초밥', '참치초밥', '돈부리']
    #     secure_random = random.SystemRandom()
    #     print(secure_random.choice(일식))
    #
    # for menu in range ("중식"):
    #     import random
    #     중식 = ['사천볶음밥', '짬뽕', '탕수육']
    #     secure_random = random.SystemRandom()
    #     print(secure_random.choice(중식))
