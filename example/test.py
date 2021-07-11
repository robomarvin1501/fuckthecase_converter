foo = 1
bar = 2

x = 4

x1 = 1
x2 = 2
x3 = 3
x4 = 4

here_we_contain_another_foo_variable = 15

def testfunc(hello, goodbye):
    return hello + goodbye


print(testfunc(2, 3))


# Here we look to see if it will catch a comment referencing the function testfunc

class TestClass:
    def __init__(self, x_position, y_position):
        self.x_graph_position = x_position
        self.y_graph_position = y_position

    def strange_method(self):
        return self.y_graph_position + self.x_graph_position


chee = 8
