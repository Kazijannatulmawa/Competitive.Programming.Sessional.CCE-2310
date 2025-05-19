//Problem Name   :  PUM
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : May/05/2025
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int x = 1;
    for (int i = 1; i <= N; i++) {
        cout << x << " " << x + 1 << " " << x + 2 << " PUM" << endl;
        x += 4;
    }

    return 0;
}
