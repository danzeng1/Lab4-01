class Graph:
    def __init__(self):
        self.adj_list = {}  # 邻接表存储图结构

    def add_node(self, node: str) -> None:
        """添加节点，若节点已存在则忽略"""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1: str, node2: str) -> None:
        """添加无向边，需确保两个节点已存在"""
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def get_neighbors(self, node: str) -> list:
        """获取节点的邻居列表，若节点不存在返回空列表"""
        return self.adj_list.get(node, [])

    def has_node(self, node: str) -> bool:
        """检查节点是否存在"""
        return node in self.adj_list

    def has_edge(self, node1: str, node2: str) -> bool:
        """检查两个节点之间是否有边"""
        return node1 in self.adj_list and node2 in self.adj_list[node1]

    def remove_node(self, node: str) -> None:
        """移除节点及其关联的边"""
        if node in self.adj_list:
            # 移除所有与该节点相连的边
            for neighbor in self.adj_list[node]:
                self.adj_list[neighbor].remove(node)
            # 移除节点本身
            del self.adj_list[node]

    def remove_edge(self, node1: str, node2: str) -> None:
        """移除两个节点之间的边"""
        if node1 in self.adj_list and node2 in self.adj_list[node1]:
            self.adj_list[node1].remove(node2)
            self.adj_list[node2].remove(node1)

    def get_nodes(self) -> list:
        """返回所有节点"""
        return list(self.adj_list.keys())

    def get_edges(self) -> list:
        """返回所有边（无向边仅返回一次）"""
        edges = []
        for node in self.adj_list:
            for neighbor in self.adj_list[node]:
                if (neighbor, node) not in edges:
                    edges.append((node, neighbor))
        return edges
