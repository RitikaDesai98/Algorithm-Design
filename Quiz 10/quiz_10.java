import java.util.*;
import java.lang.*;
import java.io.*;

public class quiz_10{
    
    static int value = 0;    
    static int weight = 0;   
    
     public static void main(String []args){
        int[] weights = {2, 5, 7, 3, 1};
        int[] values = {20, 30, 35, 12, 3};
        int[] sol = new int[weights.length];
        int[] finalSol = new int[weights.length];
        int maxWeight = 9;
         
  
        knapsack(weights, values, maxWeight, 0, sol, finalSol);    
        for (int i = 0; i < finalSol.length; i++) {
            System.out.println(finalSol[i] * weights[i]);
        }
     }

public static void knapsack(int[] weights, int[] values, int maxWeight, int index, int[] sol, int[] finalSol) { 
        sol[index] = -1;
        int n = weights.length;
        while (sol[index] < 1) {
            sol[index] = sol[index] + 1;
            if (sum(index, sol, weights) <= maxWeight && index == n - 1) {
                System.out.println("Sol: " + Arrays.toString(sol));
                System.out.println("weight = " + sum(index, sol, weights));
                update(weights, values, maxWeight, index, sol, finalSol);
                System.out.println("---------------------------------");
            } else if (index < n - 1) {    
                knapsack(weights, values, maxWeight, index + 1, sol, finalSol);
                  
            }
              
        }
  
    }
    
    private static int sum(int index, int[] weights, int[] sol) {
        int res = 0;
        for (int i = 0; i < sol.length; i++) {
            if (sol[i] < 0 ) System.out.println("in sum: i = " + i + "   sol[i] = " + sol[i]);
            res += sol[i] * weights[i];
        }
        return res;
    }
  
    private static void update(int[] weights, int[] values, int maxWeight, int index, int[] sol, int[] finalSol) {  
        int totalValue = 0;
        int totalWeight = 0;
  
        for (int i = 0; i < weights.length; i++) {
            if (sol[i] == 1) {
                totalValue += values[i];
                totalWeight += weights[i];
            }
        }
  
        if (totalValue > value) {
            for (int i = 0; i < weights.length; i++) {
                finalSol[i] = sol[i];
            }
            value = totalValue;
            weight = totalWeight;
            System.out.println("new value: " + value);   
        }
         
    }
}
