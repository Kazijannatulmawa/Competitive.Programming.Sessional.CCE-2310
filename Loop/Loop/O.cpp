//Problem Name   : Pyramid
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/10/2025
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long row;
    cin>>row;
    for(long long line=1; line<=row;line++)
    {
        for(long long star=1;star<=line;star++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    }