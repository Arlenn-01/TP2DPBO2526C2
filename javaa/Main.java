package javaa;

import java.util.Scanner;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ArrayList<DokterSpesialis> daftarDokterSp = new ArrayList<>();

        //Membuat 5 Objek Awal
        daftarDokterSp.add(new DokterSpesialis("Asep", 35, "Pria", 40000000, "Hasan Sadikin", "Jantung", 500000, "Sp.Jp"));
        daftarDokterSp.add(new DokterSpesialis("Ahmad", 36, "Pria", 30000000, "Hasan Sadikin", "Penyakit Dalam", 300000, "Sp.PD"));
        daftarDokterSp.add(new DokterSpesialis("Udin", 37, "Pria", 30000000, "Hasan Sadikin", "Anak", 350000, "Sp.A"));
        daftarDokterSp.add(new DokterSpesialis("Ucup", 38, "Pria", 40000000, "Hasan Sadikin", "Kandungan", 450000, "Sp.OG"));
        daftarDokterSp.add(new DokterSpesialis("Ancika", 25, "Wanita", 35000000, "Pindad", "Saraf", 400000, "Sp.Jp"));

        CetakTabelDinamis(daftarDokterSp);

        System.out.println("Mau nambah data? (yes/no)");
        Scanner input = new Scanner(System.in);
        String yes_or_no = input.nextLine();
        //di java tanda (==) itu membandingkan alamat memory dan antara variable dan input keyboard bisa berbeda memory
        //maka solusinya pake .equals
        if (yes_or_no.equals("yes") || yes_or_no.equals("Yes") || yes_or_no.equals("YES")) {
            System.out.println("Berapa banyak data?");
            int banyak_data = Integer.parseInt(input.nextLine());
            System.out.println("Silahkan masukkan data sesuai format");

            for (int i=0; i<banyak_data; ++i) {
                String nama = input.nextLine();
                int umur = Integer.parseInt(input.nextLine()); //mengubah string menjadi int. Mencegah kelemahan pada nextInt biasa
                String gender = input.nextLine();
                long gaji = Long.parseLong(input.nextLine());
                String rumah_sakit = input.nextLine();
                String spesialisasi = input.nextLine();
                long spesialisasi_tarif = Long.parseLong(input.nextLine());
                String gelar_spesialisasi = input.nextLine();
                
                //masukkan ke arrayList
                DokterSpesialis dokter_baru = new DokterSpesialis(
                    nama, umur, gender, gaji, rumah_sakit, spesialisasi, spesialisasi_tarif, gelar_spesialisasi
                );
                daftarDokterSp.add(dokter_baru);
            }
        }
        CetakTabelDinamis(daftarDokterSp);
        input.close();
    }

    //helper method
    public static void CetakTabelDinamis(ArrayList<DokterSpesialis> daftarDokterSp) {
        //Header kolom
        String[] headers = {"Surat Tanda Registarsi", "Nama", "Umur", "Gender", "Gaji Pokok", "Spesialisasi", "Spesialisasi Tarif", "Gelar Spesialis", "Rumah Sakit"};

        //hitung lebar maksimum untuk tiap kolom
        int[] max_lengths = new int[headers.length]; //length itu bawaan dari array statis 
        
        //set lebar awal berdasarkan panjang string headers
        for (int i=0; i<headers.length; ++i) {
            max_lengths[i] = headers[i].length(); //length disini sebagai len dari string
        }

        //Cari string terpanjang dari daftarDokterSp
        for (DokterSpesialis data : daftarDokterSp) { //in range based loop
            //tipe data prmitif harus dihtung manual
            int panjang_umur = String.valueOf(data.getUmur()).length();
            int panjang_gaji = String.valueOf(data.getGajiPokok()).length();
            int panjang_tarif = String.valueOf(data.getSpesialisasiTarif()).length();

            //cari string terpanjang
            //menggunakan max_length yang berada di scope luar sehingga nilai terpanjang dari tiap data tersimpan aman
            max_lengths[1] = Math.max(max_lengths[1], data.getNama().length());
            max_lengths[2] = Math.max(max_lengths[2], panjang_umur);
            max_lengths[3] = Math.max(max_lengths[3], data.getGender().length());
            max_lengths[4] = Math.max(max_lengths[4], panjang_gaji);
            max_lengths[5] = Math.max(max_lengths[5], data.getSpesialisasi().length());
            max_lengths[6] = Math.max(max_lengths[6], panjang_tarif);
            max_lengths[7] = Math.max(max_lengths[7], data.getGelarSpesialis().length());
            max_lengths[8] = Math.max(max_lengths[8], data.getRumahSakit().length());
        }

        StringBuilder formatBuilder = new StringBuilder(); //StringBuilder untuk append string
        StringBuilder borderBuilder = new StringBuilder(); //akan main main dengan sintaks "%-Ns"
        formatBuilder.append("| ");
        borderBuilder.append("+");

        for (int len : max_lengths) {
            formatBuilder.append("%-").append(len).append("s | "); //"%-Ns |" 
            borderBuilder.append("-".repeat(len + 2)).append("+");
        }

        String format = formatBuilder.toString() + "\n";
        String border = borderBuilder.toString();

        //cetak garis atas
        System.out.println(border);
        //cetak header
        System.out.printf(format, (Object[]) headers);
        //cetak garis pembatas header dan inisialisasi
        System.out.println(border);

        for (DokterSpesialis data : daftarDokterSp) {
            System.out.printf(format,
                data.getStr(),
                data.getNama(),
                data.getUmur(),
                data.getGender(),
                data.getGajiPokok(),
                data.getSpesialisasi(),
                data.getSpesialisasiTarif(),
                data.getGelarSpesialis(),
                data.getRumahSakit()
            );
        }
        System.out.println(border);
    }
}
