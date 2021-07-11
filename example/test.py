foo = 1
bar = 2

x = 4

x1 = 1
x2 = 2
x3 = 3
x4 = 4

here_we_contain_another_foo_variable = 15

mytuple = (1,2,3)
_, _, IMPORTANT = mytuple
_ = 5
_leading_underscore = 5


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


my = TestClass(1, 14)

my.x_graph_position = 127


chee = 8
