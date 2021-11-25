# Marcellino Giovani Handoko Suwigjo Putro
# UG 11


import random
tipe = input("Masukkan tipe yang ingin anda coba : ")

r_n1 = random.randint(1,20)
a = r_n1
r_n2 = random.randint(1,20)
b = r_n2
r_n3 = random.randint(1,20)
c = r_n3
r_n4 = random.randint(1,20)
d = r_n4
options = ["<",">","=="]

r_o = random.randint(0,2)

c_pick = options[r_o]

def generatesoal():
	print("(benar/salah) jika", end=" ")

	if tipe.lower()=="pengurangan":
		print(r_n1,"-",r_n2,c_pick,r_n3,"-",r_n4, sep='')

	elif tipe.lower()=="penjumlahan":
		print(r_n1,"+",r_n2,c_pick,r_n3,"+",r_n4, sep='')

	else:
		print("hanya ada tipe pengurangan/penjumlahan")

generatesoal()
jawaban = input("Masukkan Jawaban Anda: ")


def cekHasil():
	if c_pick == "<" and tipe.lower() == "pengurangan":

		if ((a-b)<(c-d)) == True:

			if jawaban.lower() == "benar":

				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah !")
		else: 

			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
                
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == "<" and tipe.lower() == "penjumlahan":

		if ((a+b)<(c+d)) == True:

			if jawaban.lower() == "benar":
                
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
                
		else: 

			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah !")		

	elif c_pick == ">" and tipe.lower() == "pengurangan":

		if ((a-b)>(c-d)) == True:

			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah !")
		else: 

			if jawaban.lower() =="salah":

				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == ">" and tipe.lower() == "penjumlahan":

		if ((a+b)>(c+d)) == True:

			if jawaban.lower() == "benar":

				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah !")
		else: 

			if jawaban.lower() =="salah":

				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah!")	
	elif c_pick == "==" and tipe.lower() == "pengurangan":	

		if ((a-b)==(c-d)) == True:

			if jawaban.lower() == "benar":

				print("Jawaban Anda Benar !")
			else:

				print("Jawaban Anda Masih Salah !")
		else: 

			if jawaban.lower() =="salah":
                
				print("Jawaban Anda Benar !")

			else:

				print("Jawaban Anda Masih Salah !")

	elif c_pick == "==" and tipe.lower() == "penjumlahan":

		if ((a+b)==(c+d)) == True:

			if jawaban.lower() == "benar":

				print("Jawaban Anda Benar !")

			else:

				print("Jawaban Anda Masih Salah !")	

		else: 

			if jawaban.lower() =="salah":

				print("Jawaban Anda Benar !")

			else:

				print("Jawaban Anda Masih Salah !")

cekHasil()