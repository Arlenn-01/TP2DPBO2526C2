package javaa;

public class DokterSpesialis extends Dokter {
    private String spesialisasi; //misal jantung, anak, paru, dll
    private long spesialisasi_tarif; //tarif khusus penanganan di bidang spesialisasinya
    private String gelar_spesialis; // "Sp.JP" dan lain lain

    public DokterSpesialis( //parameter kebawah biar ga kepanjangan
        String nama, 
        int umur, 
        String gender,
        long gaji_pokok,
        String rumah_sakit,
        String spesialisasi,
        long spesialisasi_tarif,
        String gelar_spesialis
    ) {
        //inisialisasi class dokter
        super(nama, umur, gender, gaji_pokok, rumah_sakit); 
        
        setSpesialisasi(spesialisasi);
        setSpesialisasiTarif(spesialisasi_tarif);
        setGelarSpesialis(gelar_spesialis);
    }
    
    //getter
    public String getSpesialisasi() {
        return spesialisasi;
    }
    public long getSpesialisasiTarif() {
        return spesialisasi_tarif;
    }
    public String getGelarSpesialis() {
        return gelar_spesialis;
    }

    //setter
    public void setSpesialisasi(String spesialisasi) {
        if (spesialisasi == "") { //early exit 
            System.out.println("Spesialisasi tidak boleh berupa string kosong");
            return;
        }
        this.spesialisasi = spesialisasi;
    }
    public void setSpesialisasiTarif(long spesialisasi_tarif) {
        if (spesialisasi_tarif < 0) {
            System.out.println("Tarif spesialisasi tidak boleh minus");
            return;
        }
        this.spesialisasi_tarif = spesialisasi_tarif;
    }
    public void setGelarSpesialis(String gelar_spesialis) {
        if (gelar_spesialis == "") {
            System.out.println("Gelar tidak boleh berupa string kosong");
            return;
        }
        this.gelar_spesialis = gelar_spesialis;
    }

    //informasi
    public void informasiDokterSpesialis() {
        System.out.println(getNama());
        System.out.println(getUmur());
        System.out.println(getGender());
        System.out.println(getStr());
        System.out.println(getGajiPokok());
        System.out.println(getRumahSakit());
        System.out.println(getSpesialisasi());
        System.out.println(getSpesialisasiTarif());
        System.out.println(getGelarSpesialis());
    }
}
