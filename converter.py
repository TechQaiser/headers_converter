import os
x = int(input(" how many lines of headers to add "))
fil = input(" file to save path : ")
try:

    os.remove(fil)
except:
    pass
file = open(fil,"a")
print(" paste lines below ")
file.write("headers = {\n")
for i in range(x):
    xx = input()
    nk = xx.split(":")[0]
    bk2 = xx.split(":")[-1]
    first = f"'{nk}'"
    last = f"'{bk2}'"
    if i+1 == x:
        file.write('    '+first+str(":")+last+"}"+"\n")
    else:
        file.write('    ' + first + str(":")+last+","+"\n")
    # file.close()
