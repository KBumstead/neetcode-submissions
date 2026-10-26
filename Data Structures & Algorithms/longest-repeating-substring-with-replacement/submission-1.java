class Solution {
    public int characterReplacement(String s, int k) {
        int p = 0;
        int res = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(!map.containsKey(s.charAt(i))){
                map.put(s.charAt(i), 1);
            }else{
                map.put(s.charAt(i), map.get(s.charAt(i)) + 1);   
            }
            int mostFreqCount = 0;
            for(int count : map.values()){
                mostFreqCount = Math.max(mostFreqCount, count);
            }
            while(i - p + 1 - mostFreqCount > k){
                map.put(s.charAt(p), map.get(s.charAt(p)) - 1);
                p += 1;

            }
            res = Math.max(i - p + 1, res);
            
            
        }
        
        return res;
    }
}
