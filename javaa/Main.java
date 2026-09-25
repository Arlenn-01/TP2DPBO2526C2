package javaa;

public class Main {
    public static void main(String[] args) {
        Manusia person = new Manusia("Arlen", 20, "Pria");
        person.informasi();
        System.out.println("\n=====================\n");
        Dokter dokter1 = new Dokter("Asep", 30, "Pria", 10000000, "Hasan Sadikin");
        Dokter dokter2 = new Dokter("Udin", 30, "Pria", 20000000, "Hasan Sadikin");
        dokter1.informasiDokter();
        dokter2.informasiDokter();
    }
}
