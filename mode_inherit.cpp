#include <bits/stdc++.h>
using namespace std;
class a{
public:
    a(){
        cout<<"this id base class"<<endl;
    }
};
class b: public a{
public:
    b(){
        cout<<"this is derived 1 class"<<endl;
    }
};
class c: public b{
public:
    c(){
        cout<<"this is the derived 2"<<endl;
    }
};
int main(){
    a a1;
    cout<<"\n";
    b b1;cout<<"\n";
    c c1;cout<<"\n";

}
