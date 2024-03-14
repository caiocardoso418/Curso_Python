import math
co = float(input('qual a medida do cateto oposto:'))
ca = float(input('qual a medida do cateto adjacente:'))
hi = math.hypot(co, ca)
print('a valo da hipotenusa é {:.3f}'.format(hi))