num1 = [1, 7, 11]
num2 = [2, 4, 6]
k = 7


def small(num1, num2):
    if (num1 == [] or num2 == []):
        return []
    x = 0
    y = 0
    len2 = len(num2)
    maxsum = max(num1) + max(num2) + 1
    now = [0] * len(num1)
    cache = [0] * len(num1)
    for i in range(0, len(num1)):
        cache[i] = num1[i] + num2[0]
    p = 0
    answer = []
    while x < len(num1):
        y = cache.index(min(cache))
        if now[y] < len2:
            answer.append([num1[y], num2[now[y]]])
            now[y] = now[y] + 1
            if now[y] == len2:
                cache[y] = maxsum
            else:
                cache[y] = num1[y] + num2[now[y]]
            p = p + 1
            if p == k:
                return answer
        else:
            return answer
    y = 0
    len2 = len(num2)
    maxsum = max(num1) + max(num2) + 1
    now = [0] * len(num1)
    cache = [0] * len(num1)
    for i in range(0, len(num1)):
        cache[i] = num1[i] + num2[0]
    p = 0
    answer = []
    while x < len(num1):
        y = cache.index(min(cache))
        if now[y] < len2:
            answer.append([num1[y], num2[now[y]]])
            now[y] = now[y] + 1
            if now[y] == len2:
                cache[y] = maxsum
            else:
                cache[y] = num1[y] + num2[now[y]]
            p = p + 1
            if p == k:
                return answer
        else:
            return answer
print(small(num1, num2))
