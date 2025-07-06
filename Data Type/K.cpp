//Problem Name   : Max and Min
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <iostream>
using namespace std;
int main()
{
  long long a,b,c;
  cin>>a>>b>>c;
  long long minimum = min(a, min(b,c));
  long long maximum = max(a, max(b,c));
  cout<< minimum << " " << maximum << endl;
}
