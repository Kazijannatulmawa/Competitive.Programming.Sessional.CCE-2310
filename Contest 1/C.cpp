//Problem Name   : Alphabet  
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional 
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    char C;
    cin >> C;

    if (C == 'z') {
        cout << 'a' << endl;
    } else {
        cout << char(C + 1) << endl;
    }

    return 0;
}
