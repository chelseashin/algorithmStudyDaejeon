import sys
sys.stdin = open('17136_input.txt')

# cnt : 사용한 색종이 수, raw 에서 남은 1의 수, 시작 행 넘겨주면서 최적화
def dfs(cnt, t, start):
    global min_count
    # 색종이로 다 덮었을 때, 최소 사용 갯수 갱신
    if t == 0:
        if min_count > cnt:
            min_count = cnt
    # 가지치기(현재까지의 사용 갯수가 최소 갯수보다 많으면 리턴
    elif cnt >= min_count:
        return
    # 종이 이미 다 사용하면
    elif sum(paper) == 0:
        return
    else:
        # 색종이 붙이기
        for i in range(start, 10):
            for j in range(10):
                if raw[i][j] == 1 and visited[i][j] == 0:
                    # 5*5 사이즈부터 1*1 사이즈 순으로 붙여보기
                    for size in range(5, 0, -1):
                        # 범위 넘어가지 않고
                        if not (i+size <= N and j+size <= N):
                            continue
                        # 붙일 수 있는 종이 남아 있으면
                        if paper[size] > 0:
                            cover = 0
                            for r in range(i, i+size):
                                for c in range(j, j+size):
                                    if visited[r][c] == 0:
                                        cover += raw[r][c]
                            # 덮이면
                            if cover == size * size:
                                for r in range(i, i+size):
                                    for c in range(j, j+size):
                                        visited[r][c] = 1
                                paper[size] -= 1
                                dfs(cnt + 1, t - size * size, i)
                                paper[size] += 1
                                for r in range(i, i+size):
                                    for c in range(j, j+size):
                                        visited[r][c] = 0
                    return

N = 10
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * 10 for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
min_count = float('inf')

temp = 0
for i in range(N):
    for j in range(N):
        if raw[i][j]:
            temp += 1
dfs(0, temp, 0)
if min_count == float('inf'):
    min_count = -1

print(min_count)