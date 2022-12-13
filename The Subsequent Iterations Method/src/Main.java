import java.util.Scanner;

public class Main {

    public static double function(double x){
        return Math.exp(-x);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x0;
        double x;
        double y;
        double EPSILON = 0.000001;
        int i = 1;

        x0 = 1.000000;

        x = x0;
        y = function(x);

        System.out.printf("-----------------------------------------------------------------------------\n" +
                "Iterations:\n" +
                "-----------------------------------------------------------------------------\n"+
                "%02d. \t %.6f\n", i++, y);
        while ( Math.abs(y-x) > EPSILON) {

            x = y;
            y = function(x);

            System.out.printf("%02d. \t %.6f\n", i++, y);
        }

        System.out.println("-----------------------------------------------------------------------------");
        System.out.printf("The Answer is: %.6f\n" +
                "-----------------------------------------------------------------------------", y);
    }
}