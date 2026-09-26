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
        super().__init__(nama, umur, gender, gaji_pokok, rumah_sakit)
        self.setSpesialisasi(spesialisasi)
        self.setSpesialisasiTarif(spesialisasi_tarif)
        self.setGelarSpesialis(gelar_spesialis)

    #setter 
    def setSpesialisasi(self, spesialisasi):
        if (spesialisasi == "") :
            print("Spesialisasi tidak boleh kosong")
            return
        self.__spesialisasi = spesialisasi

    def setSpesialisasiTarif(self, spesialisasi_tarif):
        if (spesialisasi_tarif < 0) :
            print("Tarif spesialisasi tidak boleh minus")
            return
        self.__spesialisasi_tarif = spesialisasi_tarif

    def setGelarSpesialis(self, gelar_spesialis) :
        if (gelar_spesialis == "") :
            print("Gelar spesialis tidak boleh kosong")
            return
        self.__gelar_spesialis = gelar_spesialis

    #getter
    def getSpesialis(self):
        return self.__spesialisasi

    def getSpesialisasiTarif(self):
        return self.__spesialisasi_tarif

    def getGelarSpesialis(self):
        return self.__gelar_spesialis

    def informasiDokterSpesialis(self) :
        print(self.getNoRegis())
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())
        print(self.getGajiPokok())
        print(self.getSpesialis())
        print(self.getSpesialisasiTarif())
        print(self.getGelarSpesialis())
        print(self.getRumahSakit())