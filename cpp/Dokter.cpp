// Kelas turunan pertama yang menambahkan data profesi dokter
#ifndef DOKTER_CPP
#define DOKTER_CPP

#include "Manusia.cpp"

class Dokter : public Manusia {
private:
    std::string str;
    long long gaji_pokok;
    std::string rumah_sakit;
    inline static int str_counter = 1000;

    static std::string generateStrOtomatis() {
        // Counter static dipakai bersama oleh seluruh objek Dokter
        return "STR-" + std::to_string(++str_counter);
    }

public:
    Dokter(const std::string& nama, int umur, const std::string& gender,
           long long gaji_pokok, const std::string& rumah_sakit)
        : Manusia(nama, umur, gender), str(generateStrOtomatis()),
          gaji_pokok(gaji_pokok), rumah_sakit(rumah_sakit) {
                // Gaji diperiksa setelah bagian Manusia selesai dibuat
        if (gaji_pokok < 0) {
            throw std::invalid_argument("Gaji pokok tidak boleh minus");
        }
    }

    const std::string& getStr() const { return str; }
    long long getGajiPokok() const { return gaji_pokok; }
    const std::string& getRumahSakit() const { return rumah_sakit; }

    void informasiDokter() const {
        std::cout << getStr() << '\n';
        informasi();
        std::cout << getGajiPokok() << '\n' << getRumahSakit() << '\n';
    }
};

#endif
