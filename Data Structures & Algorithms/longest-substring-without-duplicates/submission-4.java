class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int res = 0;
        int p = 0;
        for(int i = 0; i < s.length();i++){
            while(set.contains(s.charAt(i))){
                set.remove(s.charAt(p));
                p += 1;
            }
            set.add(s.charAt(i));
            res = Math.max(res, i - p + 1);
        }

        return res;
    }
}
