class Solution {
    public int countPrimes(int n) {
        if (n < 2) return 0;
        else
        {
            final List<Integer> result = Collections.nCopies(n, 1).stream().collect(Collectors.toList());
            result.set(0, 0);
            result.set(1, 0);
            IntStream.range(2, (int)Math.sqrt(n) + 1).forEach(i -> {
                for (int j = (int)Math.pow(i, 2); j < n; j += i) result.set(j, 0);});
            return result.stream().mapToInt(Integer::intValue).sum();
        }
    }
}
