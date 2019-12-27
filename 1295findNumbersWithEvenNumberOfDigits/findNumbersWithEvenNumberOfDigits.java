class Solution {
    private static int even(int num)
    {
        int result = 0;
        while (num != 0)
        {
            num /= 10;
            ++result;
        }
        return 1 - result & 1;
    }
    
    public int findNumbers(int[] nums) {
        return Arrays.stream(nums).map(Solution::even).sum();
    }
}
