import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class TSP1D {
    public static void main(String[] args) throws FileNotFoundException {
        int varAdjMatrix[] = createadjmatrix("Problem 2/Project 4_Problem 2_InputData.csv");
        varresults = new int[varTotalNodes + 1];
        varNodeVisited = new boolean[varTotalNodes];
        bandb(varAdjMatrix);
        for (int i = 0; i < varTotalNodes; i++) {
            for (int j = 0; j < varTotalNodes; j++) {
                System.out.print(varAdjMatrix[i * varTotalNodes + j] + " ");
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
    private static int[] createadjmatrix(String filevar) throws FileNotFoundException {
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
        varTotalNodes = varNodeMax + 1;
        //create matrix
        int[] varAdjMatrix = new int[(varNodeMax + 1) * (varNodeMax + 1)];
        inputvar.nextLine();
        while(inputvar.hasNext()){
            String varTempString= inputvar.nextLine();
            String[] valuearr = varTempString.split(",");
            int varNode = Integer.parseInt(valuearr[0]);
            int varNodeConnect = Integer.parseInt(valuearr[1]);
            int varDistance = Integer.parseInt(valuearr[2]);
            varAdjMatrix[(varNode * (varNodeMax + 1)) + varNodeConnect] = varDistance;
        }
        inputvar.close();
        return varAdjMatrix;
    }
    static int firstMin(int array[], int i) {
        int varmin1 = Integer.MAX_VALUE;
        for (int k = 0; k < varTotalNodes; k++)
            if (array[i* varTotalNodes +k] < varmin1 && i != k)
                varmin1 = array[i* varTotalNodes +k];
        return varmin1;
    }
    static int secondMin(int array[], int i) {
        int varmin1 = Integer.MAX_VALUE;
        int varmin2 = Integer.MAX_VALUE;
        for (int j = 0; j < varTotalNodes; j++) {
            if (i == j)
                continue;
            if (array[i* varTotalNodes +j] <= varmin1) {
                varmin2 = varmin1;
                varmin1 = array[i* varTotalNodes +j];
            } else if (array[i* varTotalNodes +j] <= varmin2 && array[i* varTotalNodes +j] != varmin1)
                varmin2 = array[i* varTotalNodes +j];
        }
        return varmin2;
    }
    static void bandbcreation(int array[], int varbound, int varweight, int varlevel, int varpath[]) {
        if (varlevel == varTotalNodes) {
            if (array[varpath[varlevel - 1] * varTotalNodes + varpath[0]] != 0) {
                int varres = varweight + array[varpath[varlevel - 1] * varTotalNodes + varpath[0]];
                if (varres < varMin) {
                    System.arraycopy(varpath, 0, varresults, 0, varpath.length);
                    varresults[varTotalNodes] = varpath[0];
                    varMin = varres;
                }
            }
            return;
        }
        for (int i = 0; i < varTotalNodes; i++) {
            if (array[varpath[varlevel - 1]* varTotalNodes +i] != 0 && varNodeVisited[i] == false) {
                int temp = varbound;
                varweight += array[varpath[varlevel - 1]* varTotalNodes +i];
                if (varlevel == 1)
                    varbound -= ((firstMin(array, varpath[varlevel - 1]) + firstMin(array, i)) / 2);
                else
                    varbound -= ((secondMin(array, varpath[varlevel - 1]) + firstMin(array, i)) / 2);
                if (varbound + varweight < varMin) {
                    varpath[varlevel] = i;
                    varNodeVisited[i] = true;
                    bandbcreation(array, varbound, varweight, varlevel + 1, varpath);
                }
                varweight -= array[varpath[varlevel - 1]* varTotalNodes +i];
                varbound = temp;
                Arrays.fill(varNodeVisited, false);
                for (int j = 0; j <= varlevel - 1; j++)
                    varNodeVisited[varpath[j]] = true;
            }
        }
    }
    static void bandb(int array[]) {
        int varpath[] = new int[varTotalNodes + 1];
        int varbound = 0;
        Arrays.fill(varpath, -1);
        Arrays.fill(varNodeVisited, false);
        for (int i = 0; i < varTotalNodes; i++)
            varbound += (firstMin(array, i) + secondMin(array, i));
        varbound = (varbound == 1) ? varbound / 2 + 1 :
            varbound / 2;
        varNodeVisited[0] = true;
        varpath[0] = 0;
        bandbcreation(array, varbound, 0, 1, varpath);
    }
}
