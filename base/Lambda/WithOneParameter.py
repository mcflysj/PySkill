# not recommended in PEP 8
powOfTwo = lambda power: pow(2.0, power)

pow8 = powOfTwo(8)


# pow8 is 256

# recommended
def pow_of_three(power):
    return pow(3.0, power)


pow3 = pow_of_three(3)
# pow3 is 27.0

print(pow8)
print(pow3)
