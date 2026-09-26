
# Kelas dasar yang menyimpan identitas umum setiap manusia
class Manusia:
    def __init__(self, nama, umur, gender):
        # Constructor memakai setter agar validasi berlaku sejak objek dibuat
        self.setNama(nama)
        self.setUmur(umur)
        self.setGender(gender)

    # Setter dibuat terpisah agar aturan data tetap terpusat
    def setNama(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = nama

    def setUmur(self, umur):
        if umur <= 0:
            raise ValueError("Masukkan umur dengan benar")
        self.__umur = umur

    def setGender(self, gender):
        self.__gender = gender

    # Getter menjadi antarmuka yang dipakai kelas turunan dan tabel
    def getNama(self):
        return self.__nama

    def getUmur(self):
        return self.__umur

    def getGender(self):
        return self.__gender

    def informasi(self):
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())