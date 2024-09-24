#include <iostream>

using namespace std;

int func(int k, int n) {
    int a[k + 1][n + 1] = {0};
    for(int i = 0; i <= n; i++) {
        a[0][i] = i;
    }

    for(int i = 1; i <= k; i++) {
        for(int j = 1; j <= n; j++) {
            a[i][j] = a[i][j - 1] + a[i - 1][j];
        }
    }  
    return a[k][n];
}

int main() {
    int T, k, n;

    scanf("%d", &T);

    for(int i = 0; i < T; i++) {
        scanf("%d", &k);
        scanf("%d", &n);
        printf("%d\n", func(k, n));
    }

    return 0;
}
