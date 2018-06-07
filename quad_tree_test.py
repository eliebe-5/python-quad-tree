import quad_tree
import random

class element:
    x, y = 0, 0
    name = 0
    def __init__(self, xx, yy, name):
        self.x = xx
        self.y = yy
        self.name = name

def test():
    tree = quad_tree.quad_tree()
    tree.setup(512, 512)
    for i in range(0, 10000):
        e = element(random.randint(0, 512), random.randint(0, 512), i)
        tree.insert_element(e)

    elmnts = tree.find_elements(200, 200, 10, 10)

    print("Found elements: ", len(elmnts))

    for e in elmnts:
        print(e.name, e.x, e.y)
test()
