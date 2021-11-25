# Marcellino Giovani Handoko Suwigjo Putro
# UG 11

cekString = input("Masukkan String: ")

def check(integer):
    try:
        float(integer)
        return True
    except ValueError :
        return False

if cekString.isnumeric() or check(cekString) :
    cekString = float(cekString)
    if((int(cekString)) % 2) == 0:
        print(int(cekString/2))
    else:
        print(int(int(cekString + 5) / 2))
else:
    print(cekString [::-1])