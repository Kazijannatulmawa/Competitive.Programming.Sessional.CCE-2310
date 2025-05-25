//Problem Name   : Max
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive Programming Sessional 
//Course Code    : CCE-2310
//Date           : Mar/03/2025
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int maxNum = arr[0];
    for (int i = 1; i < N; i++) {
        if (arr[i] > maxNum) {
            maxNum = arr[i];
        }
    }

    cout << maxNum << endl;
    return 0;
}
