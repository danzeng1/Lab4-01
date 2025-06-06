import pytest
from pygraph import Graph, create_graph, add_vertex, add_edge, get_vertices, get_edges, is_connected, find_path

def test_graph_creation():
    g = create_graph()
    assert isinstance(g, Graph)

def test_add_vertex():
    g = create_graph()
    add_vertex(g, "A")
    assert "A" in get_vertices(g)

def test_add_edge():
    g = create_graph()
    add_edge(g, "A", "B")
    assert ("A", "B") in get_edges(g)

def test_is_connected():
    g = create_graph()
    add_edge(g, "A", "B")
    assert is_connected(g, "A", "B") is True
    assert is_connected(g, "B", "A") is False

def test_find_path():
    g = create_graph()
    add_edge(g, "A", "B")
    add_edge(g, "B", "C")
    assert find_path(g, "A", "C") == ["A", "B", "C"]
    assert find_path(g, "C", "A") is None

def test_empty_path():
    g = create_graph()
    assert find_path(g, "A", "B") is None