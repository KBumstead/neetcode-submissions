class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character,Integer> map = new HashMap<>();

        for(char c : s1.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        int p = 0;
        for(int i = s1.length()-1; i < s2.length(); i++){
            HashMap<Character, Integer> temp = new HashMap<>();
            for(int j = p; j <= i; j++){
                temp.put(s2.charAt(j), temp.getOrDefault(s2.charAt(j), 0) + 1);
            }
            if(map.equals(temp)){
                return true;
            }
            
            p++;    
        }
        return false;
    }
}
