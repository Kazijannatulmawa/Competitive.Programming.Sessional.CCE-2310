//Problem Name   : Float or int
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    double N;
    cin >> N;

    int integerPart = N;
    double decimalPart = N - integerPart; 

    if (decimalPart == 0) {
        cout << "int " << integerPart << endl;
    } else {
        cout << "float " << integerPart << " " << fixed << setprecision(3) << decimalPart << endl;
    }

    return 0;
}
