

class Manusia :
    def __init__(self, nama, umur, gender) : 
        self.setNama(nama) #harus pakai prefix self kalau scopenya sama satu class
        self.setUmur(umur)
        self.__gender = gender

    #setter
    def setNama(self, nama) :
        if (nama == "") : 
            print("Nama tidak boleh kosong wok")
            return #early exit
        self.__nama = nama

    def setUmur(self, umur) :
        if (umur <= 0) :
            print("Masukkan umur dengan benar")
            return 
        self.__umur = umur

    def setGender(self, gender) :
        self.__gender = gender

    #getter
    def getNama(self) :
        return self.nama

    def getUmur(self) :
        return self.umur

    def getGender(self) :
        return self.gender

    def informasi(self) :
        print(self.getNama())
        print(self.getUmur())
        print(self.getGender())