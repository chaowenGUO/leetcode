class Solution {
    public int[] twoSum(int[] nums, int target) {
        final HashMap<Integer, Integer> dictionary = new HashMap<>();
        final ListIterator<Integer> iter = Arrays.stream(nums).boxed().collect(Collectors.toList()).listIterator();
        while (iter.hasNext())
        {
            final int index = iter.nextIndex(), num = iter.next();
            if (dictionary.containsKey(num)) return new int[]{index, dictionary.get(num)};
            else dictionary.putIfAbsent(target - num, index);
        }
        return new int[0];
    }
}
