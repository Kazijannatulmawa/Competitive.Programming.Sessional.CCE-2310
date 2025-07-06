//Problem Name   : Hard Compare
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() {
    long double A, B, C, D;
    cin >> A >> B >> C >> D;

    long double x = B * log(A);
    long double y = D * log(C);

    if (x > y) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
