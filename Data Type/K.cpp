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