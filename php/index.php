<?php

session_start();
require_once __DIR__ . '/DokterSpesialis.php';

// Lima objek awal dibuat sebelum halaman ditampilkan
$dokterAwal = [
    ['Asep', 35, 'Pria', 40000000, 'Hasan Sadikin', 'Jantung', 500000, 'Sp.Jp'],
    ['Ahmad', 36, 'Pria', 30000000, 'Hasan Sadikin', 'Penyakit Dalam', 300000, 'Sp.PD'],
    ['Udin', 37, 'Pria', 30000000, 'Hasan Sadikin', 'Anak', 350000, 'Sp.A'],
    ['Ucup', 38, 'Pria', 40000000, 'Hasan Sadikin', 'Kandungan', 450000, 'Sp.OG'],
    ['Ancika', 25, 'Wanita', 35000000, 'Pindad', 'Saraf', 400000, 'Sp.Jp'],
];

// Session menyimpan daftar selama browser masih memakai session yang sama
if (!isset($_SESSION['daftarDokter'])) {
    $_SESSION['daftarDokter'] = array_map(
        fn(array $data): DokterSpesialis => new DokterSpesialis(...$data),
        $dokterAwal
    );
}

$daftarDokter = &$_SESSION['daftarDokter'];
$pesan = '';
$jenisPesan = '';

// Form PHP menerima satu dokter tambahan per submit agar frontend tetap sederhana
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['reset'])) {
        // Tombol reset menghapus data tambahan dan mengembalikan data awal
        unset($_SESSION['daftarDokter']);
        header('Location: ' . $_SERVER['PHP_SELF']);
        exit;
    }

    try {
        // Nilai form dibersihkan sebelum dikirim ke constructor
        $dataForm = [
            trim($_POST['nama'] ?? ''), (int) ($_POST['umur'] ?? 0), trim($_POST['gender'] ?? ''),
            (int) ($_POST['gaji'] ?? 0), trim($_POST['rumah_sakit'] ?? ''),
            trim($_POST['spesialisasi'] ?? ''), (int) ($_POST['tarif'] ?? 0), trim($_POST['gelar'] ?? ''),
        ];
        $daftarDokter[] = new DokterSpesialis(...$dataForm);
        $pesan = 'Data dokter berhasil ditambahkan';
        $jenisPesan = 'success';
    } catch (InvalidArgumentException $error) {
        // Pesan validasi ditampilkan kembali di halaman agar kesalahan mudah diperbaiki
        $pesan = $error->getMessage();
        $jenisPesan = 'error';
    }
}
?>
<!doctype html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <title>Daftar Dokter Spesialis</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main class="container">
        <header class="page-header">
            <p class="eyebrow">Sistem Data Klinik</p>
            <h1>Daftar Dokter Spesialis</h1>
            <p>Kelola data dokter dengan PHP dan multilevel inheritance</p>
        </header>
        <?php if ($pesan !== ''): ?>
            <div class="alert <?= htmlspecialchars($jenisPesan) ?>">
                <?= htmlspecialchars($pesan) ?>
            </div>
        <?php endif; ?>

        <section class="table-section">
            <div class="section-heading">
                <div>
                    <p class="eyebrow">Data aktif</p>
                    <h2>Dokter terdaftar</h2>
                </div>
                <span class="count"><?= count($daftarDokter) ?> dokter</span>
            </div>
    <!-- Tabel menampilkan seluruh objek dalam daftar dokter -->
    <div class="table-wrapper"><table>
        <thead><tr>
            <th>Surat Tanda Registrasi</th><th>Nama</th><th>Umur</th><th>Gender</th>
            <th>Gaji Pokok</th><th>Spesialisasi</th><th>Spesialisasi Tarif</th>
            <th>Gelar Spesialis</th><th>Rumah Sakit</th>
        </tr></thead>
        <tbody>
        <?php foreach ($daftarDokter as $dokter): ?>
            <!-- Setiap objek menghasilkan satu baris tabel -->
            <tr>
                <td><?= htmlspecialchars($dokter->getStr()) ?></td>
                <td><?= htmlspecialchars($dokter->getNama()) ?></td>
                <td><?= $dokter->getUmur() ?></td>
                <td><?= htmlspecialchars($dokter->getGender()) ?></td>
                <td><?= $dokter->getGajiPokok() ?></td>
                <td><?= htmlspecialchars($dokter->getSpesialisasi()) ?></td>
                <td><?= $dokter->getSpesialisasiTarif() ?></td>
                <td><?= htmlspecialchars($dokter->getGelarSpesialis()) ?></td>
                <td><?= htmlspecialchars($dokter->getRumahSakit()) ?></td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table></div>
        </section>

    <section class="form-section">
        <div class="section-heading">
            <div>
                <p class="eyebrow">Input data</p>
                <h2>Tambah Dokter</h2>
            </div>
        </div>
    <!-- Form mengumpulkan delapan nilai yang dibutuhkan constructor -->
    <form method="post">
        <label>Nama<input name="nama" placeholder="Contoh: Asep" required></label>
        <label>Umur<input name="umur" type="number" min="1" placeholder="35" required></label>
        <label>Gender<input name="gender" placeholder="Pria atau Wanita" required></label>
        <label>Gaji pokok<input name="gaji" type="number" min="0" placeholder="40000000" required></label>
        <label>Rumah sakit<input name="rumah_sakit" placeholder="Hasan Sadikin" required></label>
        <label>Spesialisasi<input name="spesialisasi" placeholder="Jantung" required></label>
        <label>Tarif spesialisasi<input name="tarif" type="number" min="0" placeholder="500000" required></label>
        <label>Gelar spesialis<input name="gelar" placeholder="Sp.Jp" required></label>
        <div class="form-actions">
            <button class="primary" type="submit">Tambah data</button>
        </div>
    </form>
    <form method="post" class="reset-form">
        <button class="secondary" type="submit" name="reset" value="1">Kembalikan data awal</button>
    </form>
    </section>
    </main>
</body>
</html>
