import unittest

from module_lab2_task2 import Network


class TestNetworkMethods(unittest.TestCase):

    def test_add_node(self):
        network = Network()
        network.add_node("A")
        network.add_node("B", 5)
        self.assertEqual(len(network.nodes), 2)
        self.assertEqual(network.nodes[0].name, "A")
        self.assertEqual(network.nodes[1].name, "B")
        self.assertEqual(network.nodes[1].value, 5)

    def test_add_arc(self):
        network = Network()
        network.add_node("A")
        network.add_node("B")
        network.add_node("C")
        network.add_arc(network.get_node("A"), network.get_node("B"), 2.0)
        network.add_arc(network.get_node("B"), network.get_node("C"), 3.0)
        self.assertEqual(len(network.arcs), 2)
        self.assertEqual(network.arcs[0].weight, 2.0)
        self.assertEqual(network.arcs[1].weight, 3.0)
        self.assertEqual(network.arcs[0].from_node.name, "A")
        self.assertEqual(network.arcs[0].to_node.name, "B")
        self.assertEqual(network.arcs[1].from_node.name, "B")
        self.assertEqual(network.arcs[1].to_node.name, "C")

    def test_read_network(self):
        network = Network()
        network.read_network("network.txt")
        self.assertEqual(len(network.nodes), 6)
        self.assertEqual(len(network.arcs), 9)

        node_a = network.get_node("A")
        node_b = network.get_node("B")
        node_c = network.get_node("C")
        node_d = network.get_node("D")
        node_e = network.get_node("E")
        node_f = network.get_node("F")

        self.assertIsNotNone(node_a)
        self.assertIsNotNone(node_b)
        self.assertIsNotNone(node_c)
        self.assertIsNotNone(node_d)
        self.assertIsNotNone(node_e)
        self.assertIsNotNone(node_f)

        self.assertEqual(len(node_a.arcs_out), 2)
        self.assertEqual(len(node_b.arcs_out), 2)
        self.assertEqual(len(node_c.arcs_out), 2)
        self.assertEqual(len(node_d.arcs_out), 2)
        self.assertEqual(len(node_e.arcs_out), 1)
        self.assertEqual(len(node_f.arcs_out), 0)

        arc_ab = next((arc for arc in node_a.arcs_out if arc.to_node == node_b), None)
        arc_ac = next((arc for arc in node_a.arcs_out if arc.to_node == node_c), None)
        arc_bc = next((arc for arc in node_b.arcs_out if arc.to_node == node_c), None)
        arc_bd = next((arc for arc in node_b.arcs_out if arc.to_node == node_d), None)
        arc_cd = next((arc for arc in node_c.arcs_out if arc.to_node == node_d), None)
        arc_ce = next((arc for arc in node_c.arcs_out if arc.to_node == node_e), None)
        arc_de = next((arc for arc in node_d.arcs_out if arc.to_node == node_e), None)
        arc_df = next((arc for arc in node_d.arcs_out if arc.to_node == node_f), None)
        arc_ef = next((arc for arc in node_e.arcs_out if arc.to_node == node_f), None)

        self.assertIsNotNone(arc_ab)
        self.assertIsNotNone(arc_ac)
        self.assertIsNotNone(arc_bc)
        self.assertIsNotNone(arc_bd)
        self.assertIsNotNone(arc_cd)
        self.assertIsNotNone(arc_ce)
        self.assertIsNotNone(arc_de)
        self.assertIsNotNone(arc_df)
        self.assertIsNotNone(arc_ef)

        self.assertEqual(arc_ab.weight, 2)
        self.assertEqual(arc_ac.weight, 4)
        self.assertEqual(arc_bc.weight, 1)
        self.assertEqual(arc_bd.weight, 4)
        self.assertEqual(arc_cd.weight, 2)
        self.assertEqual(arc_ce.weight, 1)
        self.assertEqual(arc_de.weight, 2)
        self.assertEqual(arc_df.weight, 2)
        self.assertEqual(arc_ef.weight, 3)


if __name__ == '__main__':
    unittest.main()
