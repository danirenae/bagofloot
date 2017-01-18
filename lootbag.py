import sys
import sqlite3

class LootBag():

    def __init__(self):
        self.good_children = dict()

    def add_toy_for_child(self, child, toy):

        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            try:
                c.execute("""INSERT INTO Child
                            VALUES (?, ?, ?)""",
                            (None, child, 0))
            except sqlite3.OperationalError:
                pass

            c.execute("""SELECT ChildId
                        FROM Child
                        WHERE Name='{}'""".format(child))
            results = c.fetchall()

            try:
                c.execute("""INSERT INTO Toy
                            VALUES (?, ?, ?)""",
                            (None, toy, results[0][0]))
            except sqlite3.OperationalError:
                pass

    def remove_toy_for_child(self, child, toy):

        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT ChildId
                        FROM Child
                        WHERE Name='{}'""".format(child))
            results = c.fetchall()

            try:
                c.execute("""DELETE FROM Toy
                            WHERE ChildId={}
                            AND Name='{}'""".format(results[0][0], toy))
            except sqlite3.OperationalError:
                pass


    def get_by_child(self, child):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT t.Name
                        FROM Toy t, Child c
                        WHERE c.Name='{}'
                        AND c.ChildId = t.ChildId
                    """.format(child))

            toys = c.fetchall()
            print(toys)


    def get_list_of_kids(self):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT c.Name, COUNT (t.ToyId) ToyCount
                        FROM Child c, Toy t
                        WHERE t.ChildId = c.ChildId
                        GROUP BY c.Name
                      """)

            names = c.fetchall()
            print(names)


    def is_child_happy(self, child):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT c.Name, c.Happy
                    FROM Child c, Toy t
                    WHERE c.ChildId = t.ToyId
                    AND c.Happy = 1
              """)

            deliveredandhappy = c.fetchall()
            print(deliveredandhappy)

    def deliver_toys_to_child(self, child):
        # with sqlite3.connect('lootbag.db') as conn:
        #     c = conn.cursor()




if __name__ == "__main__":
    bag = LootBag()
    if sys.argv[1] == "add":
      bag.add_toy_for_child(sys.argv[3], sys.argv[2])
      print(bag.get_by_child(sys.argv[3]))
    elif sys.argv[1] == "remove":
      bag.remove_toy_for_child(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls":
      bag.get_list_of_kids()
    elif sys.argv[1] == "ls":
      bag.get_by_child(sys.argv[2])
    elif sys.argv[1] == "delivered":
      bag.deliver_toys_to_child(sys.argv[2])

