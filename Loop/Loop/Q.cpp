//Problem Name   :  Digits
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/17/2025
#include<bits/stdc++.h>
using namespace std;
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
       string s;
       cin>>s;
       for(int i= s.size()-1;i>=0;i--)
       {
           cout<<s[i]-'0'<<" ";
       }
       cout<<endl;
   }
}