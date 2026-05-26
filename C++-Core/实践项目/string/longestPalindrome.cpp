#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = static_cast<int>(s.length());
        if (n <= 1) {
            // 空串或单个字符本身就是回文串。
            return s;
        }

        int bestStart = 0;
        int bestLen = 1;

        // 回文串一定可以从“中心”向两边扩展得到。
        // 这里分别处理两种中心：
        // 1. 单中心：对应长度为奇数的回文串，例如 "aba"。
        // 2. 双中心：对应长度为偶数的回文串，例如 "abba"。
        for (int center = 0; center < n; ++center) {
            // 以 s[center] 为中心，向两边扩展，寻找奇数长度回文。
            int left = center;
            int right = center;
            while (left >= 0 && right < n && s[left] == s[right]) {
                int currentLen = right - left + 1;
                if (currentLen > bestLen) {
                    bestLen = currentLen;
                    bestStart = left;
                }
                --left;
                ++right;
            }

            // 以 s[center] 和 s[center + 1] 为中心，向两边扩展，寻找偶数长度回文。
            left = center;
            right = center + 1;
            while (left >= 0 && right < n && s[left] == s[right]) {
                int currentLen = right - left + 1;
                if (currentLen > bestLen) {
                    bestLen = currentLen;
                    bestStart = left;
                }
                --left;
                ++right;
            }
        }

        return s.substr(bestStart, bestLen);
    }
};