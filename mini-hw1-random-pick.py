# 랜덤뽑기
import random
Lotto = ['a', 'b', 'c', 'd', 'e']
secure_random = random.SystemRandom()
print(secure_random.choice(Lotto))
