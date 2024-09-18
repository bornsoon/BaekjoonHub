#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m, x;

    scanf("%d", &n);
    
    vector<int> a(n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    scanf("%d", &m);
    

    sort(a.begin(), a.end());
        
    for(int i = 0; i < m; i++) {
        scanf("%d", &x);
        if(binary_search(a.begin(), a.end(), x)) {
            printf("1\n");
        } else {
            printf("0\n");
        }
    }
    
    return 0;
}
