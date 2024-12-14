#include <iostream>
using namespace std;

int n0 = 0, n1 = 0;
int m[40][2] = {0,};

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, t;
    void fibo(int n);
    cin >> t;
    
    m[0][0] = 1;
    m[1][1] = 1;
    
    for(int i = 0; i < t; i++) {
        cin >> n;
        if (n > 1) {
            fibo(n);
        }
        cout << m[n][0] << ' ' << m[n][1] << '\n';
    }
    
    return 0;
}

void fibo(int n) {
    if (m[n-1][0] == 0 && m[n-1][1] == 0) {
        fibo(n-1);
    }
    if (m[n-2][0] == 0 && m[n-2][1] == 0) {
        fibo(n-2);
    }
    m[n][0] = m[n-1][0] + m[n-2][0];
    m[n][1] = m[n-1][1] + m[n-2][1];
}