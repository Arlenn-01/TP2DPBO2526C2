# Program utama Python untuk input dokter dan tabel dinamis
import sys

from DokterSpesialis import DokterSpesialis

HEADERS = [
	# Judul kolom menjadi acuan ukuran awal tabel
	"Surat Tanda Registrasi", "Nama", "Umur", "Gender", "Gaji Pokok",
	"Spesialisasi", "Spesialisasi Tarif", "Gelar Spesialis", "Rumah Sakit",
]


def data_baris(dokter):
	"""Mengubah objek menjadi nilai yang siap dirender sebagai satu baris"""
	# Angka diubah ke string agar panjang semua isi dapat diukur dengan cara yang sama
	return [
		dokter.getStr(), dokter.getNama(), str(dokter.getUmur()), dokter.getGender(),
		str(dokter.getGajiPokok()), dokter.getSpesialisasi(),
		str(dokter.getSpesialisasiTarif()), dokter.getGelarSpesialis(),
		dokter.getRumahSakit(),
	]


def cetak_tabel_dinamis(daftar_dokter):
	"""Menghitung lebar tiap kolom berdasarkan header dan seluruh data"""
	# Setiap objek diubah menjadi satu baris sebelum ukuran kolom dihitung
	rows = [data_baris(dokter) for dokter in daftar_dokter]
	# Lebar awal setiap kolom mengikuti panjang judul tabel
	widths = [len(header) for header in HEADERS]
	for row in rows:
		# Lebar kolom diperbesar jika isi data lebih panjang daripada judulnya
		widths = [max(width, len(value)) for width, value in zip(widths, row)]

	# Garis tabel dibentuk dari tanda minus sesuai lebar masing-masing kolom
	border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

	def format_row(row):
		# ljust menambahkan spasi agar setiap pemisah kolom tetap sejajar
		return "| " + " | ".join(value.ljust(width) for value, width in zip(row, widths)) + " |"

	# Urutan cetak terdiri dari garis atas, header, isi data, dan garis bawah
	print(border)
	print(format_row(HEADERS))
	print(border)
	for row in rows:
		print(format_row(row))
	print(border)


def baca_dokter(input_stream):
	"""Membaca delapan nilai dokter dari input baris demi baris"""
	# Urutan input mengikuti format Java: nama sampai gelar spesialis
	# readline menjaga teks yang memiliki spasi agar terbaca sebagai satu nilai
	return DokterSpesialis(
		input_stream.readline().rstrip("\n"),
		int(input_stream.readline()),
		input_stream.readline().rstrip("\n"),
		int(input_stream.readline()),
		input_stream.readline().rstrip("\n"),
		input_stream.readline().rstrip("\n"),
		int(input_stream.readline()),
		input_stream.readline().rstrip("\n"),
	)


def main():
	# Membuat lima data awal seperti pada implementasi Java
	daftar_dokter = [
		DokterSpesialis("Asep", 35, "Pria", 40000000, "Hasan Sadikin", "Jantung", 500000, "Sp.Jp"),
		DokterSpesialis("Ahmad", 36, "Pria", 30000000, "Hasan Sadikin", "Penyakit Dalam", 300000, "Sp.PD"),
		DokterSpesialis("Udin", 37, "Pria", 30000000, "Hasan Sadikin", "Anak", 350000, "Sp.A"),
		DokterSpesialis("Ucup", 38, "Pria", 40000000, "Hasan Sadikin", "Kandungan", 450000, "Sp.OG"),
		DokterSpesialis("Ancika", 25, "Wanita", 35000000, "Pindad", "Saraf", 400000, "Sp.Jp"),
	]

	# Tabel pertama menampilkan data awal sebelum input tambahan
	cetak_tabel_dinamis(daftar_dokter)
	jawaban = input("Mau nambah data? (yes/no) ").strip().lower()
	if jawaban == "yes":
		# Jumlah data menentukan berapa kali delapan input dibaca
		banyak_data = int(input("Berapa banyak data? "))
		print("Silakan masukkan data sesuai format")
		for _ in range(banyak_data):
			# Data baru langsung dimasukkan ke daftar sebelum tabel kedua dicetak
			daftar_dokter.append(baca_dokter(sys.stdin))

	# Tabel kedua menampilkan data awal dan data tambahan
	cetak_tabel_dinamis(daftar_dokter)


if __name__ == "__main__":
	main()