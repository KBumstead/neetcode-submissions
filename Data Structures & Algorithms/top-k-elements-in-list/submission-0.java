class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<List<Integer>> count = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            count.add(new ArrayList<>());
        }

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);         
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            count.get(entry.getValue()).add(entry.getKey());
        }

        List<Integer> result = new ArrayList<>();
        for (int i = count.size() - 1; i >= 0 && result.size() < k; i--) {
            for (int num : count.get(i)) {
                result.add(num);
                if (result.size() == k) break;
            }
        }

        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = result.get(i);
        }

        return topK;
    }
}
