
public class Pessoa {
    String nome;
    int idade;
    char sexo;

    public Pessoa(String nome, int idade, char sexo){
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;

    }

    public boolean verificarMaiorIdade(){
        return this.idade >= 18 ? true : false;

    }

    public boolean verificarAlistamentooMilitar(){
        if((this.idade >= 18 && this.idade <= 45) && this.sexo == 'M'){
            return true;
        }

        return false;

    }

    public void imprimirDados(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Idade: " + this.idade);
        System.out.println("Sexo: " + this.sexo);
        System.out.println("Maior Idade: " + this.verificarMaiorIdade());
        System.out.println("Precisa de alistamento: " + this.verificarAlistamentooMilitar() + "\n");
    }
}