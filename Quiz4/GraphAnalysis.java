import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.*;

public class GraphAnalysis {
    public static void main(String[] args) {
        int test_case = 1;

        try {

            Scanner sc = new Scanner(new BufferedReader(new FileReader("input.txt")));

            while (sc.hasNextLine()) {
                int t = 0;
                int size = 0;
                int counter1 = 0;
                int counter2 = 0;
                int connected = 0;

                String line = sc.nextLine();

                int v = Integer.parseInt(String.valueOf(line));
                size = (v * v) - v;

                int[][] aMat = new int[v][v];
                for (int i = 0; i < v; i++) {
                    String[] rows = sc.nextLine().split(" ");

                    for (int j = 0; j < v; j++) {
                        aMat[i][j] = Integer.parseInt(rows[j]);

                    }
                }
                
                for (int i = 0; i < v; i++) {
                    for (int j = 0; j < v; j++) {
                        if (i != j && aMat[i][j] == 1) {
                            counter1++;
                        }
                    }
                }
                if(size != counter1){
                    connected = 1;
                }

                System.out.println("Test Case " + test_case);
                test_case = test_case + 1;
                if (connected == 0) {
                    System.out.println("Connected");
                } else {
                    System.out.println("Not Connected");
                }

                for (int i = 0; i < v; i++) {
                    for (int j = 0; j < v; j++) {

                        if (i != j && aMat[i][j] == 1) {
                            counter2++;
                        }
                    }
                }

                if (size == counter2) {

                    t = 1;
                }

                if (t == 1) {
                    System.out.println("Complete");

                } else {
                    System.out.println("Not Complete");
                }

                System.out.println("VerticesOut\tIn\tTotal");
                for (int m = 0; m < v; m++) {
                    int count1 = 0;
                    int count2 = 0;

                    for (int n = 0; n < v; n++) {
                        if (aMat[m][n] == 1) {
                            count1 = count1 + 1;
                        }

                    }
                    for (int p = 0; p < v; p++) {
                        if (aMat[p][m] == 1) {
                            count2 = count2 + 1;
                        }
                    }

                    int total = count1 + count2;

                    System.out.print(m + 1 + "\t" + count1);
                    System.out.println("\t" + count2);
                    System.out.println("\t\t\t" + total);
                }

            }

        } catch (FileNotFoundException filenotfoundexception) {
            System.out.println("File not found");
        }
    }
}
