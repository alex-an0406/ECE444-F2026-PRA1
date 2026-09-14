from utils import utils

my_utils = utils()

#integer tests
print(my_utils.reversed(123)) #321
print(my_utils.formatter(10)) #0b1010, 0o12

try:
    print(my_utils.reversed(12.34))
except TypeError as e:
    print("Caught expected error for float:", e)

# 3. Test with strings (Invalid)
try:
    print(my_utils.formatter("123"))
except TypeError as e:
    print("Caught expected error for string:", e)