import math
n = input('enter n')
r = input('enter r')
n = int(n)
r = int(r)
n_frac = math.factorial(int(n))
nr_frac = math.factorial(int(n-r))
r_frac = math.factorial(int(r))

denon = r_frac*nr_frac
combination = n_frac/denon
print(combination)
