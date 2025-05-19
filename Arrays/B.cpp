#include<bits/stdc++.h>
using namespace std;
int main()
{
   long long n,arr[n],x;
   for(int i=0;i<n;i++)
   {
    cin>>arr[i];
   }   
   cin>>x;
   bool flag=false;
   for(int j=0;j<n;j++)
   {
     if(arr[j]==x)
     {
        flag=true;
        cout<<j<<endl;
        break;
     }
     if(flag)
     cout<<-1<<endl;
   }

}    