class Solution {
    public int fib(int n) {
        int a = 0, b = 1;
        int count = 0;
        int next;
        while (count<n) {
            next = a+b;
            a = b;
            b = next;
            count++;
        }
        return a;


    }   
}