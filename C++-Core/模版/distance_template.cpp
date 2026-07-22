#include <iostream>
#include <cmath>
using namespace std;

template < class T> 
double dist(const T& a, const T& b){
    double d = b - a;
    return d < 0 ? -d : d;
}
class point{
private:
    int x;
    int y;
    int z;
public:
    //构造函数
    point()=default; //默认构造函数
    point(int a,int b,int c):x(a),y(b),z(c){} //有参构造函数
    friend double operator-(const point& p1,const point& p2);
    friend istream& operator>>(istream& in,point& p);
};
//重载-
double operator-(const point& p1,const point& p2){
    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;
    int dz = p2.z - p1.z;
    long long sum = 1LL*dx*dx + 1LL*dy*dy + 1LL*dz*dz;
    return sqrt((double)sum);
}
//重载>>
istream& operator>>(istream& in,point& p){
    in>>p.x>>p.y>>p.z;
    return in;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n=1;
    cin>>n;
    while(n!=0){
        switch(n){
            case 1:
                int a,b;
                cin>>a>>b;
                cout<<dist(a,b)<<"\n";
                break;
            case 2:
                float f1,f2;
                cin>>f1>>f2;
                cout<<dist(f1,f2)<<"\n";
                break;
            case 3:
                point p1,p2;
                cin>>p1>>p2;
                cout<<dist(p1,p2)<<"\n";
                break;
        }
        cin>>n;
    }
    return 0;
}