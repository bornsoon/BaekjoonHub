#include <stdio.h>
#include <math.h>

int main() {
    int a, b, c, d, e;
    int answer, sum;
    
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    sum = pow(a, 2) + pow(b, 2) + pow(c, 2) + pow(d, 2) + pow(e, 2);
    answer = (int)sum % 10;
    printf("%d", answer);
    return 0;
}