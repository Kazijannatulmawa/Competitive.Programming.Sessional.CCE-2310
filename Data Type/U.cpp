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
