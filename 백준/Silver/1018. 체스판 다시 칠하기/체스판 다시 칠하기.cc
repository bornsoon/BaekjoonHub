#include<iostream>
using namespace std;

int main(void){
	cin.tie(NULL);     //입출력 묶음 해제
    ios_base::sync_with_stdio(false);

    int n, m , min, count;
    cin >> n >>m;

    char chess[n][m];

    for(int i =0 ; i < n; i++){
        for (int j = 0; j < m; j++){ 
            cin >> chess[i][j];
        }
    }

    n -= 8;
    m -= 8;
    min = 32;
    
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= m ; j++){
            count = 0;
            for(int k = 0; k < 8; k = k + 2){
                for(int l = 0; l < 8; l = l + 2){
                    if(chess[i + k][j + l] != 'W'){
                        count += 1;
                    }
                    if(chess[i + k][j + l + 1] != 'B'){
                        count += 1;
                    }
                    if(chess[i + k + 1][j + l] != 'B'){
                        count += 1;
                    }
                    if(chess[i + k + 1][j + l + 1] != 'W'){
                        count += 1;
                    }
                }
            }
            if(count > 64 - count){
                count = 64 - count;
            }
            if(min > count){
                min = count;
            }
        }
    }
    cout << min;
}