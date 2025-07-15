// https://leetcode.com/problems/process-string-with-special-operations-i/
class Solution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i != s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '*') {
                if (sb.length() > 0)
                    sb.deleteCharAt(sb.length() - 1);
            } else if (ch == '#')
                sb.append(sb.toString());
            else if (ch == '%')
                sb.reverse();
            else
                sb.append(ch);
        }
        return sb.toString();
    }
}
