Finger = int(input("Jari-jari : "))

if(Finger < 0):
    print("jari-jari lingkarang tidak boleh negatif")
else:
    Luas = 3.14 * (Finger*Finger)
    keliling = 2 * 3.14 * Finger
    print("Luas : " + str(Luas))
    print("Keliling : " + str(keliling))