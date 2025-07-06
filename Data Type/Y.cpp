//Problem Name   : The last 2 digits
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

    // Extract last two digits of each number
    A %= 100;
    B %= 100;
    C %= 100;
    D %= 100;

    // Compute the last two digits of the multiplication
    long long result = (A * B * C * D) % 100;

    // Ensure two-digit output
    if (result < 10) {
        cout << "0" << result << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}
