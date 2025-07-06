//Problem Name   : First digit
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int X;
    cin >> X;
    
    int firstDigit = X / 1000;
    
    if (firstDigit % 2 == 0) {
        cout << "EVEN" << endl;
    } else {
        cout << "ODD" << endl;
    }
    
    return 0;
}
