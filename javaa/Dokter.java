package javaa;

public class Dokter extends Manusia {
    private String str; //Surat Tanda Registrasi (No.izin)
    private long gaji_pokok; //tidak boleh sembarangan dirubah jadi private
    private String rumah_sakit; 
    private static int str_counter = 1000; //ini untuk str unik yang tidak bisa diakses siapapun sembarangan
    //harus berupa static agar atribut dianggap milik class dan setiap kali ada objek baru nilainya akan meningkat

    public Dokter(String nama, int umur, String gender, long gaji_pokok, String rumah_sakit) {
        super(nama, umur, gender); //di java wajib inisialisasi constructor parent dengan sintaks super (ini constructor Manusia)
        setGajiPokok(gaji_pokok);
        setRumahSakit(rumah_sakit);
        this.str = generateStrOtomated(); //nantinya teks akan masuk ke str
    }

    private String generateStrOtomated() { //Surat tanda registrasi tidak bisa sembarangan diubah oleh siapapun
        str_counter++; //inin akan mengcounter nilai milik class
        return "STR-" + str_counter; 
    }

    //getter
    public String getStr() {
        return str;
    }
    public String getRumahSakit() {
        return rumah_sakit;
    }
    public long getGajiPokok() {
        return gaji_pokok;
    }

    //setter
    public void setRumahSakit(String rumah_sakit) {
        this.rumah_sakit = rumah_sakit;
    }
    public void setGajiPokok(long gaji_pokok) {
        this.gaji_pokok = gaji_pokok;
    }

    //informasi
    public void informasiDokter() {
        System.out.println(getNama());
        System.out.println(getUmur());
        System.out.println(getGender());
        System.out.println(getStr());
        System.out.println(getGajiPokok());
        System.out.println(getRumahSakit());
    }
}
