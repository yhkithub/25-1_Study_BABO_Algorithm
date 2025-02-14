# 프로그래머스- 주식가격
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    
    return answer

# 백준 1743 음식물 피하기

def dfs(x, y, graph, visited):
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]
    visited[x][y] = True
    count = 1  # 음식물 크기

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 음식물이 있고, 방문하지 않았다면
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count

def solution(N, M, K, food_locations):
    # 통로 초기화 (0으로 채움)
    graph = [[0] * M for _ in range(N)]
    for r, c in food_locations:
        graph[r-1][c-1] = 1

    visited = [[False] * M for _ in range(N)]
    max_food_size = 0

    # 각 위치에서 DFS 탐색
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                max_food_size = max(max_food_size, dfs(i, j, graph, visited))

    return max_food_size

# 입력 예시
N, M, K = 3, 4, 5
food_locations = [(3, 2), (2, 2), (3, 1), (2, 3), (1, 1)]

print(solution(N, M, K, food_locations))  # 출력: 4
