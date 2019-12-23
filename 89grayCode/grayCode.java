class Solution {
    public List<Integer> grayCode(int n) {
        return IntStream.range(0, 1 << n).map($ -> $ >> 1 ^ $).boxed().collect(Collectors.toList());
    }
}
