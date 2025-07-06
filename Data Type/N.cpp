//Problem Name   : Char
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    char X;
    cin >> X;
    
    if (X >= 'a' && X <= 'z') {
        X -= 32;
    } else if (X >= 'A' && X <= 'Z') {
        X += 32;
    }
    
    cout << X << endl;
    return 0;
}
