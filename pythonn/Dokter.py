from Manusia import Manusia

class Dokter(Manusia):
    _nomor_regis_counter = 1000 #static protected, ga pake private nanti pusing namling 

    def __init__(self, nama, umur, gender, gaji_pokok, rumah_sakit) :
        #isi construct parent class
        super().__init__(nama, umur, gender) 
        self.setGajiPokok(gaji_pokok)
        self.setRumahSakit(rumah_sakit)

        self.__nomor_regis = self.generateStrOtomatis()

    def generateStrOtomatis(self) :
        #Dokter karena static milik class, bukan instance
        Dokter._nomor_regis_counter += 1
        return "STR-" + str(Dokter._nomor_regis_counter) #str mengubah int ke string 

    #setter
    def setGajiPokok(self, gaji_pokok) :
        if (gaji_pokok <= 0) :
            print("Harus punya gaji")
            return
        self.__gaji_pokok = gaji_pokok

    def setRumahSakit(self, rumah_sakit) :
        self.__rumah_sakit = rumah_sakit

    #getter
    def getNoRegis(self) :
        return self.__nomor_regis
    
    def getGajiPokok(self) :
        return self.__gaji_pokok

    def getRumahSakit(self) :
        return self.__rumah_sakit

    def informasiDokter(self) :
        print(self.getNoRegis())
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())
        print(self.getGajiPokok())
        print(self.getRumahSakit())
