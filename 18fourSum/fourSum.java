class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        final Map<Integer, List<java.util.AbstractMap.SimpleEntry<Integer, Integer>>> dictionary = IntStream.range(0, nums.length - 1).boxed().flatMap(left -> IntStream.range(left + 1, nums.length).mapToObj(right -> new java.util.AbstractMap.SimpleEntry<>(left, right))).collect(Collectors.groupingBy($ -> nums[$.getKey()] + nums[$.getValue()]));        
        final HashSet<List<Integer>> result = new HashSet<>();
        java.util.stream.IntStream.range(2, nums.length - 1).forEach(left -> java.util.stream.IntStream.range(left + 1, nums.length).forEach(right -> {
            final int complement = target - java.util.stream.IntStream.of(left, right).map($ -> nums[$]).sum();
            if (dictionary.containsKey(complement)) dictionary.get(complement).stream().filter($ -> $.getValue() < left).forEach($_ -> result.add(java.util.stream.IntStream.of($_.getKey(), $_.getValue(), left, right).map($ -> nums[$]).boxed().collect(java.util.stream.Collectors.toList())));}));
        return new ArrayList<>(result);
    }
}
