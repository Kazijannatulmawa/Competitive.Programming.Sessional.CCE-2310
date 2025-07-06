//Problem Name   : Alibaba and puzzles 
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional 
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long A, B, C, D;
    cin >> A >> B >> C >> D;

    if ((A + B - C == D) || (A + B * C == D) || (A - B + C == D) || 
        (A - B * C == D) || (A * B + C == D) || (A * B - C == D)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
