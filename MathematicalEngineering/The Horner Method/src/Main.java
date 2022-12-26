import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the maximum exponent: ");
        int n = sc.nextInt();

        int[] a = new int[n+1];
        System.out.print("Enter the coeficients in front of a_i: ");
        for (int i = 0; i <= n; i++) {
            a[i] = sc.nextInt();
        }

        System.out.print("Enter the argument r: ");
        int r = sc.nextInt();

        int[] b = new int[n+1];
        b[0] = a[0];
        for (int i = 1; i <= n; i++) {
            b[i] = a[i] + b[i-1]*r;
        }

        System.out.printf("The value of the polynomial is: %d\n", b[n]);

    }
}