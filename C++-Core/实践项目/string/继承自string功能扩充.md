# 继承自 string 的功能扩充

## 题目描述

> 
> 
> 
> 题目描述：
> 编写一个 MyString 类，该类公有继承自 C++ 标准库的 std::string 类。
> 
> 要求：
> 
> 1. 该类需要能够兼容 std::string 的所有基本功能（如直接赋值字符串字面量、使用 + 拼接等）。
> 2. 为 MyString 类增加一个新的功能：重载函数调用运算符 operator()(size_t start, size_t len)。
> 3. 该运算符的作用是返回从下标 start 开始，长度为 len 的子串（返回类型仍为 MyString）。
> 4. 提示：可以直接调用父类 std::string 的 substr 成员函数来实现该功能。
> 
> 程序功能要求：
> 程序读取一行原始字符串，然后读取两个整数 start 和 len。利用你编写的 MyString 类及其重载的 operator()，输出截取后的子串。
> 

## 代码实现

```cpp
#include <iostream>
#include <string>
using namespace std;

// MyString 类：公有继承自 std::string，扩展其功能
// MyString class: publicly inherits from std::string and extends its functionality
class MyString : public string {
public:
    // ===== 继承基类构造函数 =====
    // 使用 using 关键字继承 std::string 的所有构造函数
    // Inherit all constructors of std::string using the 'using' keyword
    // 好处：MyString 可以像 std::string 一样被构造
    // Benefit: MyString can be constructed just like std::string
    using string::string;
    
    // ===== 类型转换构造函数 =====
    // Convert std::string to MyString
    // 参数：const string& s - 待转换的 std::string 对象
    // Parameter: const string& s - the std::string object to be converted
    // 初始化列表：string(s) 调用父类构造函数进行初始化
    // Initializer list: string(s) calls parent class constructor for initialization
    MyString(const string& s) : string(s) {}
    
    // ===== 重载函数调用运算符 =====
    // Overload the function call operator (callable object)
    // 参数：
    //   size_t start - 子串的起始位置 / starting position of substring
    //   size_t len   - 子串的长度 / length of substring
    // 返回值：MyString 对象，包含提取的子串 / returns MyString object containing the extracted substring
    // const 修饰符：表示该函数不修改对象成员 / const qualifier indicates this function doesn't modify object members
    MyString operator()(size_t start, size_t len) const {
        // substr(start, len) 是 std::string 的成员函数，返回 std::string 对象
        // substr(start, len) is a member function of std::string, returns std::string object
        // 通过类型转换构造函数将其转换为 MyString 对象
        // Convert to MyString object via the type conversion constructor
        return MyString(substr(start, len));
    }
};

int main() {
    string inputStr;
    // 读取包含空格的整行字符串
    getline(cin, inputStr);
    
    int start, len;
    cin >> start >> len;

    // 将输入字符串转为自定义的 MyString 对象
    MyString ms = inputStr;
    
    // 调用重载的 operator() 并输出结果
    cout << ms(start, len) << endl;

    return 0;
}
```

## 知识点补充

### 1. 为什么要继承构造函数？(Why inherit constructors?)

**问题场景：** 如果不继承基类构造函数，子类对象的创建会很繁琐。

```cpp
// 不继承的情况下，需要为每种构造方式提供对应的子类构造函数
MyString s1("hello");              // ❌ 错误：没有这个构造函数
MyString s2(string("hello"));      // ❌ 错误：需要显式转换
MyString s3 = string("hello");     // ❌ 错误：没有对应的构造函数
```

**好处：** 继承构造函数可以让子类直接使用基类的所有构造函数，使接口更加一致。

```cpp
// 继承后，可以直接使用基类的构造函数
MyString s1("hello");              // ✅ 正确：继承了 string(const char*)
MyString s2(5, 'a');               // ✅ 正确：继承了 string(size_t, char)
MyString s3(string("hello"));      // ✅ 正确：继承了 string(const string&)
```

### 2. 怎样继承构造函数？(How to inherit constructors?)

**在 C++11 及以后版本中，使用 `using` 关键字：**

```cpp
class MyString : public string {
public:
    using string::string;  // 继承 string 的所有构造函数
};
```

**工作原理：**
- `using string::string;` 告诉编译器将 `std::string` 的所有构造函数引入到 `MyString` 的作用域中
- 编译器会自动为这些继承的构造函数生成对应的 `MyString` 版本
- 当创建 `MyString` 对象时，会自动调用相应的继承构造函数

**不同 C++ 版本的对比：**
| C++版本 | 方法 | 需要手动编写 |
|--------|------|-----------|
| C++11前 | 手动定义 | 每个基类构造函数都需要重新定义 |
| C++11及以后 | `using 基类::基类;` | 无需手动定义 |

### 3. 类型转换构造函数 (Type Conversion Constructor / Conversion Constructor)

**定义：** 只有一个参数的构造函数，能够将其他类型隐式转换为该类

```cpp
// 类型转换构造函数：从 std::string 转换为 MyString
MyString(const string& s) : string(s) {}
```

**作用与用法：**

```cpp
string inputStr = "hello";
MyString ms = inputStr;        // ✅ 隐式转换调用该构造函数
// 等价于：MyString ms = MyString(inputStr);

// 也可以显式调用
MyString ms2(inputStr);        // ✅ 显式调用类型转换构造函数
```

**为什么需要这个构造函数：**
- `std::string` 和 `MyString` 是不同的类型
- 虽然 `MyString` 继承了 `std::string` 的构造函数（如 `string(const char*)`），但无法直接处理已有的 `std::string` 对象
- 这个类型转换构造函数充当"桥梁"，使 `std::string` 能够被转换为 `MyString`

**`explicit` 关键字的影响：**

```cpp
// 允许隐式转换（推荐）
MyString(const string& s) : string(s) {}

// 禁止隐式转换，只允许显式转换
explicit MyString(const string& s) : string(s) {}

// 当使用 explicit 时
string inputStr = "hello";
MyString ms1 = inputStr;          // ❌ 编译错误：隐式转换被禁止
MyString ms2(inputStr);           // ✅ 正确：显式调用
```

### 4. 函数调用运算符重载 (Function Call Operator Overload / Callable Object)

**语法：** `ReturnType operator()(参数列表) const/非const {}`

**作用：** 让对象可以像函数一样被调用

```cpp
MyString operator()(size_t start, size_t len) const {
    return MyString(substr(start, len));
}

// 使用方式
MyString ms("hello world");
MyString sub = ms(0, 5);           // 调用 operator()，得到 "hello"
// 等价于：MyString sub = ms.operator()(0, 5);
```

**const 修饰符的含义：**
- `const` 修饰整个函数，表示该函数**不会修改对象的任何成员变量**
- 在这个例子中，提取子串不需要修改原字符串，所以使用 `const`

**其他 operator() 的例子：**

```cpp
// 函数对象（Function Object / Functor）
class Multiplier {
    int factor;
public:
    Multiplier(int f) : factor(f) {}
    int operator()(int x) const { return x * factor; }
};

Multiplier times3(3);
cout << times3(10);  // 输出：30，调用了 operator()(10)
```

### 5. 继承、构造函数初始化列表、类型转换流程总结

```cpp
// 完整的继承和转换流程演示：

string inputStr = "hello";           // 1. 创建 std::string 对象

MyString ms = inputStr;              // 2. 隐式调用类型转换构造函数
                                     //    MyString(const string& s) 被触发

// 此时调用过程：
// a) 识别 inputStr 是 std::string，ms 需要 MyString
// b) 查找接受 std::string 的构造函数
// c) 找到 MyString(const string& s)，进行隐式转换
// d) 在初始化列表中调用 string(s)（基类构造函数）初始化基类部分
// e) MyString 对象成功创建

MyString result = ms(0, 5);          // 3. 调用 operator()
                                     //    substr() 返回 std::string
                                     //    隐式转换为 MyString（再次调用类型转换构造函数）
```

### 6. 常见易错点

| 问题 | 原因 | 解决方案 |
|------|------|--------|
| `using string::string;` 报错 | C++ 版本低于 C++11 | 升级编译器或手动定义构造函数 |
| 类型匹配错误 | 缺少类型转换构造函数 | 添加 `MyString(const string& s)` |
| `operator()` 调用失败 | 没有重载 `operator()` | 根据需求重载该运算符 |
| 隐式转换不发生 | 构造函数被声明为 `explicit` | 移除 `explicit` 或使用显式转换 |