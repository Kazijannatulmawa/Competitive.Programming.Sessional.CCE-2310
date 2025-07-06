//Problem Name   : Memo and Momo 
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional 
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long a, b, k;
    cin >> a >> b >> k;

    if (a % k == 0 && b % k == 0) {
        cout << "Both" << endl;
    } else if (a % k == 0) {
        cout << "Memo" << endl;
    } else if (b % k == 0) {
        cout << "Momo" << endl;
    } else {
        cout << "No One" << endl;
    }

    return 0;
}
