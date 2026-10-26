class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newStr = new StringBuilder();
        for(char c : s.toCharArray()){
            if(Character.isLetterOrDigit(c)){
                newStr.append(Character.toLowerCase(c));
            }
        }
        // String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int j = newStr.length() - 1;
        for(int i = 0; i < newStr.length(); i++){
            if(newStr.charAt(i) != newStr.charAt(j)){
                return false;
            }
            j--;
        }
        return true;
    }
}
