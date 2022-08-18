import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class TSP2D {
    public static void main(String[] args) throws FileNotFoundException {
        int varAdjMatrix[][] = createadjmatrix("Problem 2/Project 4_Problem 2_InputData.csv");
        varTotalNodes = varAdjMatrix.length;
        varresults = new int[varTotalNodes + 1];
        varNodeVisited = new boolean[varTotalNodes];
        bandb(varAdjMatrix);
        for (int i = 0; i < varAdjMatrix.length; i++) {
            for (int j = 0; j < varAdjMatrix[0].length; j++) {
                System.out.print(varAdjMatrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Optimal parameters: ");
        System.out.println("Cost: " + varMin);
        System.out.println("Path: ");
        for (int i = 0; i <= varTotalNodes; i++) {
            System.out.print(varresults[i] + " ");
        }
        System.out.println("\n");
    }
    static int varresults[];
    static boolean varNodeVisited[];
    static int varMin = Integer.MAX_VALUE;
    static int varTotalNodes = -1;
    private static int[][] createadjmatrix(String filevar) throws FileNotFoundException {
        //Find Max Node
        Scanner inputvar = new Scanner(new File(filevar));
        int varNodeMax = -1;
        inputvar.nextLine();
        while (inputvar.hasNext()) {
            String line = inputvar.nextLine();
            String[] values = line.split(",");
            int node = Integer.parseInt(values[0]);
            int connectedNode = Integer.parseInt(values[1]);
            if (varNodeMax < node)
                varNodeMax = node;
            if (varNodeMax < connectedNode)
                varNodeMax = connectedNode;
        }
        inputvar.close();
        inputvar = new Scanner(new File(filevar));
        //create matrix
        int[][] varAdjMatrix = new int[varNodeMax + 1][varNodeMax + 1];
        inputvar.nextLine();
        while (inputvar.hasNext()) {
            String varstring = inputvar.nextLine();
            String[] varstring1 = varstring.split(",");
            int varNode = Integer.parseInt(varstring1[0]);
            int varNodeConnected = Integer.parseInt(varstring1[1]);
            int varDistance = Integer.parseInt(varstring1[2]);
            varAdjMatrix[varNode][varNodeConnected] = varDistance;
        }
        inputvar.close();
        return varAdjMatrix;
    }
    static int firstMin(int array[][], int i) {
        int varmin = Integer.MAX_VALUE;
        for (int k = 0; k < varTotalNodes; k++)
            if (array[i][k] < varmin && i != k)
                varmin = array[i][k];
        return varmin;
    }
    static int secondMin(int array[][], int i) {
        int varmin = Integer.MAX_VALUE, varmin2 = Integer.MAX_VALUE;
        for (int j = 0; j < varTotalNodes; j++) {
            if (i == j)
                continue;
            if (array[i][j] <= varmin) {
                varmin2 = varmin;
                varmin = array[i][j];
            } else if (array[i][j] <= varmin2 && array[i][j] != varmin)
                varmin2 = array[i][j];
        }
        return varmin2;
    }
    static void bandbcreation(int array[][], int varbound, int varweight, int varlevel, int varpath[]) {
        if (varlevel == varTotalNodes) {
            if (array[varpath[varlevel - 1]][varpath[0]] != 0) {
                int curr_res = varweight + array[varpath[varlevel - 1]][varpath[0]];
                if (curr_res < varMin) {
                    System.arraycopy(varpath, 0, varresults, 0, varpath.length);
                    varresults[varTotalNodes] = varpath[0];
                    varMin = curr_res;
                }
            }
            return;
        }
        for (int i = 0; i < varTotalNodes; i++) {
            if (array[varpath[varlevel - 1]][i] != 0 && varNodeVisited[i] == false) {
                int temp = varbound;
                varweight += array[varpath[varlevel - 1]][i];
                if (varlevel == 1)
                    varbound -= ((firstMin(array, varpath[varlevel - 1]) + firstMin(array, i)) / 2);
                else
                    varbound -= ((secondMin(array, varpath[varlevel - 1]) + firstMin(array, i)) / 2);

                if (varbound + varweight < varMin) {
                    varpath[varlevel] = i;
                    varNodeVisited[i] = true;
                    bandbcreation(array, varbound, varweight, varlevel + 1, varpath);
                }
                varweight -= array[varpath[varlevel - 1]][i];
                varbound = temp;
                Arrays.fill(varNodeVisited, false);
                for (int j = 0; j <= varlevel - 1; j++)
                    varNodeVisited[varpath[j]] = true;
            }
        }
    }
    static void bandb(int array[][]) {
        int varpath[] = new int[varTotalNodes + 1];
        int varbound = 0;
        Arrays.fill(varpath, -1);
        Arrays.fill(varNodeVisited, false);
        for (int i = 0; i < varTotalNodes; i++)
            varbound += (firstMin(array, i) + secondMin(array, i));
        varbound = (varbound == 1) ? varbound / 2 + 1 : varbound / 2;
        varNodeVisited[0] = true;
        varpath[0] = 0;
        bandbcreation(array, varbound, 0, 1, varpath);
    }
}
