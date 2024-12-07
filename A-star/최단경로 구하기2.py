# 13페이지 구현, 정점 다 안 지나도 됨

import heapq

# A* 알고리즘 함수
def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start, 0, [start]))  # (f_cost, current, g_cost, path)
    visited = set()

    while open_set:
        f_cost, current, g_cost, path = heapq.heappop(open_set)

        # 목표에 도달한 경우
        if current == goal:
            return path, g_cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                tentative_g_cost = g_cost + cost
                heuristic_cost = heuristic(neighbor, goal)
                f_cost = tentative_g_cost + heuristic_cost
                heapq.heappush(open_set, (f_cost, neighbor, tentative_g_cost, path + [neighbor]))

    return None, float('inf')  # 경로를 찾지 못한 경우

# 그래프 데이터: 인접 리스트
graph = {
    1: [(2, 20)],
    2: [(5, 17)],
    3: [(1, 10), (2, 17), (4, 30), (5, 25), (6, 23)],
    4: [(1, 19), (7, 24)],
    5: [(8, 25), (9, 39)],
    6: [(4, 16), (5, 28), (7, 18)],
    7: [(10, 20)],
    8: [(9, 29)],
    9: [(6, 20), (10, 28)],
    10: []
}

# 단순한 휴리스틱 함수 (유클리드 거리 대체)
def heuristic(node, goal):
    return 0  # 거리 기반 정보가 없으므로 휴리스틱을 0으로 설정

# 시작 노드와 목표 노드
start_node = 3
goal_node = 10

# A* 실행
path, cost = a_star(graph, start_node, goal_node, heuristic)

# 결과 출력
if path:
    print("최단 경로:", " -> ".join(map(str, path)))
    print("최단 경로 비용:", cost)
else:
    print("경로를 찾을 수 없습니다.")
