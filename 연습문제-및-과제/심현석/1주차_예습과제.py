# p.87

n = int(input())    # 입력받은 돈 
count = 0           # 동전 개수

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin  # 현재 금액에서 거슬러줄 수 있는 동전의 개수
    n %= coin           # 동전을 거슬러 준 후 남은 금액

print(count)    # 동전 개수 출력

# ===============================================================
# p.99 실전문제 3

# 나의 답안
N,K = map(int,input().split())     # N, K를 공백으로 구분하여 입력받기
count = 0                          # 연산 횟수

while N >= K:           # 나눗셈 연산 => 값의 크기를 가장 빠르게 줄이는 목적 => N이 K 이상이어야 의미가 있음
    if N % K != 0:      # 나누어 떨어지지 않을 경우 1씩 빼주기
        N -= 1
    else:               # 나누어 떨어질 경우 나눗셈 연산 
        N //= K
    count += 1          # 연산 횟수 업데이트

while N > 1:            # N이 1이 될 때까지 반복하여 1을 빼주기
    N -= 1
    count += 1          # 연산 횟수 업데이트

print(count)            # 연산 횟수 출력

# 교재의 답안
n, k = map(int, input().split())    # N, K를 공백으로 구분하여 입력받기
result = 0                          # 연산 횟수
while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k    # 몫×(나누어준 수)
    result += (n- target)    # N을 K로 나누었을 때 나머지를 계산하여 result에 한번에 업데이트 (즉, 1을 일일이 빼줄 필요가 없음)
    n = target               # N을 K로 나누었을 때 나머지

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나눈 나머지 계산
    result += 1              # 나눗셈 연산을 수행하므로 result에 연산 횟수 1회 업데이트
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)            # N이 1이 될 때까지 "1씩 빼는 연산"을 해야하는 횟수를 result에 한번에 업데이트
print(result)                # 연산 횟수 출력
