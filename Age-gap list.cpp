#include <bits/stdc++.h>
using namespace std;
int main(){
    int MaleAge;
    cin >> MaleAge;
    for( int i = 14; i <= MaleAge; i++){
        cout << i << " - " << (i / 2) +7  << "\n";
    }
    return 0;
}
