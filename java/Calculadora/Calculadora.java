import java.util.Scanner;

public class Calculadora {

    public double soma(double n1, double n2) {
        return n1 + n2;
    }

    public double sub(double n1, double n2) {
        return n1 - n2;
    }

    public double multi(double n1, double n2) {
        return n1 * n2;
    }

    public double div(double n1, double n2) {
        if (n2 == 0) throw new IllegalArgumentException("Não é possivel dividir por 0!");
        return n1 / n2;
    }

    public double func(String sinal, double n1, double n2) {
        switch (sinal) {
            case "+":
                return soma(n1, n2);
            case "-":
                return sub(n1, n2);
            case "*":
                return multi(n1, n2);
            case "/":
                return div(n1, n2);
            default:
                throw new IllegalArgumentException("Operação desconhecida!");
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calculadora c = new Calculadora();
        double n1 = sc.nextDouble();
        double n2 = sc.nextDouble();
        sc.nextLine();
        System.out.print("Operação: ");
        String sinal = sc.nextLine();
        System.out.println(c.func(sinal, n1, n2));
        sc.close();
    }
}