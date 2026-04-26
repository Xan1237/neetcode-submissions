class Solution {

    public String encode(List<String> strs) {
        String concat = "";
        for (String s : strs){
            concat += "-";
            concat += s;
        }
        return concat;
    }

    public List<String> decode(String str) {
    if(str.length()==0){
        return new ArrayList<>();
    }
    String[] list = str.split("-");
    List<String> string = new ArrayList<String>(Arrays.asList(list));
      if (!string.isEmpty()) {
        string.remove(0);
    }else{
        return new ArrayList<>(Collections.singletonList(""));
    }
    return string;
    }
}
