import pytest

@pytest.fixture
def sample_graph():
    from pygraph import create_graph, add_edge
    g = create_graph()
    add_edge(g, "A", "B")
    add_edge(g, "B", "C")
    add_edge(g, "C", "D")
    return g