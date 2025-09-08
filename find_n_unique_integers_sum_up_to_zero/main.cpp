#include <iostream>
#include <vector>

using namespace std; 

class Solution {
public:
    vector<int> sumZero(int n) {
        if(n == 1){
            return vector<int>{0};
        }

        if(n == 2){
            return vector<int>{-1,1};
        }

        auto array = vector<int>(n,0);
        for(size_t i = 0; i < (int)n/2; i++){
            // cout << "aaa " << i << " " << i*1 << " " <<(i+1) << "\n";
            array.at(i+(i*1)) = i+1;
            array.at(i+(i+1)) = -(i+1);
        }

        return array;
    }
};

int main(){
    auto sol = Solution();

    for(const auto a : sol.sumZero(6)){
        cout << a << ",";
    }
    cout << endl;
    
    return 0;
}
