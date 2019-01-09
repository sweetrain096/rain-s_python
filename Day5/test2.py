import random


lotto = ", ".join(map(str, sorted(random.sample(range(1, 46), 6))))
print(lotto)