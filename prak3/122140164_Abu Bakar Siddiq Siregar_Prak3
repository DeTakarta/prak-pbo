class Dagangan:
    _jumlah_barang = 0
    _list_barang = []

    def __init__(self, nama, stok, harga):
        self._nama = nama
        self._stok = stok
        self._harga = harga

        Dagangan._jumlah_barang += 1
        Dagangan._list_barang.append({
            'nama': self._nama,
            'stok': self._stok,
            'harga': self._harga
        })

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls._jumlah_barang} buah")
        for index, barang in enumerate(cls._list_barang, start=1):
            print(f"{index}. {barang['nama']} seharga Rp {barang['harga']} (stok: {barang['stok']})")

    def __del__(self):
        for index, barang in enumerate(Dagangan._list_barang):
            if barang['nama'] == self._nama:
                del Dagangan._list_barang[index]
                Dagangan._jumlah_barang -= 1
                print(f"{self._nama} dihapus dari toko!")
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()
