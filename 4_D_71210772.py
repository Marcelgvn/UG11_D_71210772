# Marcellino Giovani Handoko Suwigjo Putro
# UG 11

print("Untuk memulai program masukkan (-1) untuk mulai")
a = int(input(": "))

tebakan = 0

def tabakangka():

	global tebakan
	print("Apakah 4?")

	print("Apakah tebakan sudah benar ?")

	print("lebih < (0)")

	print("lebih > (1)")

	print("benar (2)")

	b = int(input(": "))
	tebakan += 1

	if b == 2:

		print("Jumlah tebakan : ", tebakan)

		print("Program Selesai !")

	elif b == 0:

		print("Apakah 2?")

		print("Apakah tebakan sudah benar ?")

		print("lebih < (0)")

		print("lebih > (1)")

		print("benar (2)")
        
		c = int(input(": "))
		tebakan += 1

		if c == 2:

			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")

		elif c == 0:

			print("Hasil Penjumlahannya Pasti 1 !")
			tebakan +=1

			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")
            
		elif c == 1:

			print("Hasil Penjumlahannya pasti 3 !")
			tebakan +=1

			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")
	elif b == 1:

		print("Apakah 6?")

		print("Apakah tebakan sudah benar ?")

		print("lebih < (0)")

		print("lebih > (1)")

		print("benar (2)")

		d = int(input(": "))
		tebakan += 1

		if d == 2:
			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")

		elif d == 0:

			print("Hasil Penjumlahannya Pasti 5 !")
			tebakan +=1

			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")

		elif d == 1:

			print("Hasil Penjumlahannya Pasti 7 !")
			tebakan +=1

			print("Jumlah tebakan :", tebakan)

			print("Program Selesai !")		

if a == -1 : 

	tabakangka()

else : 

	print("Program tidak berhasil dijalankan")