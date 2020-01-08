class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        Arrays.parallelPrefix(arr, (a,b) -> a ^ b);
        return Arrays.stream(queries).mapToInt($ -> $[0] != 0 ? arr[$[0] - 1] ^ arr[$[1]] : arr[$[1]]).toArray();
    }
}
