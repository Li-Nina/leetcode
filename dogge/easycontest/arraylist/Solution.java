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

    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i] = digits[i] + 1;
                return digits;
            } else {
                digits[i] = 0;
            }
        }
        int[] ints = new int[digits.length + 1];
        ints[0] = 1;
        return ints;
    }

    public void moveZeroes(int[] nums) {
        int firstZero = -1;
        for (int i = 0; i < nums.length; i++) {
            if (firstZero == -1 && nums[i] == 0) {
                firstZero = i;
            } else if (firstZero != -1 && nums[i] != 0) {
                nums[firstZero] = nums[i];
                nums[i] = 0;
                firstZero++;
            }
        }
    }


    public static void main(String[] args) {
        int[] a = {0, 1, 0, 3, 12};
        int[] b = {1, 1, 0, 3, 0, 12};
        new Solution().moveZeroes(a);
        System.out.println(Arrays.toString(a));
    }

}
