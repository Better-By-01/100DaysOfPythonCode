# Random (module)
# use askpython documentation
import random
import my_module

random_integer = random.randint(1,10)      # 1 and 10 inclusive
print(f"Random Number b/w 1 and 10: {random_integer}")

print(f"From my_module pi = {my_module.pi}")

# for random floating values between [0,1)
random_float = random.random()
print(f"Random float no.: {'{:.4f}'.format(random_float)}")

# random floating num. between [0,5) 0.00000... to 4.99999...
print(f"Random floating no. between [0,5): {'{:.4}'.format(random_float*5)}")

# random floating num. between [0,5] 0.00000... to 5.00000...
a = 0
b = 5
random_nu = '{:.4}'.format(random.randint(a,b) + (random.random()))
print(f"Random number between {a} and {b}: {random_nu}")

