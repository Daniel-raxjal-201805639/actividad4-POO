num = int (input ("ingresa un número:"))
fac = 1.
for i in range (1, num + 1):
    fac = fac * i
print ("factorial de", num, "es", round(fac,0))