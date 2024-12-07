# 12페이지 구현, 정점 다 지나게

import heapq

def tsp_a_star(graph, start):
    n = len(graph)  # 노드의 수
    # 초기 상태: (f_cost, g_cost, current_node, visited_mask, path)
    open_set = []
    heapq.heappush(open_set, (0, 0, start, 1 << (start - 1), [start]))

    # 최단 경로 비용과 경로 저장
    best_cost = float('inf')
    best_path = []

    while open_set:
        f_cost, g_cost, current, visited, path = heapq.heappop(open_set)

        # 모든 노드를 방문하고 시작점으로 돌아온 경우
        if visited == (1 << n) - 1:  # 모든 노드 방문
            if start in [neighbor for neighbor, _ in graph[current]]:  # 시작점으로 돌아갈 수 있는 경우
                total_cost = g_cost + next(cost for neighbor, cost in graph[current] if neighbor == start)
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = path + [start]
            continue

        # 현재 노드에서 다른 노드로 이동
        for neighbor, cost in graph[current]:
            if visited & (1 << (neighbor - 1)):  # 이미 방문한 노드 무시
                continue

            next_visited = visited | (1 << (neighbor - 1))
            tentative_g_cost = g_cost + cost
            # 간단한 휴리스틱: 남은 경로에 대한 추정값 (여기선 0으로 설정)
            heuristic = 0
            tentative_f_cost = tentative_g_cost + heuristic

            # 우선순위 큐에 추가
            heapq.heappush(open_set, (tentative_f_cost, tentative_g_cost, neighbor, next_visited, path + [neighbor]))

    return best_path, best_cost


# 그래프 데이터: (노드 번호 -> [(인접 노드, 가중치), ...])
graph = {
    1: [(2, 10), (3, 10), (4, 30), (5, 25)],
    2: [(1, 10), (3, 14), (4, 21), (5, 10)],
    3: [(1, 10), (2, 18), (4, 7),  (5, 9)],
    4: [(1, 8),  (2, 11), (3, 7),  (5, 3)],
    5: [(1, 14), (2, 10), (3, 10), (4, 3)]
}

# 시작 노드
start_node = 1

# A* 알고리즘 실행
path, cost = tsp_a_star(graph, start_node)

# 결과 출력
if path:
    print("최단 경로:", " -> ".join(map(str, path)))
    print("최단 경로 비용:", cost)
else:
    print("경로를 찾을 수 없습니다.")
