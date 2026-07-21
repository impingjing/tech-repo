# 删除有序数组中的重复项

---

## 第一次尝试思路

新建一个数组arr用来计数`vector<int> arr(201);` 

新建一个数组temp代替nums，便于后续遍历数组计数

>下面是一个有很多BUG的代码，请思考，哪里错了？运行时会遇到什么问题？

```cpp
//这是一个有很多BUG的代码
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int s=nums.size();
        vector<int> temp=nums;

        vector<int> arr(201);
        for(int i=0;i<temp.size();i++){
            arr[temp[i]+100]++;
            if(arr[temp[i]+100]>1){
                for(int j=i;j<s-1;j++){
                    nums[j]=nums[j+1];
                }
                s--;
                arr[temp[i]+100]--;
            }
        }
        
        return s;
    }
};
```

- 索引越界：在内存循环移动元素时，使用了`num[j]=nums[j+1]`。当`j`到达`s-2`时，`j+1`就是`s-1`，这是合法的。但是，外层循环是基于`temp.size()`的，而`temp`是原数组的副本。当你修改 `nums` 的长度 `s` 后，如果后续 `i` 继续增加，可能会导致访问到无效的逻辑区域。
- 逻辑错误：删除元素后，后面的元素前移，当前的`i`实际上指向了一个新移过来的元素，直接进行下一次`i++`操作会漏掉对这个新元素的检查。
- 违反“原地删除”原则：新建了一个temp和arr额外数组。题目要求“原地”删除重复项，意思是**只能利用输入数组 `nums` 本身的空间**来完成任务。你不能为了计算方便而申请一个和输入数组一样大的新容器。

---

## 第二次尝试思路

在不改变第一次解决思路（哈希计数，发现重复就移位）下，改正语法错误。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       // 获取原始长度
        int s=nums.size();
       // ~~vector<int> temp=nums;~~ 删除temp这个多余的数组
        
        // int arr[201]=0; //错误！在C++中，原生数组的初始化规则比较严格
        // 你试图用一个整数 0 来初始化整个数组，编译器不知道如何把单个整数分配给整个数组，因此报错“array initializer must be an initializer list”（数组初始化器必须是初始化列表）。
        int arr[201]={0}; //用于计数，等同于vector<int> arr(201，0);

        for (int i = 0; i < s; i++) {
            arr[nums[i] + 100]++;

            if (arr[nums[i] + 100] > 1) {
                // 发现重复，元素前移
                for (int j = i; j < s - 1; j++) {
                    nums[j] = nums[j + 1];
                }
                s--;       // 数组长度减1
                i--;       // 【关键修改】索引回退，重新检查当前位置
                arr[nums[i] + 100]--; // 恢复计数（因为当前这个被移走了）
            }
        }
        return s;
    }
};
```

---

## 第三次优化思路

不创建arr来计数，用双指针解决问题

```cpp
class Solution {
public:
     int removeDuplicates(vector<int>& nums){
         // 检查数组为空的情况
         if(nums.empty()) return 0;
         // 设置双指针
         int slow=0;
         int fast=1;
         
         for(fast=1;fast<nums.size();++fast){
             if(nums[slow]!=nums[fast]){
                 //如果二者不相等，即说明是新元素
                 slow++; //慢指针移动
                 nums[slow]=nums[fast];
             }
         }
         
         return slow+1;
   }
};
```