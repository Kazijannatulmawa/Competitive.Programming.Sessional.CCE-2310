//Problem Name   : Two intervals
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long l1, r1, l2, r2;
    cin >> l1 >> r1 >> l2 >> r2;

    if (l1 <= r2 && l2 <= r1) {
        cout << max(l1, l2) << " " << min(r1, r2) << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}
