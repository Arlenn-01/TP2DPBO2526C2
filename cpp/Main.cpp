// Program utama untuk membuat data dokter dan mencetak tabel dinamis
#include "DokterSpesialis.cpp"
#include <algorithm>
#include <iomanip>
#include <limits>
#include <vector>

using Baris = std::vector<std::string>;

Baris dataBaris(const DokterSpesialis& dokter) {
    // Semua getter dikumpulkan menjadi urutan kolom tabel
    return {dokter.getStr(), dokter.getNama(), std::to_string(dokter.getUmur()),
            dokter.getGender(), std::to_string(dokter.getGajiPokok()),
            dokter.getSpesialisasi(), std::to_string(dokter.getSpesialisasiTarif()),
            dokter.getGelarSpesialis(), dokter.getRumahSakit()};
}

void cetakTabelDinamis(const std::vector<DokterSpesialis>& daftar) {
    // Header menentukan nama dan jumlah kolom yang akan dicetak
    const std::vector<std::string> header = {
        "Surat Tanda Registrasi", "Nama", "Umur", "Gender", "Gaji Pokok",
        "Spesialisasi", "Spesialisasi Tarif", "Gelar Spesialis", "Rumah Sakit"};
    // Baris disimpan sebagai string agar angka dan teks dapat diproses seragam
    std::vector<Baris> rows;
    std::vector<std::size_t> widths;
    // Lebar awal diambil dari panjang setiap header
    for (const auto& kolom : header) widths.push_back(kolom.size());
    for (const auto& dokter : daftar) {
        // Setiap objek diubah menjadi baris lalu dibandingkan dengan lebar saat ini
        rows.push_back(dataBaris(dokter));
        for (std::size_t i = 0; i < widths.size(); ++i)
                // Kolom mengikuti nilai terpanjang antara header dan data
                widths[i] = std::max(widths[i], rows.back()[i].size());
    }

            // Border dibuat berdasarkan lebar final setiap kolom
    std::string border = "+";
    for (const auto width : widths) border += std::string(width + 2, '-') + "+";
    auto cetakBaris = [&](const Baris& row) {
        // setw dan left menjaga isi setiap kolom tetap rata dan sejajar
        std::cout << "|";
        for (std::size_t i = 0; i < row.size(); ++i)
            std::cout << ' ' << std::left << std::setw(static_cast<int>(widths[i])) << row[i] << " |";
        std::cout << '\n';
    };
    std::cout << border << '\n';
    cetakBaris(header);
    std::cout << border << '\n';
    for (const auto& row : rows) cetakBaris(row);
    std::cout << border << '\n';
}

DokterSpesialis bacaDokter() {
    // Delapan variabel berikut mengikuti urutan input yang digunakan Java
    std::string nama, gender, rumah_sakit, spesialisasi, gelar;
    int umur;
    long long gaji, tarif;
    // getline dipakai untuk teks karena nama dan rumah sakit dapat mengandung spasi
    std::getline(std::cin, nama);
    std::cin >> umur; std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, gender);
    std::cin >> gaji; std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, rumah_sakit);
    std::getline(std::cin, spesialisasi);
    std::cin >> tarif; std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, gelar);
    // Semua input digabung menjadi satu objek dokter spesialis
    return DokterSpesialis(nama, umur, gender, gaji, rumah_sakit, spesialisasi, tarif, gelar);
}

int main() {
    // Lima objek awal dibuat sama seperti pada implementasi Java
    std::vector<DokterSpesialis> daftar = {
        {"Asep", 35, "Pria", 40000000, "Hasan Sadikin", "Jantung", 500000, "Sp.Jp"},
        {"Ahmad", 36, "Pria", 30000000, "Hasan Sadikin", "Penyakit Dalam", 300000, "Sp.PD"},
        {"Udin", 37, "Pria", 30000000, "Hasan Sadikin", "Anak", 350000, "Sp.A"},
        {"Ucup", 38, "Pria", 40000000, "Hasan Sadikin", "Kandungan", 450000, "Sp.OG"},
        {"Ancika", 25, "Wanita", 35000000, "Pindad", "Saraf", 400000, "Sp.Jp"}};
    // Tabel pertama dicetak sebelum pengguna menambahkan data
    cetakTabelDinamis(daftar);
    std::string jawaban;
    std::cout << "Mau nambah data? (yes/no) "; std::getline(std::cin, jawaban);
    if (jawaban == "yes" || jawaban == "Yes" || jawaban == "YES") {
        // Jumlah menentukan berapa kali fungsi pembacaan dipanggil
        int jumlah;
        std::cout << "Berapa banyak data? "; std::cin >> jumlah;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Silakan masukkan data sesuai format\n";
        for (int i = 0; i < jumlah; ++i) {
            // Setiap objek baru dimasukkan ke vector daftar dokter
            daftar.push_back(bacaDokter());
        }
    }
    // Tabel kedua memuat data awal dan data tambahan
    cetakTabelDinamis(daftar);
}
