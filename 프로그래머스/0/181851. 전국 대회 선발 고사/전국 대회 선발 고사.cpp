#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> rank, vector<bool> attendance) {
    vector<int> temp;
    
    for (int i = 0; i < rank.size(); i++) {
        int j = rank[i] * attendance[i];
        if(j) temp.push_back(j);
    };
    sort(temp.begin(), temp.end());
    
    int a = find(rank.begin(), rank.end(), temp[0]) - rank.begin();
    int b = find(rank.begin(), rank.end(), temp[1]) - rank.begin();
    int c = find(rank.begin(), rank.end(), temp[2]) - rank.begin();
    
    int answer = 10000 * a + 100 * b + c;

    return answer;
}