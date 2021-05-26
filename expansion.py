import math
n = input('enter the end term')
n = int(n)
for r in range(0,n):
    r = int(r)
    set = []
    set = [r]
    for a in set:
        xset = []
        yset = []
        nCr = []
        n_frac = math.factorial(int(n))
        na_frac = math.factorial(int(n - a))
        a_frac = math.factorial(int(a))
        denon = a_frac*na_frac
        C = n_frac/denon
        nCr = [C]
        print(C)
        xset = [n-a]
        yset = [a]
    for b in xset:
        for d in yset:
            for a in set:
                print('the', a, 'th term is ')
                print('Binomial coefficent =', C, 'x-index =', b, 'y-index = ', d)