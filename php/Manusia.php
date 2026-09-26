<?php
// Kelas dasar untuk data identitas manusia

class Manusia
{
    private string $nama;
    private int $umur;
    private string $gender;

    public function __construct(string $nama, int $umur, string $gender)
    {
        // Setter dipakai agar data awal langsung melewati validasi
        $this->setNama($nama);
        $this->setUmur($umur);
        $this->setGender($gender);
    }

    public function setNama(string $nama): void
    {
        // Nama kosong tidak boleh disimpan ke dalam objek
        if ($nama === '') {
            throw new InvalidArgumentException('Nama tidak boleh kosong');
        }
        $this->nama = $nama;
    }

    public function setUmur(int $umur): void
    {
        // Umur harus lebih besar dari nol
        if ($umur <= 0) {
            throw new InvalidArgumentException('Umur tidak valid');
        }
        $this->umur = $umur;
    }

    public function setGender(string $gender): void { $this->gender = $gender; }
    public function getNama(): string { return $this->nama; }
    public function getUmur(): int { return $this->umur; }
    public function getGender(): string { return $this->gender; }
}
