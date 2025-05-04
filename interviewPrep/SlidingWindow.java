package interviewPrep;

import java.util.HashSet;

public class SlidingWindow {
    public int lengthOfLongestSubString(String s) {
        // Create a set
        HashSet<Character> set = new HashSet<>();
        // create the left and the right pointers
        int l = 0;
        // Maintain a counter for the max length
        int maxLength = 0;
        
        for(int r = 0; r < s.length(); r++) {
            while(set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l++;
            }

            set.add(s.charAt(r));
            maxLength = Math.max(maxLength, r - l + 1);
        }

        return maxLength;
    }

    public int maxLengthOfLongestUniqueSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int l = 0;
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            while (set.contains(s.charAt(i))) {
                set.remove(s.charAt(l));
                l++;
            }

            set.add(s.charAt(i));
            maxLength = Math.max(maxLength, i - l + 1);
        }

        return maxLength;
    }
}
