//Problem Name   : Intervel Sweep 
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional 
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int a, b;
    cin >> a >> b;

    if (a == 0 && b == 0) {
        cout << "NO" << endl;
    } else if (a == b || a == b + 1 || b == a + 1) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
