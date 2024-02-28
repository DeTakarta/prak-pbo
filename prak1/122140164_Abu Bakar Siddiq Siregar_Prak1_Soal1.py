Lower = int(input("batas bawah : "))
upper = int(input("batas atas  : "))
Total = 0

if (Lower <= 0 or upper <= 0):
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
else:
    for i in range(Lower, upper):
        if(i % 2 != 0):
            print(str(i))
            Total = Total + i
    print("Total : " + str(Total))
