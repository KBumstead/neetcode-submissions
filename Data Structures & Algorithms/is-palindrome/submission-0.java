class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int j = cleaned.length() - 1;
        for(int i = 0; i < cleaned.length(); i++){
            if(cleaned.charAt(i) != cleaned.charAt(j)){
                return false;
            }
            j--;
        }
        return true;
    }
}
