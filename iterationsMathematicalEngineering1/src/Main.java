import java.util.Scanner;

public class Main {

    public static double function(double x){
        return ( (x*x*x) - (5*x) + 1 );
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a;
        double b;

        a = sc.nextDouble();
        b = sc.nextDouble();

        double c= (a+b)/2;

        double EPSILON = 0.0001;

        System.out.printf("-----------------------------------------------------------------------------\nIterations:\n-----------------------------------------------------------------------------\n" +
                "a = %.4f, b = %.4f, c = %.4f, f(a) = %.4f, f(b) = %.4f, f(c) = %.4f\n", a, b, c, function(a), function(b), function(c));
        while ( ((b-a)/2) > EPSILON) {

            if ( function(a)*function(c) < 0){
                b=c;
            }else{
                a=c;
            }

            c = (a+b)/2;
            System.out.printf("a = %.4f, b = %.4f, c = %.4f, f(a) = %.4f, f(b) = %.4f, f(c) = %.4f\n", a, b, c, function(a), function(b), function(c));
        }

        System.out.println("-----------------------------------------------------------------------------");
        System.out.printf("The Answer is: %.4f\n-----------------------------------------------------------------------------", c);
    }
}