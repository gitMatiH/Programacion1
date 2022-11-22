
def factorial(numero):
    i = numero
    productoria = 1
    print(productoria)
    while i > 0:
        productoria = productoria * (i)
        print(productoria)
        i = i-1
    return productoria


## test

num = 5
fact = factorial(num)
print(fact)

print()

fact = factorial(3)
print(fact)
