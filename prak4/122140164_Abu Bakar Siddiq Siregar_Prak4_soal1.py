class Hewan:
    def __init__(self, nama, kelamin):
        self.nama = nama
        self.kelamin = kelamin
        
    def makan(self):
        print(f"{self.__class__.__name__} {self.nama} sedang makan: tulang")
        
    def minum(self):
        print(f"{self.__class__.__name__} {self.nama} sedang minum: air")
    
class Kucing(Hewan):
    def __init__(self, nama, kelamin):
        super().__init__(nama, kelamin)
        self.urut = 0
        
    def bersuara(self):
        if self.urut == 0:
            print("kucing " + self.nama + "Bersuara : Meong!")
            self.urut = self.urut + 1
        elif self.urut == 1:
            super().makan()
            self.urut = self.urut + 1
        else:
            super().minum()
            self.urut = 0
     
class Anjing(Hewan):
    def __init__(self, nama, kelamin):
        super().__init__(nama, kelamin)
        self.urut = 0
        
    def bersuara(self):
        if self.urut == 0:
            print("Anjing " + self.nama + "Bersuara : Guk Guk!")
            self.urut = self.urut + 1
        elif self.urut == 1:
            super().makan()
            self.urut = self.urut + 1
        else:
            super().minum()
            self.urut = 0
         
        
hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

#contoh penggunaan 1

hewan1.bersuara()
hewan1.bersuara()
hewan2.bersuara()
hewan2.bersuara()

# contoh penggunaan 2
"""
hewan1.bersuara()
hewan1.bersuara()
hewan1.bersuara()
hewan2.bersuara()
hewan2.bersuara()
hewan2.bersuara() 
"""
