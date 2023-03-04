public class Produto {
    /*1) Criação de classses e objetos 
     * 1.1) Crie uma classe chamada "Produto" com os seguintes atributos: nome (String), preço (double)
     * e quantidadeEmEstoque (int), todos privados.
    */
    private String nome;
    private double preco;
    private int quantidadeEmEstoque;

    public Produto(String nome, double preco, int quantidadeEmEstoque){
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidadeEmEstoque() {
        return quantidadeEmEstoque;
    }

    public void setQuantidadeEmEstoque(int quantidadeEmEstoque) {
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    /*2.1) Adicione um método na classe "Produto" chamado "vender" que diminui a quantidade em estoque do produto em uma
     *quantidade recebida como parâmetro. */

    public void vender(int amount){
        if(getQuantidadeEmEstoque() == 0){
            System.out.println("Estoque zerado");
        }else{
            if(amount > getQuantidadeEmEstoque()){
                System.out.println("Pedido superior ao estoque. Quant. em estoque = " + getQuantidadeEmEstoque());
            }else{
                setQuantidadeEmEstoque(getQuantidadeEmEstoque() - amount);
                System.out.println("Venda confirmada.");
            }
        }
        
    }

}
