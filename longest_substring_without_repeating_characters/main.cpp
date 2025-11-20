#include <set>
#include <map>
#include <print>

#define DEBUG

class Solution {

private:
    bool new_best_solution(int max_size, set<char>& new_solution){
        return new_solution.size() > max_size;
    }

public:
    int lengthOfLongestSubstring(string s) {
        if(s.empty()) return 0;

        set<char> in_current_chars;
        map<char, int> positions;

        int max_size = 1;

        for(size_t current_char_i = 0; current_char_i < s.length(); current_char_i++){
            char current_char = s[current_char_i];

            size_t prev_len = in_current_chars.size();
            in_current_chars.insert(current_char);
            size_t new_len = in_current_chars.size();

            #ifdef DEBUG
                printf("c=%c; i=%d\n", current_char, current_char_i);
            #endif

            // repeated char
            if(new_len == prev_len){
                int back_pos = positions[current_char];
                int new_pos = back_pos;

                #ifdef DEBUG
                    printf("CURRENT CHAR: %c;\n", current_char);
                    printf("POS: %d;\n", back_pos);
                    printf("BACKTRACKING POS: %d;\n\n", new_pos);
                #endif

                if(new_len > max_size){
                    max_size = new_len;
                }

                in_current_chars.clear();
                positions.clear();
                current_char_i = new_pos;
                continue;
            }

            positions[current_char] = current_char_i;
        }

        if(this->new_best_solution(max_size, in_current_chars)){
            return in_current_chars.size();
        }

        return max_size;
    }
};
