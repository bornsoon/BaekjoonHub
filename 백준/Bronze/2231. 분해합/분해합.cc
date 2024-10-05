#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main() {
    string s;

    cin >> s;

    int digits = s.length() -1;
    int n = stoi(s);
    int answer = n;
    int m = n - 1;

    while(m > n - 9 * (digits + 1)){
        int temp = m;
        int a = m;
        for(int i = digits; i >= 0; i--){
            temp += a / pow(10, i);
            a = a % int(pow(10, i));
        }
        
        if(temp == n && m < answer){
            answer = m;
        }
        m--;
    }

    if(answer != n){
        cout << answer;
    } else {
        cout << 0;
    }
    
    return 0;
}