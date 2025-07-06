//Problem Name   : Age in Days
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    int years = N / 365;
    int months = (N % 365) / 30;
    int days = (N % 365) % 30;
    cout << years << " years" << endl;
    cout << months << " months" << endl;
    cout << days << " days" << endl;
     return 0;
}
