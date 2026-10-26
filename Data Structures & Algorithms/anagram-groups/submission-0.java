class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<List<Integer>, List<String>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            List<Integer> countCharacter = new ArrayList<>(Collections.nCopies(26,0));
            for(int j = 0; j < strs[i].length(); j++){
                char a = 'a';
                int index = strs[i].charAt(j) - 'a';
                countCharacter.set(index, countCharacter.get(index) + 1);
            }

            if(!map.containsKey(countCharacter)){
                map.put(countCharacter, new ArrayList<>());
            }
            map.get(countCharacter).add(strs[i]);
        }
return new ArrayList<>(map.values());

    }
}
