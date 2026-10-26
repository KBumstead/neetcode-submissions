class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> sMap = new HashMap<Character, Integer>();
        HashMap<Character, Integer> tMap = new HashMap<Character, Integer>();

        for(int i = 0; i < s.length(); i++){
           char sChar = s.charAt(i);
           char tChar = t.charAt(i);

           sMap.put(sChar, sMap.getOrDefault(sChar, 0) + 1);
           tMap.put(tChar, tMap.getOrDefault(tChar, 0) + 1);
        }

        for (Character key : sMap.keySet()){
            if(!tMap.containsKey(key) || !sMap.get(key).equals(tMap.get(key))){
                return false;
            }
        }

    return true;

    }
}
