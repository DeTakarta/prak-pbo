from datetime import date

class worker:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    @classmethod
    def dari_tahun_lahir(cls, nama, tahun):
        return cls(nama, date.today().year - tahun)

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur} tahun")

    def __del__(self):
        print(f"worker {self.nama} dipecat")

karyawan1 = worker("Shihap", 19)
karyawan2 = worker.dari_tahun_lahir("Giren", 1990)

karyawan1.tampilkan_info()
karyawan2.tampilkan_info()

del karyawan1