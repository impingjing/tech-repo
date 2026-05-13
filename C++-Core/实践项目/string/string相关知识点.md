# String

## 1. 基础定义与初始化

`std::string` 本质上是 `std::basic_string<char>` 的一个特化版本。

```cpp
string s1;                   // 默认初始化，空字符串
string s2 = "hello";         // 拷贝初始化
string s3("world");          // 直接初始化
string s4(s2);               // 拷贝构造
string s5(5, 'a');           // 生成 "aaaaa"
string s6("abcdef", 3);      // 取前3个字符，生成 "abc"
```

## 2. 容量操作

- `size() length()` ：返回字符个数
    - 二者完全一样，均返回字符的个数，不包含结尾的 `\0`
- `empty()` ：判断是否为空
- `capacity()` ：底层分配的内存空间大小
    - `capacity` 永远大于等于 `size` ，字符串的“总容量”
- `reserve(n)` ：与分配内存，减少多次扩容带来的性能开销
    - 仅仅开辟空间，不改变字符串的内容，也不改变 `size`
    - **避免频繁扩容:** 如果预知字符串会很大，提前调用 `reserve()`。
        
        ```cpp
        string s;
        s.reserve(1000); //提前扩容到1000，提高效率
        cout << s.size(); //输出0
        cout << s.capacity(); //输出100（或更大的数）
        ```
        
        - 坑！reserve 之后直接用下标赋值
        
        ```cpp
        string s;
        s.reserve(100); 
        s[0] = 'a'; // 错误！虽然有空间，但 size 还是 0，下标访问越界。
        ```
        
- `resize(n)` ：改变字符串长度，多出的部分用默认值填充
    - **作用：** 真正**改变字符串的长度**（`size`）。
    - **两种情况：**
        1. **变长：** `s.resize(10, 'a')`。如果原长为 5，则在末尾填充 5 个 'a'。
        2. **变短：** `s.resize(2)`。截断字符串，只保留前 2 个字符，多余的内存空间（`capacity`）通常不会释放。

## 3. 访问与遍历

访问字符时注意**边界检查**！

- 下标访问：`s[i]` （不检查越界，速度快）或 `s.at(i)` （检查越界，抛出异常）
- 首尾访问： `front()` 和 `back()`
- 遍历方式：
    
    ```cpp
    // 1. 范围 for 循环 (C++11)
    for (char c : s) { ... }
    // 2. 迭代器遍历
    for (auto it = s.begin(); it != s.end(); ++it) { ... }
    ```
    

## 4. 修改与连接

string 支持重载运算符

- **拼接：** 使用 `+` 或 `+=` 运算符，或者使用 `append()` 方法。
- **插入：** `insert(pos, str)` 在指定位置插入字符串。
- **删除：** `erase(pos, len)` 从 `pos` 开始删除 `len` 个字符。
- **替换：** `replace(pos, len, str)`。
- **清空：** `clear()`。

## 5. 查找与子串处理

- **查找：** `find(str, pos)` 返回第一次出现的位置，若未找到则返回 `string::npos`。
    
    ```cpp
    string s = "Hello C++ World, Hello Code!";
    
    // 1. 查找子串
    size_t pos1 = s.find("Hello");      // 返回 0 (第一次出现的位置)
    
    // 2. 从指定位置开始查找
    size_t pos2 = s.find("Hello", 5);   // 返回 17 (跳过前5个字符开始找)
    
    // 3. 查找单个字符
    size_t pos3 = s.find('+');          // 返回 7
    ```
    
    - 还有 `rfind()` (逆向查找), `find_first_of()`, `find_last_of()` 等。
- **截取子串：** `substr(pos, len)` 返回从 `pos` 开始的 `len` 个字符组成的**新字符串**。
- 应用：用于提取文件名

```cpp
string path="user/bin/g++";

size_t last_slash=path.find('/');
string filename=path.substr(last_slash+1); //得到 "g++"
```

## 6. 与C风格字符串的转换

在调用底层 C API 时，经常需要这种转换。

- *string 转 char：*`s.c_str()` 返回一个以 `\0` 结尾的常量字符数组指针。
- *char 转 string：*直接赋值或构造即可。

## 7. 数值转换

方便地在字符串与数值类型（int, double 等）之间切换。

- **数值转字符串：** `to_string(val)`。
- **字符串转数值：** * `stoi()` (int), `stol()` (long), `stod()` (double) 等。

## 8. 常用算法配合

`string` 可以无缝配合 `<algorithm>` 库：

- **排序：** `sort(s.begin(), s.end());`
- **反转：** `reverse(s.begin(), s.end());`
