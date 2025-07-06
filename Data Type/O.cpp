//Problem Name   : Calculator
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int A, B;
    char S;
    cin >> A >> S >> B;
    
    if (S == '+') {
        cout << A + B << endl;
    } else if (S == '-') {
        cout << A - B << endl;
    } else if (S == '*') {
        cout << A * B << endl;
    } else if (S == '/') {
        cout << A / B << endl;
    }
    
    return 0;
}
