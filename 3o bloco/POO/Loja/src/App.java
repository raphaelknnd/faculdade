public class App {
    public static void main(String[] args) throws Exception {
        /*1.2) Crie um objeto da classe "Produto" chamado "prod1" e inicialize seus atributos com os seguintes valores:
         * nome="Camiseta", preço=29.99, quantidadeEmEstoque=50. */
        Produto prod1 = new Produto("Camiseta", 29.99, 50);

        /*1.3) Crie outro objeto da classe "Produto" chamado "prod2" e inicialize seus atributos com os seguintes valores
         *nome="Calça", preço=59.99, quantidadeEmEstoque=20. */
        Produto prod2 = new Produto("Calça", 59.99, 20);

        //2.2) Chame o método "vender" no objeto "prod1" passando uma quantidade de 5.".
        prod1.vender(5);

        //2.3) Imprima na tela a quantidade em estoque do objeto "prod1".
        System.out.println(prod1.getQuantidadeEmEstoque());

        // 2.4) Chame o método "vender" no objeto "prod2" passando uma quantidade de 10.
        prod2.vender(10);

        // 2.5) Imprima na tela a quantidade em estoque do objeto "prod2.
        System.out.println(prod2.getQuantidadeEmEstoque());
    }
}
