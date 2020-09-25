import math
class Funtions():
    def sum_complex(c1, c2):
        x1 = []
        a = c1[0] + c2[0]
        b = c1[1] + c2[1]
        x1.append(a)
        x1.append(b)
        return x1

    def subt_complex(c1, c2):
        x2 = []
        a = c1[0] - c2[0]
        b = c1[1] - c2[1]
        x2.append(a)
        x2.append(b)
        return x2

    def mult_complex(c1, c2):
        x3 = []
        a = c1[0]*c2[0] - c1[1]*c2[1]
        b = c1[0]*c2[1] + c2[0]*c1[1]
        x3.append(a)
        x3.append(b)
        return x3

    def div_complex(c1, c2):
        x4 = []
        den = (mod_complex(c2))**2
        if den == 0:
            raise ValueError('No es posible dividir por cero')
        else:
            a = (c1[0]*c2[0] + c2[1]*c2[1])/den
            b = (c2[0]*c1[1] - c1[0]*c2[1])/den
            x4.append(a)
            x4.append(b)
        return x4

    def mod_complex(c):
        mod_c = math.sqrt(a[0]**2+a[1]**2)
        return mod_c

    def conj_complex(c):
        c[1] = c[1]*-1
        return c

    def polar(cc):
        x5 = []
        p = mod_complex(cc)
        ang = math.atan2(cc[1], cc[0])
        x5.append(p)
        x5.append(ang)
        return x5

    def carte(pc):
        x6 = []
        a = pc[0] * math.cos(pc[1])
        b = pc[0] * math.sin(pc[1])
        x6.append(a)
        x6.append(b)
        return x6
    
