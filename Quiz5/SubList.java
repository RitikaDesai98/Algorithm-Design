class SubList {

    static void maxSubArraySum(int a[], int size) {
        int max_now = Integer.MIN_VALUE, max_end = 0, start = 0, end = 0, k = 0;

        if(size == 0){
            System.out.println("Empty");
        }
        else{

        for (int i = 0; i < size; i++) {
            max_end += a[i];

            if (max_now < max_end) {
                max_now = max_end;
                start = k;
                end = i;
            }

            if (max_end < 0) {
                max_end = 0;
                k = i + 1;
            }
        }
        for(int i = start; i<=end;i++){
            System.out.println(a[i]);
        }
        System.out.println("Sum: " + max_now);        
    }
}

    public static void main(String[] args) {
        System.out.println("Test Case 1:");        
        int a1[] = {};
        int n1 = a1.length;
        maxSubArraySum(a1, n1);

        System.out.println("Test Case 2:");        
        int a2[] = {1};
        int n2 = a2.length;
        maxSubArraySum(a2, n2);

        System.out.println("Test Case 3:");        
        int a3[] = {1, 2, 3, 4};
        int n3 = a3.length;
        maxSubArraySum(a3, n3);

        System.out.println("Test Case 4:");        
        int a4[] = {-7, -4, -2, -8};
        int n4 = a4.length;
        maxSubArraySum(a4, n4);

        System.out.println("Test Case 5:");        
        int a5[] = {-2, 3, 5, -7};
        int n5 = a5.length;
        maxSubArraySum(a5, n5);

        System.out.println("Test Case 6:");        
        int a6[] = {-2, -3, 4, -1, -2, 1, 5, -3};
        int n6 = a6.length;
        maxSubArraySum(a6, n6);

        System.out.println("Test Case 7:");        
        int a7[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int n7 = a7.length;
        maxSubArraySum(a7, n7);
    }
}