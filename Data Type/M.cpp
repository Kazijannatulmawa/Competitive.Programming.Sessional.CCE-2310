//Problem Name   : Capital or Small or Digit
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include<bits/stdc++.h>
using namespace std;
int main()
{
    char c;
    cin>> c;
    if (c >= 97 && c <= 122)
    {
        cout<< "ALPHA" <<endl;
        cout<< "IS SMALL" <<endl;
    }
    else if (c >= 65 && c <= 90)
    {
        cout<< "ALPHA" <<endl;
        cout<< "IS CAPITAL" <<endl;
    }
    else
    {
        cout <<"IS DIGIT"<<endl;
    }
}
