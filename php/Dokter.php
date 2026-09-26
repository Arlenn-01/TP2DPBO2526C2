<?php
// Kelas dokter mewarisi identitas manusia dan memiliki data pekerjaan

require_once __DIR__ . '/Manusia.php';

class Dokter extends Manusia
{
    private string $str;
    private int $gajiPokok;
    private string $rumahSakit;
    private static int $strCounter = 1000;

    public function __construct(string $nama, int $umur, string $gender, int $gajiPokok, string $rumahSakit)
    {
        // Constructor parent mengisi data identitas manusia
        parent::__construct($nama, $umur, $gender);
        // Gaji divalidasi melalui setter sebelum disimpan
        $this->setGajiPokok($gajiPokok);
        $this->rumahSakit = $rumahSakit;
        // Counter static menghasilkan nomor registrasi unik untuk setiap objek
        $this->str = 'STR-' . (++self::$strCounter);
    }

    public function setGajiPokok(int $gajiPokok): void
    {
        // Gaji negatif tidak sesuai dengan aturan data dokter
        if ($gajiPokok < 0) {
            throw new InvalidArgumentException('Gaji pokok tidak boleh minus');
        }
        $this->gajiPokok = $gajiPokok;
    }

    public function getStr(): string { return $this->str; }
    public function getGajiPokok(): int { return $this->gajiPokok; }
    public function getRumahSakit(): string { return $this->rumahSakit; }
}
