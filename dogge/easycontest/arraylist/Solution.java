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

    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> aLine = new HashSet<>();
        HashSet<Character> a1Squre = new HashSet<>();
        HashSet<Character> a2Squre = new HashSet<>();
        HashSet<Character> a3Squre = new HashSet<>();
        char[] chars;
        for (int i = 0; i < board.length; i++) {
            chars = board[i];//每一行
            for (int j = 0; j < chars.length; j++) {
                if (dealSet(chars[j], aLine) == 1) {
                    return false;
                }

                if (j < 3 && dealSet(chars[j], a1Squre) == 1) {
                    return false;
                } else if (j >= 3 && j < 6 && dealSet(chars[j], a2Squre) == 1) {
                    return false;
                } else if (j >= 6 && dealSet(chars[j], a3Squre) == 1) {
                    return false;
                }
            }
            aLine.clear();
            if (i % 3 == 2) {
                a1Squre.clear();
                a2Squre.clear();
                a3Squre.clear();
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (dealSet(board[j][i], aLine) == 1) {
                    return false;
                }
            }
            aLine.clear();
        }
        return true;
    }


    private int dealSet(Character c, HashSet<Character> set) {
        if (c != '.' && set.contains(c)) {
            return 1;
        } else {
            set.add(c);
            return 0;
        }
    }


    public void rotate(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i; j < matrix.length - 1 - i; j++) {
                int x = i, y = j;
                int move = matrix[x][y];
                for (int k = 0; k < 4; k++) {
                    int i1 = y;
                    int j1 = matrix.length - 1 - x;
                    int temp = matrix[i1][j1];
                    matrix[i1][j1] = move;
                    move = temp;
                    x = i1;
                    y = j1;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}};
        new Solution().rotate(matrix);
        System.out.println(Arrays.deepToString(matrix));
    }

}
