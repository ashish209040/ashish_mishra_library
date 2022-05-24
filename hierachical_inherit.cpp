#include <bits/stdc++.h>
using namespace std;
class a{
public:
    a(){
        cout<<"hello, this is class A"<<endl;
    }
};
class b:public a{
public:
    b(){
        cout<<"this is 1st derived class"<<endl;
    }
};
class c{
public:
    c(){
        cout<<"this is again a base class"<<endl;
    }
};
class d:public c, public b{
public:
    d(){
        cout<<"this is the lowest derived class"<<endl;
    }
};
int main(){
    d d1;
}
