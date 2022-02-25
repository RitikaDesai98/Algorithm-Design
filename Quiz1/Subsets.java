import java.io.*;
 
class Subsets {
    //subsetLogic takes in parameters arr[] -> the input set, n -> lenght of arr[], subsetSize -> size of subset, 
    // temp[] -> temporary array to store the subset combinations, index -> current index of temp[]
    static void subsetLogic(int arr[], int n, int subsetSize,
                          int index, int temp[], int i)
    {
        // prints the subset that's ready 
        if (index == subsetSize) {
            for (int j = 0; j < subsetSize; j++)
                System.out.print(temp[j] + " ");
            System.out.println("");
            return; 
        }
        // if there are no more elements to be added into the temp array
        if (i >= n)
            return;
        //inserting arr[i] into temp[index]
        temp[index] = arr[i];
        subsetLogic(arr, n, subsetSize, index + 1,
                               temp, i + 1);
        subsetLogic(arr, n, subsetSize, index, temp, i + 1);

    }

    static void printSubset(int arr[], int n, int subsetSize)
    {
        //temp to store the subsets
        int temp[] = new int[subsetSize];
        subsetLogic(arr, n, subsetSize, 0, temp, 0);

        if(subsetSize > n) {
            System.out.println("Size of subset is greater than size of input set");
        }
    }
 
    public static void main(String[] args)
    {
        int arr[] = {7,3};
        int subsetSize = 3;
        int n = arr.length;
        for(int i = 0; i < arr.length; i++)
        {
            System.out.println(arr[i]);
        }
        printSubset(arr, n, subsetSize);
        
    }
}