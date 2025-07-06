//Problem Name   : Coordinates of a Point
//Teacher’s Name : Mirza Raquib
//Course Title   : Competitive programming sessional
//Course Code    : CCE-2310
//Date           : 04.05.25
#include <bits/stdc++.h>
using namespace std;
int main() {
    double X, Y;
    cin >> X >> Y;

    if (X == 0 && Y == 0) {
        cout << "Origem" << endl;
    } else if (Y == 0) {
        cout << "Eixo X" << endl;
    } else if (X == 0) {
        cout << "Eixo Y" << endl;
    } else if (X > 0 && Y > 0) {
        cout << "Q1" << endl;
    } else if (X < 0 && Y > 0) {
        cout << "Q2" << endl;
    } else if (X < 0 && Y < 0) {
        cout << "Q3" << endl;
    } else {
        cout << "Q4" << endl;
    }

    return 0;
}
