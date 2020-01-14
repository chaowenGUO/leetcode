class Solution {
    public boolean canReach(int[] arr, int start) {
        final LinkedList<Integer> queue = IntStream.of(start).boxed().collect(Collectors.toCollection(LinkedList::new));
        final Set<Integer> seen = IntStream.of(start).boxed().collect(Collectors.toSet());
        while (!queue.isEmpty())
        {
            final int index = queue.poll();
            if (arr[index] == 0) return true;
            else
            {
                final Set<Integer> child = IntStream.of(index + arr[index], index - arr[index]).filter($ -> 0 <= $ && $ < arr.length).boxed().collect(Collectors.toSet());
                child.removeAll(seen);
                queue.addAll(child);
                seen.addAll(child);
            }
        }
        return false;
    }
}
