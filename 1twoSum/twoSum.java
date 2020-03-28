class Solution {
    public int[] twoSum(int[] nums, int target) {
        final var dictionary = new HashMap<Integer, Integer>();
        final var iter = Arrays.stream(nums).boxed().collect(Collectors.toList()).listIterator();
        while (iter.hasNext())
        {
            final var index = iter.nextIndex();
            final var num = iter.next();
            if (dictionary.containsKey(num)) return new int[]{index, dictionary.get(num)};
            else dictionary.putIfAbsent(target - num, index);
        }
        return new int[0];
    }
}
