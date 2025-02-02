def solution(numlist, n):
    num = {}
    for i in numlist:
        num[i] = abs(i-n)
        
    sorted_num = sorted(num.items(), key=lambda x: x[1])
    num_v = sorted(num.values())
    answer = []
    for i in range(len(sorted_num)):
        if sorted_num[i][0] not in answer:
            if num_v.count(sorted_num[i][1]) > 1:
                answer.append(max(sorted_num[i + 1][0], sorted_num[i][0]))
                answer.append(min(sorted_num[i + 1][0], sorted_num[i][0]))
            else:
                answer.append(sorted_num[i][0])
        else:
            pass
        
    return answer

'''
def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])

def solution(numlist, n):
    # num -> (abs(n-num), -num)
    numlist = [(abs(n-num), -num) for num in numlist]
    # 첫 번째 요소를 기준으로 오름차순 정렬 and 두 번째 요소를 기준으로 내림차순 정렬
    numlist.sort()
    # 두 번쨰 요소만 반환
    return [-num for _, num in numlist]
'''