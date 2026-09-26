from Manusia import Manusia
from Dokter import Dokter
from DokterSpesialis import DokterSpesialis

manusia = Manusia("Arlen", 20, "pria")
manusia.informasi()

dokter1 = Dokter("Asep", 23, "pria", 9000000, "Pindad")
dokter1.informasiDokter()
print("===========")
dokter1 = Dokter("Ahmad Dhani", 23, "pria", 9000000, "Pindad")
dokter1.informasiDokter()

print("===========")
dokterSp = DokterSpesialis("Anjay", 30, "wanita", 10000000, "Pindad", "Jantung", 300000, "Sp.JP")
dokterSp.informasiDokterSpesialis()