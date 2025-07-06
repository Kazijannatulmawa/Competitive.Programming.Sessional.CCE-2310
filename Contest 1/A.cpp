//Problem Name   : Winter Sale 
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional 
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    double X, P;
    cin >> X >> P;
    double originalPrice = P / (1 - X / 100.0);
    cout << fixed << setprecision(2) << originalPrice << endl;

    return 0;
}
