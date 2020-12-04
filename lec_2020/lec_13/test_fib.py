from lec_2020.lec_13.fib import *

all_correct = True
for n, answer in [(0, 0), (1, 1), (2, 1), (5, 5)]:
    result = fib(n)
    correct = (result == answer)
    if not correct:
        print('Test case failed:', result, '!=', n, answer)
    all_correct &= correct

if all_correct:
    print('Testing fib(): OK')
else:
    print('Testing fib(): Failed')
