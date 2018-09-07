package easycontest.arraylist;

import java.util.Arrays;
import java.util.HashSet;

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

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>(nums.length);
        for (int num : nums) {
            if (!set.contains(num)) {
                set.add(num);
            } else {
                return true;
            }
        }
        return false;
    }

    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        Integer k = null;
        for (int num : nums) {
            if (k == null) {
                k = num;
            } else if (k == num) {
                k = null;
            } else {
                return k;
            }
        }
        return nums[nums.length - 1];
    }


    public static void main(String[] args) {
        int[] a = {1, 2, 3};
        int i = -1;
        System.out.println(a[i = 2]);
        System.out.println(i);
    }

}
