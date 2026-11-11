class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        int left = 0;
        int right = nums.length-1;

        while(left<right) {
            int temp = nums[left];
            nums[left]= nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
        int l=0;
        int r=k-1;

        int L = k;
        int R = n-1;
        while(l<r) {
            int temp = nums[l];
            nums[l]= nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
        while(L<R) {
            int temp = nums[L];
            nums[L]= nums[R];
            nums[R] = temp;
            L++;
            R--;
        }
    }
}