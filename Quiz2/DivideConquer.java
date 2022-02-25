class DivideConquer {
    public static void main(String[] args) {
        int[][] testCase1 = new int[][] { { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 } };
        int testRows1 = testCase1.length, testCols1 = testCase1[0].length, key1 = 8;

        search(testCase1, 0, testRows1 - 1, 0, testCols1 - 1, key1);
        int[][] testCase2 = new int[][] { { 2, 4, 9, 14, 14, 15, 18 },
                { 21, 27, 31, 35, 42, 45, 50 },
                { 54, 59, 64, 69, 82, 84, 84 } };
        int testRows2 = testCase2.length, testCols2 = testCase2[0].length, key2 = 45;

        search(testCase2, 0, testRows2 - 1, 0, testCols2 - 1, key2);

        int[][] testCase3 = new int[][] { { 3, 15, 21, 24, 83, 87, 88, 93 },
                { 178, 319, 541, 669, 770, 793, 848, 970 },
                { 1439, 1546, 1853, 2124, 2234, 2459, 2518, 2978 },
                { 3111, 3406, 3490, 3669, 3796, 3936, 4112, 4776 },
                { 5277, 5667, 6067, 6555, 7890, 8056, 8234, 9968 } };
        int testRows3 = testCase3.length, testCols3 = testCase3[0].length, key3 = 2356;

        search(testCase3, 0, testRows3 - 1, 0, testCols3 - 1, key3);
        

    }

    public static void search(int[][] arr, int startRow, int endRow,
            int startCol, int endCol, int key) {
        int i = startRow + (endRow - startRow) / 2;
        int j = startCol + (endCol - startCol) / 2;

        if (arr[i][j] == key) 
            System.out.println("Found " + key + " at [" + i +
                    "," + j + "]");

        else {
            if (i != endRow || j != startCol)
                search(arr, startRow, i, j, endCol, key);
            if (startRow == endRow && startCol + 1 == endCol)
                if (arr[startRow][endCol] == key)
                    System.out.println("Found " + key + " at [" +
                            startRow + "," + endCol + "]");
            if (arr[i][j] < key) {
                if (i + 1 <= endRow)
                    search(arr, i + 1, endRow, startCol, endCol, key);
            }
            else {
                if (j - 1 >= startCol)
                    search(arr, startRow, endRow, startCol, j - 1, key);
            }
        } 
            if(arr[i][j] > key){
                System.out.println("Not Found");
            }
        
        
    }
}
