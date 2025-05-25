//Problem Name   : Even, Odd, Positive and Negative
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/03/2025
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n;
    cin>>n;
    long long even=0, odd=0, pos=0,neg=0;
    long long a;
    for(int i=1;i<=n;i++)
    {
        cin>>a;
        if(a%2==0)even++;
        if(a%2!=0)odd++;
        if(a>0)pos++;
        if(a<0)neg++;
    }
    cout<<"Even: "<<even<<endl;
    cout<<"Odd: "<<odd<<endl;
    cout<<"Positive: "<<pos<<endl;
    cout<<"Negative: "<<neg<<endl;
}

