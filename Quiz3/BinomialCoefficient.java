import java.util.*;

class BinomialCoefficient {

    static int binomialCoefficientDC(int n, int k) {
        if (k > n)
            return 0;
        if (k == 0 || k == n)
            return 1;
        return binomialCoefficientDC(n - 1, k - 1)
                + binomialCoefficientDC(n - 1, k);
    }

    static int binomialCoefficientDP(int n, int k) {
        int B[][] = new int[n + 1][k + 1];
        int i, j;

        for (i = 0; i <= n; i++) {
            for (j = 0; j <= min(i, k); j++) {
                if (j == 0 || j == i)
                    B[i][j] = 1;
                else
                    B[i][j] = B[i - 1][j - 1] + B[i - 1][j];
            }
        }

        return B[n][k];
    }

    static int min(int a, int b) {
        return (a < b) ? a : b;
    }

    public static void main(String[] args) {

        // Please uncomment the section you would like to run otherwise it would end up running all codes

        // Algo3.1: k variable, n constant

        // int n1 = 30;
        // for(int i = 0; i <= 30; i++){
        // long start = System.currentTimeMillis();
        // binomialCoeff(n1, i);
        // long end = System.currentTimeMillis();
        // long elapsedTime = end - start;
        // System.out.println(elapsedTime);
        // }

        // Algo3.1: n variable, k constant

        // int k1 = 20;
        // for (int i = 15; i <= 40; i++) {
        //     long start = System.currentTimeMillis();
        //     binomialCoefficientDC(i, k1);

        //     long end = System.currentTimeMillis();
        //     long elapsedTime = end - start;
        //     System.out.println(elapsedTime);
        // }
        
        // Algo3.2: k variable, n constant

        // int n2 = 3000;
        // for(int i = 0; i <= 3000; i = i+10){
        // long start = System.currentTimeMillis();
        // binomialCoefficientDP(n2, i);
        // long end = System.currentTimeMillis();
        // long elapsedTime = end - start;
        // System.out.println(elapsedTime);
        // }

        // Algo3.2: n variable, k constant

        // int k2 = 750;
        // for (int i = 700; i <= 8000; i = i + 10) {
        //     long start = System.currentTimeMillis();
        //     binomialCoefficientDP(i, k2);

        //     long end = System.currentTimeMillis();
        //     long elapsedTime = end - start;
        //     System.out.println(elapsedTime);
        // }
    }
}