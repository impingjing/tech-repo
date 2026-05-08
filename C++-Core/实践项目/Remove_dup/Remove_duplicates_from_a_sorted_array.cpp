#include <vector>
using namespace std;
/* Remove duplicates from a sorted array */
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // 处理空数组的情况
        if(nums.empty()) return 0;
        // 利用双指针解决
        int slow=0; // 慢指针，指向当前不重复元素的最后一个位置
        int fast=1; // 快指针，用于遍历数组

        for(fast=1;fast<nums.size();++fast){
            if(nums[fast]!=nums[slow]){ // 如果快指针指向的元素与慢指针指向的元素不同，说明找到了一个新的不重复元素
                slow++;
                nums[slow]=nums[fast];
            }
        }
        return slow+1;
    }
};