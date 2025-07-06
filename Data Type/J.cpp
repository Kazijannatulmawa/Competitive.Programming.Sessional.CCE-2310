//Problem Name   : Multipuls
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 24.02.25
#include <iostream>
using namespace std;
int main()
{
  long long a,b;
  cin>> a >> b;
  if(a%b==0||b%a==0)
  {
    cout<< "Multiples"<<endl;
  }
  else
  {
    cout<< "No Multiples"<<endl;
  }
}
