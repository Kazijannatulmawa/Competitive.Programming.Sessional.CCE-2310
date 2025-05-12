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
