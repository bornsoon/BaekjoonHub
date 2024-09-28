#include <iostream>

int main() {
    char s[1001];
    int n;
    std::cin >> s >> n;
    std::cout << s[n - 1] << std::endl;
    return 0;
}