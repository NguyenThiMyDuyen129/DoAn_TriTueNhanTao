import math # thư viện toán học
import random # thư viện sinh số ngẫu nhiên
import networkx as nx # thư viện đồ thị
import matplotlib.pyplot as plt # thư viện vẽ đồ thị
import os # thư viện thao tác hệ thống các phương thuc với file và thư mục

# Các hàm tiện ích chung cho đồ thị
# in ma trận kề, nhập đỉnh, heuristic Euclid,
def print_adjacency_matrix(vertices, adj): #vertices: danh sách đỉnh, adj: ma trận kề
    """In ma trận kề có tiêu đề"""
    n = len(vertices) # số đỉnh
    print("\nMa tran ke cua do thi:")
    print("    " + " ".join(vertices)) # in tiêu đề cột
    for i in range(n):
        print(vertices[i] + " | " + " ".join(map(str, adj[i]))) # in mỗi hàng với tiêu đề hàng

# nhập đỉnh hợp lệ đỉnh bắt đầu và kết thúc
def input_vertex(vertices, msg):
    """Nhập đỉnh hợp lệ"""
    while True:
        v = input(msg).strip().upper()
        if v in vertices:
            return v
        print("Nhap sai. Cac dinh hop le:", vertices)

# heuristic Euclid giữa hai đỉnh
def heuristic(u, v, pos):
    """Heuristic Euclid"""
    return math.dist(pos[u], pos[v])# ước lượng chi phí từ đỉnh hiện tại đến đích

# sinh đồ thị ngẫu nhiên, random ma trận kề với trong số cạnh từ 1-9
def generate_random_graph(n, min_degree=2):
    """Sinh đồ thị vô hướng có trọng số"""
    vertices = [chr(ord('A') + i) for i in range(n)] # Đặt tên đỉnh từ A, B, C, ...
    adj = [[0]*n for _ in range(n)]# Ma trận kề ban đầu với tất cả các cạnh bằng 0

    # Đảm bảo đồ thị liên thông và không có đỉnh cô lập
    # thực hiện bằng cách kết nối mỗi đỉnh i với đỉnh i+1
    for i in range(n):# Đảm bảo mỗi đỉnh có ít nhất trọng số tối thiểu
        while sum(1 for x in adj[i] if x > 0) < min_degree:# Đếm số cạnh hiện tại của đỉnh i
            j = random.randint(0, n-1) # Chọn ngẫu nhiên đỉnh j
            if i != j and adj[i][j] == 0: 
                w = random.randint(1, 9)
                adj[i][j] = w
                adj[j][i] = w

    G = nx.Graph()
    for v in vertices:
        G.add_node(v)

    for i in range(n):
        for j in range(i+1, n):
            if adj[i][j] > 0:
                G.add_edge(vertices[i], vertices[j], weight=adj[i][j])

    return G, vertices, adj


def load_graph_from_txt(filename="graph.txt"):
    """Load đồ thị từ file txt"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    n = int(lines[0])
    vertices = lines[1].split()
    adj = [list(map(int, lines[i+2].split())) for i in range(n)]

    G = nx.Graph()
    for v in vertices:
        G.add_node(v)

    for i in range(n):
        for j in range(i+1, n):
            if adj[i][j] > 0:
                G.add_edge(vertices[i], vertices[j], weight=adj[i][j])

    return G, vertices, adj

# xây dựng đường đi tạm thời từ cha đến con
def build_current_path(parent, current):
    """Dựng đường đi tạm thời"""
    path = [current]
    while parent[current] is not None:
        current = parent[current]
        path.append(current)
    return list(reversed(path))


def draw_step(G, pos, step, path_so_far=None):
    """Vẽ đồ thị từng bước, tô đỏ các cạnh đã đi"""
    plt.figure(figsize=(3, 3))

    nx.draw(
        G, pos,
        with_labels=True,
        node_size=550,
        node_color="orange",
        edge_color="black"
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')# Lấy nhãn trọng số cạnh
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) # Vẽ nhãn trọng số cạnh
    # Tô đỏ các cạnh trong đường đi đã đi
    if path_so_far and len(path_so_far) > 1:
        edges_path = list(zip(path_so_far[:-1], path_so_far[1:]))
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges_path,
            edge_color="red",
            width=3
        )

    plt.title(f"Step {step}")
    os.makedirs("steps", exist_ok=True)
    plt.savefig(f"steps/step_{step}.png")
    plt.show()

class AStar:
    def __init__(self, graph):
        self.graph = graph
        self.pos = nx.spring_layout(graph, seed=42)

    def h(self, node, goal): # hàm heuristic ước lượng chi phí từ node đến goal
        return heuristic(node, goal, self.pos)

    def f(self, node, g_cost, goal): # hàm f = g + h chi phí thực tế + ước lượng chi phí = chi phí tổng
        return g_cost[node] + self.h(node, goal)

    def reconstruct_path(self, parent, goal):# tái tạo đường đi từ cha đến con
        path = [goal] # bắt đầu từ đích
        while parent[goal] is not None: # lặp lại cho đến khi không còn cha
            goal = parent[goal] # di chuyển đến cha
            path.append(goal) # thêm cha vào đường đi
        return list(reversed(path)) # đảo ngược đường đi để có từ đầu đến đích

    def solve(self, start, goal):
        open_list = set([start]) # tập các đỉnh chưa được khám phá
        closed_list = set() # tập các đỉnh đã được khám phá

        g_cost = {start: 0} # chi phí từ đỉnh bắt đầu đến đỉnh hiện tại
        parent = {start: None} # từ cha đến con

        step = 0 # bước đếm

        while open_list: # trong khi còn đỉnh chưa khám phá
            # Hiển thị OPEN / CLOSED
            print("\nOPEN LIST:")
            for node in open_list:
                print(f"  {node}: g={g_cost[node]}, f={round(self.f(node, g_cost, goal), 2)}")
            print("CLOSED LIST:", closed_list)

            # Chọn node có f nhỏ nhất
            n = None # khởi tạo n là None để tìm đỉnh có f nhỏ nhất
            for node in open_list: # duyệt qua các đỉnh trong open_list
                if n is None or self.f(node, g_cost, goal) < self.f(n, g_cost, goal): # nếu n chưa được gán hoặc f(node) < f(n)
                    n = node

            step += 1
            print(f"\nBuoc {step}:")
            print(f"Chon dinh: {n}")
            print(f"g({n}) = {g_cost[n]}")
            print(f"f({n}) = {round(self.f(n, g_cost, goal), 2)}")

            current_path = build_current_path(parent, n)
            draw_step(self.graph, self.pos, step, current_path)

            if n == goal:
                print("→ GOAL duoc chon voi f nho nhat")
                return self.reconstruct_path(parent, goal)

            print("Mo cac dinh ke:")

            for m in self.graph.neighbors(n):
                if m in closed_list:
                    continue

                w = self.graph[n][m]['weight']
                tentative_g = g_cost[n] + w
                print(f"  g({n} -> {m}) = {g_cost[n]} + {w} = {tentative_g}")

                if m not in open_list: 
                    open_list.add(m)
                    parent[m] = n
                    g_cost[m] = tentative_g
                else:
                    if tentative_g < g_cost[m]:
                        g_cost[m] = tentative_g
                        parent[m] = n

            open_list.remove(n)
            closed_list.add(n)

        return None
