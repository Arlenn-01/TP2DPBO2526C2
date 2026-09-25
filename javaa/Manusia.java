package javaa;

public class Manusia {
    private String nama;
    private int umur; 
    private String gender;

    public Manusia(String nama, int umur, String gender) {
        this.nama = nama;
        this.umur = umur;
        this.gender = gender;
    }

    // getter
    public String getNama() {
        return nama;
    }
    public int getUmur() {
        return umur;
    }
    public String getGender() {
        return gender;
    }

    // setter
    public void setNama(String nama) {
        if (nama == "") {
            System.out.println("Nama tidak boleh kosong");
            return; //exit
        } 
        this.nama = nama;
    }
    public void setUmur(int umur) {
        if (umur <= 0) {
            System.out.println("Umur tidak valid");
            return; //exit
        }
        this.umur = umur;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }

    //method
    public void informasi() {
        System.out.println(getNama());
        System.out.println(getUmur());
        System.out.println(getGender());
    }
}
