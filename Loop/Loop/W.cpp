//Problem Name   :  Shape3
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/17/2025
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long row;
    cin>>row;
    for(long long line=1;line<=row;line++)
    {
        for(long long space=1;space<=(row-line);space++)
        {
            cout<<" ";
        }
        for(long long star=1;star<=((line*2)-1);star++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    for(long long line=row;line>=1;line--)
    {
        for(long long space=1;space<=(row-line);space++)
        {
            cout<<" ";
        }
        for(long long star=1;star<=((line*2)-1);star++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
}