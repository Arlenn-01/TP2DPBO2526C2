<?php
// Kelas spesialis mewarisi data dokter dan menambahkan bidang keahlian

require_once __DIR__ . '/Dokter.php';

class DokterSpesialis extends Dokter
{
    private string $spesialisasi;
    private int $spesialisasiTarif;
    private string $gelarSpesialis;

    public function __construct(
        string $nama, int $umur, string $gender, int $gajiPokok, string $rumahSakit,
        string $spesialisasi, int $spesialisasiTarif, string $gelarSpesialis
    ) {
        // Data identitas dan pekerjaan diproses oleh constructor parent
        parent::__construct($nama, $umur, $gender, $gajiPokok, $rumahSakit);
        // Tiga setter berikut mengisi data khusus dokter spesialis
        $this->setSpesialisasi($spesialisasi);
        $this->setSpesialisasiTarif($spesialisasiTarif);
        $this->setGelarSpesialis($gelarSpesialis);
    }

    public function setSpesialisasi(string $nilai): void
    {
        // Spesialisasi wajib diisi agar informasi dokter lengkap
        if ($nilai === '') throw new InvalidArgumentException('Spesialisasi tidak boleh kosong');
        $this->spesialisasi = $nilai;
    }

    public function setSpesialisasiTarif(int $nilai): void
    {
        // Tarif konsultasi tidak boleh bernilai negatif
        if ($nilai < 0) throw new InvalidArgumentException('Tarif spesialisasi tidak boleh minus');
        $this->spesialisasiTarif = $nilai;
    }

    public function setGelarSpesialis(string $nilai): void
    {
        // Gelar spesialis wajib diisi
        if ($nilai === '') throw new InvalidArgumentException('Gelar spesialis tidak boleh kosong');
        $this->gelarSpesialis = $nilai;
    }

    public function getSpesialisasi(): string { return $this->spesialisasi; }
    public function getSpesialisasiTarif(): int { return $this->spesialisasiTarif; }
    public function getGelarSpesialis(): string { return $this->gelarSpesialis; }
}
