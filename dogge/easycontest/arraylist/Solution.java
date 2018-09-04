package easycontest.arraylist;

import java.util.Arrays;

public class Solution {
    public void rotate(int[] nums, int k) {
        k = k >= nums.length ? k % nums.length : k;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        int temp;
        while (end > start) {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }


    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        new Solution().rotate(nums, 3);
        System.out.println(Arrays.toString(nums));
    }

}
