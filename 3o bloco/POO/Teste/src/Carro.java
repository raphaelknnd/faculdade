public class Carro {
    double velocidade;
    String modelo;
    boolean farolAceso;
    boolean ligado;

    public Carro(String modelo){
        this.modelo = modelo;
        this.velocidade = 0.0;
        this.farolAceso = false;
        this.ligado =  false;
    }

    public String situacao_carro(){
        return this.ligado == true ? "Sim" : "Nao";
    }

    public void ligar_carro(){
        this.ligado = true;
        System.out.println("Carro ligado.");
    }

    //Aqui iniciamos o exercício de implementação

    public void acelerar(){
        if(this.ligado == true){
            this.velocidade += 10;
        }else{
            System.out.println("O Carro está desligado.");
        }
    }

    public void frear(){
        if(this.ligado == false || this.velocidade == 0.0){
            System.out.println("O carro está parado.");
        }else{
            this.velocidade -= 10;
        }
    }

    public void acenderFarol(){
        this.farolAceso = true;
    }

    public void apagarFarol(){
        this.farolAceso = false;
    }
}