# Kelas turunan pertama yang menambahkan data profesi dokter
from Manusia import Manusia

class Dokter(Manusia):
    _nomor_regis_counter = 1000

    def __init__(self, nama, umur, gender, gaji_pokok, rumah_sakit):
        # Inisialisasi bagian manusia terlebih dahulu melalui pewarisan
        super().__init__(nama, umur, gender)
        # Data pekerjaan diisi melalui setter milik kelas Dokter
        self.setGajiPokok(gaji_pokok)
        self.setRumahSakit(rumah_sakit)
        # Nomor registrasi dibuat otomatis dan bersifat unik antar objek
        self.__nomor_regis = self.generateStrOtomatis()

    def generateStrOtomatis(self):
        # Atribut class membuat nomor registrasi terus bertambah antar objek
        Dokter._nomor_regis_counter += 1
        return "STR-" + str(Dokter._nomor_regis_counter)

    def setGajiPokok(self, gaji_pokok):
        if gaji_pokok < 0:
            raise ValueError("Gaji pokok tidak boleh minus")
        self.__gaji_pokok = gaji_pokok

    def setRumahSakit(self, rumah_sakit):
        self.__rumah_sakit = rumah_sakit

    def getStr(self):
        return self.__nomor_regis

    def getNoRegis(self):
        return self.getStr()

    def getGajiPokok(self):
        return self.__gaji_pokok

    def getRumahSakit(self):
        return self.__rumah_sakit

    def informasiDokter(self):
        print(self.getStr())
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())
        print(self.getGajiPokok())
        print(self.getRumahSakit())
