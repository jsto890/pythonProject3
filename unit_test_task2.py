import unittest
import module_lab2_task2.py

class TestNetworkMethods(unittest.TestCase):

    def test_add_node(self):
        network = Network()
        network.add_node("A")
        network.add_node("B", 10)

        self.assertEqual(len(network.nodes), 2)
        self.assertEqual(network.nodes[0].name, "A")
        self.assertEqual(network.nodes[0].value, None)
        self.assertEqual(network.nodes[1].name, "B")
        self.assertEqual(network.nodes[1].value, 10)

        network.add_node("A", 20)
        self.assertEqual(len(network.nodes), 2)
        self.assertEqual(network.nodes[0].name, "A")
        self.assertEqual(network.nodes[0].value, None)

    def test_add_arc(self):
        network = Network()
        node_a = network.add_node("A")
        node_b = network.add_node("B")

        network.add_arc(node_a, node_b, 5.0)
        self.assertEqual(len(network.arcs), 1)
        self.assertEqual(network.arcs[0].source, node_a)
        self.assertEqual(network.arcs[0].destination, node_b)
        self.assertEqual(network.arcs[0].weight, 5.0)
        self.assertEqual(len(node_a.outbound_arcs), 1)
        self.assertEqual(len(node_b.inbound_arcs), 1)

    def test_read_network(self):
        network = Network()
        network.read_network("network.txt")

        self.assertEqual(len(network.nodes), 3)
        self.assertEqual(len(network.arcs), 2)

        node_a = network.get_node("A")
        node_b = network.get_node("B")
        node_c = network.get_node("C")

        self.assertIsNotNone(node_a)
        self.assertIsNotNone(node_b)
        self.assertIsNotNone(node_c)

        self.assertEqual(len(node_a.outbound_arcs), 2)
        self.assertEqual(len(node_b.inbound_arcs), 1)
        self.assertEqual(len(node_c.inbound_arcs), 1)

        self.assertEqual(node_a.outbound_arcs[0].destination, node_b)
        self.assertEqual(node_a.outbound_arcs[0].weight, 2.0)
        self.assertEqual(node_a.outbound_arcs[1].destination, node_c)
        self.assertEqual(node_a.outbound_arcs[1].weight, 4.0)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
