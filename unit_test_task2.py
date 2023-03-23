import unittest

from module_lab2_task2 import Network


class TestNetworkMethods(unittest.TestCase):

    def test_add_node(self):
        network = Network()
        network.add_node("A")
        network.add_node("B")

        self.assertEqual(len(network.nodes), 2)

    def test_add_arc(self):
        network = Network()
        node_a = network.add_node("A")
        node_b = network.add_node("B")
        network.add_arc(node_a, node_b, 5.0)

        self.assertEqual(len(network.arcs), 1)

    def test_read_network(self):
        network = Network()
        network.read_network("network.txt")

        self.assertEqual(len(network.nodes), 6)
        self.assertEqual(len(network.arcs), 9)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
