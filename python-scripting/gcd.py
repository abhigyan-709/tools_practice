# implementing the HCF or GDC in python 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = gcd(10, 20)
print(gcd)