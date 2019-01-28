number1 = int(input('Ketik angka pertama        : '))
number2 = int(input('Ketik angka kedua          : '))

def fpb(no1,no2):
    angkaFpb = 0
    if no1 > no2:
        kecil = no2
    else:
        kecil = no1

    for urutan in range(1,kecil+1):
        if no1 % urutan == 0 and no2 % urutan == 0:
            angkaFpb = urutan

    print('FPB dari',no1,'dan',no2,'adalah  :',angkaFpb)

def kpk(no1,no2):
    angkaKpk = 0
    if no1 > no2:
        besar = no1
    else:
        besar = no2

    while True:
        if besar % no1 == 0 and besar % no2 == 0:
            angkaKpk = besar
            break
        besar += 1

    print('KPK dari',no1,'dan',no2,'adalah  :',angkaKpk)

fpb(number1,number2)
kpk(number1,number2)