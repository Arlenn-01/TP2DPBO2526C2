// Kelas dasar yang menyimpan identitas umum setiap manusia
#ifndef MANUSIA_CPP
#define MANUSIA_CPP

#include <iostream>
#include <stdexcept>
#include <string>

class Manusia {
private:
    std::string nama;
    int umur;
    std::string gender;

public:
    Manusia(const std::string& nama, int umur, const std::string& gender)
        : nama(), umur(0), gender() {
        // Setter dipanggil dari constructor agar data awal langsung divalidasi
        setNama(nama);
        setUmur(umur);
        setGender(gender);
    }

    void setNama(const std::string& nilai) {
        // Nama kosong tidak diperbolehkan oleh aturan kelas dasar
        if (nilai.empty()) {
            throw std::invalid_argument("Nama tidak boleh kosong");
        }
        nama = nilai;
    }

    void setUmur(int nilai) {
        // Umur harus lebih besar dari nol agar data manusia valid
        if (nilai <= 0) {
            throw std::invalid_argument("Masukkan umur dengan benar");
        }
        umur = nilai;
    }

    void setGender(const std::string& nilai) { gender = nilai; }
    const std::string& getNama() const { return nama; }
    int getUmur() const { return umur; }
    const std::string& getGender() const { return gender; }

    virtual void informasi() const {
        std::cout << getNama() << '\n' << getUmur() << '\n' << getGender() << '\n';
    }
};

#endif
