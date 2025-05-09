package interviewPrep;

import java.util.Arrays;
import java.util.HashMap;

public class StringQuestions {
    public String reverse(String s) {
        char[] characters = s.toCharArray();
        int left = 0;
        int right = characters.length - 1;

        while(left < right) {
            char temp = characters[left];
            characters[left] = characters[right];
            characters[right] = temp;            
            left++;
            right--;
        }

        return new String(characters);
    }

    public String reverse2(String s) {
        char[] characters = s.toCharArray();
        int left = 0;
        int right = characters.length - 1;

        while(left < right) {
            char temp = characters[left];
            characters[left] = characters[right];
            characters[right] = temp;

            left++;
            right--;
        }

        return new String(characters);
    }


    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    public boolean isPalindrom(String s) {
        int left = 0;
        int right = s.length() - 1;

        while(left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        char[] sa = s.toCharArray();
        char[] ta = t.toCharArray();

        Arrays.sort(sa);
        Arrays.sort(ta);

        return Arrays.equals(sa, ta);
    }
}
