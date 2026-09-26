# Kelas turunan kedua yang menambahkan data spesialisasi dokter
from Dokter import Dokter

class DokterSpesialis(Dokter):
    def __init__(
        self,
        nama,
        umur,
        gender,
        gaji_pokok,
        rumah_sakit,
        spesialisasi,
        spesialisasi_tarif,
        gelar_spesialis
    ):
        # Constructor meneruskan data umum dan data pekerjaan ke parent class
        super().__init__(nama, umur, gender, gaji_pokok, rumah_sakit)
        # Data khusus dokter spesialis diisi setelah constructor parent selesai
        self.setSpesialisasi(spesialisasi)
        self.setSpesialisasiTarif(spesialisasi_tarif)
        self.setGelarSpesialis(gelar_spesialis)

    # Setter menjaga data spesialis tetap valid
    def setSpesialisasi(self, spesialisasi):
        if not spesialisasi:
            raise ValueError("Spesialisasi tidak boleh kosong")
        self.__spesialisasi = spesialisasi

    def setSpesialisasiTarif(self, spesialisasi_tarif):
        if spesialisasi_tarif < 0:
            raise ValueError("Tarif spesialisasi tidak boleh minus")
        self.__spesialisasi_tarif = spesialisasi_tarif

    def setGelarSpesialis(self, gelar_spesialis) :
        if not gelar_spesialis:
            raise ValueError("Gelar spesialis tidak boleh kosong")
        self.__gelar_spesialis = gelar_spesialis

    # Nama getter disamakan dengan implementasi Java
    def getSpesialisasi(self):
        return self.__spesialisasi

    def getSpesialis(self):
        return self.getSpesialisasi()

    def getSpesialisasiTarif(self):
        return self.__spesialisasi_tarif

    def getGelarSpesialis(self):
        return self.__gelar_spesialis

    def informasiDokterSpesialis(self) :
        print(self.getStr())
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())
        print(self.getGajiPokok())
        print(self.getSpesialisasi())
        print(self.getSpesialisasiTarif())
        print(self.getGelarSpesialis())
        print(self.getRumahSakit())