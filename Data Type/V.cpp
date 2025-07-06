//Problem Name   : Comperison
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int A, B;
    char S;
    cin >> A >> S >> B;

    if ((S == '<' && A < B) || (S == '>' && A > B) || (S == '=' && A == B)) 
    {
        cout << "Right" << endl;
    } else {
        cout << "Wrong" << endl;
    }

    return 0;
}
