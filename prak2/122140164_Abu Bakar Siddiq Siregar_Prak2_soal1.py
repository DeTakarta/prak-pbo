class Mahasiswa:
    def __init__(self, NIM, nama, angkatan, isMahasiswa=True):
        self._nim = NIM
        self._nama = nama
        self._angkatan = angkatan
        self._isMahasiswa = isMahasiswa

    def getNim(self):
        return self._nim

    def setNim(self, nim):
        self._nim = nim

    def getNama(self):
        return self._nama

    def setNama(self, nama):
        self._nama = nama

    def hitungNilaiAkhir(self, nilai):
        return nilai * 2

    def isAktif(self):
        return self._isMahasiswa

    def hitungSemester(self, tahun_sekarang):
        return tahun_sekarang - self._angkatan + 1

mahasiswa1 = Mahasiswa(NIM="12345", nama="John Doe", angkatan=2020, isMahasiswa=True)

mahasiswa2 = Mahasiswa(NIM="67890", nama="Jane Doe", angkatan=2019)

nilai_mahasiswa1 = mahasiswa1.hitungNilaiAkhir(80)
print(f"Nilai Akhir Mahasiswa 1: {nilai_mahasiswa1}")

status_mahasiswa1 = "Aktif" if mahasiswa1.isAktif() else "Tidak Aktif"
print(f"Status Mahasiswa 1: {status_mahasiswa1}")

semester_mahasiswa2 = mahasiswa2.hitungSemester(2024)
print(f"Semester Mahasiswa 2: {semester_mahasiswa2}")
