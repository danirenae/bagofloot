import unittest
from lootbag import *

class TestLootBag(unittest.TestCase):

    def test_can_add_toy_for_child(self):

      bag = LootBag()
      child = "Timothy"
      toy = "Tonka Truck"

      bag.add_toy_for_child(child, toy)

      self.assertIn(toy, bag.get_by_child(child))

    def test_can_remove_toy_for_child(self):

      bag = LootBag()
      child = "Timothy"
      toy = "Tonka Truck"

      bag.add_toy_for_child(child, toy)
      self.assertIn(toy, bag.get_by_child(child))

      bag.remove_toy_for_child(child, toy)
      self.assertNotIn(toy, bag.get_by_child(child))

    def test_can_list_all_children_getting_a_toy(self):

      bag = LootBag()
      bag.add_toy_for_child("Ben", "Duct Tape")
      bag.add_toy_for_child("Drew", "Haircut accessories")
      bag.add_toy_for_child("Trent", "Google course")

      list_of_kids = bag.get_list_of_kids()

      self.assertIs(type(list_of_kids), list)
      self.assertIn("Ben", list_of_kids)
      self.assertIn("Drew", list_of_kids)
      self.assertIn("Trent", list_of_kids)

    def test_list_child_toys(self):

      bag = LootBag()
      bag.add_toy_for_child("Trent", "Google course")
      bag.add_toy_for_child("Trent", "Silly putty")
      bag.add_toy_for_child("Drew", "Haircut accessories")

      self.assertListEqual(bag.get_by_child("Trent"), ["Google course", "Silly putty"])

    def test_toys_can_be_delivered_to_child(self):

      bag = LootBag()
      child = "Trent"
      bag.add_toy_for_child(child, "Google course")
      bag.add_toy_for_child(child, "Silly putty")

      self.assertFalse(bag.is_child_happy(child))
      bag.deliver_toys_to_child(child)
      self.assertTrue(bag.is_child_happy(child))





