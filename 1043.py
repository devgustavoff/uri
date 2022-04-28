a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if a + b > c and a + c > b and b + c > a:
    print('Perimetro = {}'.format(a + b + c))
else:
    print('Area = {}'.format((a + b) / 2 * c))