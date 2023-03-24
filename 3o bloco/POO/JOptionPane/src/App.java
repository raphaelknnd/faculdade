import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) throws Exception {
        int num = Integer.parseInt(JOptionPane.showInputDialog("Insira um numero"));
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Insira um numero"));

        int soma = num + num2;

        JOptionPane.showMessageDialog(null, "A soma eh, " + soma, null, 1);
    }
}
