def solution(n):
    for i in range(1, n+1):
        if i ** 2 == n:
            return (i+1) ** 2
    return -1