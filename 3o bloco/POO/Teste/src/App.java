public class App {
    public static void main(String[] args) throws Exception {
        Pessoa person = new Pessoa("João", 20, 'M');
        person.imprimirDados();

        Pessoa person2 = new Pessoa("Maria", 17, 'F');
        person2.imprimirDados();
    }
}
