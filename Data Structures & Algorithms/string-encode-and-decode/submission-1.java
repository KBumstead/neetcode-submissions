class Solution {

    public String encode(List<String> strs) {
        String string = "";
        for(int i = 0; i < strs.size(); i++){
            string += strs.get(i) + "|";
        }
        return string;
    }

    public List<String> decode(String str) {
        List<String> decode = new ArrayList<>();
        String temp = "";
        int pos = 0;
        for(int i = 0; i < str.length(); i ++){
            if(str.charAt(i) == '|'){
                decode.add(temp);
                temp = "";
            }else{
                temp += str.charAt(i);
            }
        }
        return decode;
    }
}
