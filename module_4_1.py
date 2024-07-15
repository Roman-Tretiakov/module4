from fake_math import divide as fake_div
from true_math import divide as true_div
import random


result1 = fake_div(random.randint(1, 100), random.randint(2, 10))
result2 = fake_div(random.randint(1, 100), 0)

result3 = true_div(random.randint(1, 100), random.randint(2, 10))
result4 = true_div(random.randint(1, 100), 0)

print(result1)
print(result2)
print(result3)
print(result4)
