//Problem Name   : Convert To Decimal 2
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/17/2025
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t;
    cin>>t;
    while(t--)
  {
     long long n,one=0,r;
     cin>>n;
     while(n!=0)
   {
     r=n%2;
     if(r==1)one++;
     n=n/2;
   }
   long long ans= pow(2,one);
   cout<< ans -1<<endl;
  }
}
