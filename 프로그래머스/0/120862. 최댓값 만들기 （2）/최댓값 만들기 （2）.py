def solution(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    numbers.remove(max2)
    m_max = max1 * max2
    
    if len(numbers) == 0:
        return m_max
    
    if len(numbers) == 1:
        if max2 >= 0:
            return m_max
        else:
            return max2 * numbers[0]
    elif max2 >= 0:
        min1 = min(numbers)
        numbers.remove(min1)
        min2 = min(numbers)
        numbers.remove(min2)
        m_min = min1 * min2
        
        if m_min > m_max:
            return m_min
        else:
            return m_max