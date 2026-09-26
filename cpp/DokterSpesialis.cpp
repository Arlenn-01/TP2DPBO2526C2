// Kelas turunan kedua yang menambahkan data spesialisasi dokter
#ifndef DOKTER_SPESIALIS_CPP
#define DOKTER_SPESIALIS_CPP

#include "Dokter.cpp"

class DokterSpesialis : public Dokter {
private:
    std::string spesialisasi;
    long long spesialisasi_tarif;
    std::string gelar_spesialis;

public:
    DokterSpesialis(const std::string& nama, int umur, const std::string& gender,
                    long long gaji_pokok, const std::string& rumah_sakit,
                    const std::string& spesialisasi, long long spesialisasi_tarif,
                    const std::string& gelar_spesialis)
        : Dokter(nama, umur, gender, gaji_pokok, rumah_sakit),
          spesialisasi(), spesialisasi_tarif(0), gelar_spesialis() {
                // Data khusus spesialis diisi setelah data Manusia dan Dokter siap
        setSpesialisasi(spesialisasi);
        setSpesialisasiTarif(spesialisasi_tarif);
        setGelarSpesialis(gelar_spesialis);
    }

    void setSpesialisasi(const std::string& nilai) {
        // Bidang spesialisasi wajib memiliki isi
        if (nilai.empty()) throw std::invalid_argument("Spesialisasi tidak boleh kosong");
        spesialisasi = nilai;
    }

    void setSpesialisasiTarif(long long nilai) {
        // Tarif tidak boleh bernilai negatif
        if (nilai < 0) throw std::invalid_argument("Tarif spesialisasi tidak boleh minus");
        spesialisasi_tarif = nilai;
    }

    void setGelarSpesialis(const std::string& nilai) {
        // Gelar spesialis wajib memiliki isi
        if (nilai.empty()) throw std::invalid_argument("Gelar spesialis tidak boleh kosong");
        gelar_spesialis = nilai;
    }

    const std::string& getSpesialisasi() const { return spesialisasi; }
    long long getSpesialisasiTarif() const { return spesialisasi_tarif; }
    const std::string& getGelarSpesialis() const { return gelar_spesialis; }
};

#endif
