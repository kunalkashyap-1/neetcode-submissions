class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n != m) return false;

        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < n; i++){
            char c = s.charAt(i);
            map.put(c,map.getOrDefault(c,0)+1);
        }

        for(int i = 0; i < n; i++){
            char c = t.charAt(i);
            if (!map.containsKey(c)) return false;

            int val = map.get(c);
            if(val == 1) map.remove(c);
            else map.put(c,val-1);
        }
        return map.isEmpty();
    }
}
