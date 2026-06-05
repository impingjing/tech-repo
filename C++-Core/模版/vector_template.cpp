#include <iostream>
using namespace std;

template <class T>
class Vector {
private:
    T* data;
    int size;
    int capacity;
    void ensure_capacity(int minCapacity) {
        if (capacity >= minCapacity) return;
        int newcap = capacity > 0 ? capacity : 1;
        while (newcap < minCapacity) newcap <<= 1;
        T* newdata = new T[newcap];
        for (int i = 0; i < size; ++i) newdata[i] = data[i];
        delete[] data;
        data = newdata;
        capacity = newcap;
    }
public:
    Vector(): data(nullptr), size(0), capacity(0) {}
    Vector(const Vector& other): data(nullptr), size(other.size), capacity(other.capacity) {
        if (capacity > 0) {
            data = new T[capacity];
            for (int i = 0; i < size; ++i) data[i] = other.data[i];
        }
    }
    Vector& operator=(const Vector& other) {
        if (this == &other) return *this;
        T* newdata = nullptr;
        if (other.capacity > 0) {
            newdata = new T[other.capacity];
            for (int i = 0; i < other.size; ++i) newdata[i] = other.data[i];
        }
        delete[] data;
        data = newdata;
        size = other.size;
        capacity = other.capacity;
        return *this;
    }
    ~Vector() { delete[] data; }

    int add(const T& val) {
        ensure_capacity(size + 1);
        data[size] = val;
        int idx = size;
        ++size;
        return idx;
    }
    int get_size() const { return size; }
    T& operator[](int idx) { return data[idx]; }
    const T& operator[](int idx) const { return data[idx]; }
    void remove(int idx) {
        if (idx < 0 || idx >= size) return;
        for (int i = idx; i + 1 < size; ++i) data[i] = data[i+1];
        --size;
    }
};
int main()
{
    Vector<int> vint;
    int n,m;
    cin >> n >> m;
    for ( int i=0; i<n; i++ ) {
        //    add() can inflate the vector automatically
        vint.add(i);    
    }
    //    get_size() returns the number of elements stored in the vector
    cout << vint.get_size() << endl;
    cout << vint[m] << endl;
    //    remove() removes the element at the index which begins from zero
    vint.remove(m);
    cout << vint.add(-1) << endl;
    cout << vint[m] << endl;
    Vector<int> vv = vint;
    cout << vv[vv.get_size()-1] << endl;
    vv.add(m);
    cout << vint.get_size() << endl;
}
