#include <iostream>
// #include <ctime>
using namespace std;

int k, n;

int main(void) {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int binarySearch(int lan[], long start, long end);
    // clock_t start, finish;
    // double duration;
    // start = clock();
    cin >> k >> n;
    int lan[k];

    long sum = 0;  // 변수 범위 주의

    for(int i = 0; i < k; i++) {
        cin >> lan[i];
        sum += lan[i];
    }

    long end = sum / n;
    
    int answer = binarySearch(lan, 1, end);

    cout << answer << '\n';

    // finish = clock();

    // duration = (double)(finish - start) / CLOCKS_PER_SEC;
    // cout << duration << "초";

    return 0;
}

int binarySearch(int lan[], long start, long end) {
    if (start > end) {
        return start - 1;
    }

    long long mid = (start + end) / 2;

    int total = 0;
    for (int i = 0; i < k && total < n; i++) {
        total += lan[i] / mid;
    }

    if (total >= n) {
        start = mid + 1;
    } else {
        end = mid -1;
    }

    return binarySearch(lan, start, end);
}