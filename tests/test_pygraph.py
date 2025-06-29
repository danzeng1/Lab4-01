from pygraph import Graph

def test_add_node():
    """测试添加节点"""
    g = Graph()
    g.add_node("A")
    assert g.has_node("A") is True
    assert g.get_nodes() == ["A"]

def test_add_edge():
    """测试添加无向边"""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B")
    
    assert g.has_edge("A", "B") is True
    assert g.has_edge("B", "A") is True
    assert g.get_edges() == [("A", "B")]

def test_get_neighbors():
    """测试获取邻居"""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    
    assert g.get_neighbors("A") == ["B", "C"]
    assert g.get_neighbors("D") == []  # 不存在的节点

def test_remove_node():
    """测试移除节点"""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B")
    
    g.remove_node("A")
    assert g.has_node("A") is False
    assert g.has_edge("A", "B") is False
    assert "A" not in g.get_neighbors("B")

def test_remove_edge():
    """测试移除边"""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_edge("A", "B")
    
    g.remove_edge("A", "B")
    assert g.has_edge("A", "B") is False
    assert g.get_edges() == []

def test_get_nodes_and_edges():
    """测试获取所有节点和边"""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    
    assert g.get_nodes() == ["A", "B", "C"]
    assert g.get_edges() == [("A", "B"), ("B", "C")]
