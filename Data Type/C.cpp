//Problem Name   : Simple calculator
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 24.02.25
#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long X, Y;
    cin >> X >> Y;
    if (X <= 1 || X >= 100000 || Y <= 1 || Y >= 100000) 
{
    return 0; 
} 
    cout << X << " + " << Y << " = " << X + Y << endl;
    cout << X << " * " << Y << " = " << X * Y << endl;
    cout << X << " - " << Y << " = " << X - Y << endl;
    return 0;
}
