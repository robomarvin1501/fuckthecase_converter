#!/usr/bin/env
import ast
import sys
import random
import re
from functools import lru_cache


# random.seed(100)

# TODO market as a code correcter, remove double space etc...

@lru_cache(maxsize=None)
def convert_to_fuckthecase(name: str) -> str:
    if name[0:2] == '__' or name[-2:] == '__':
        return name
    if name == '_':
        return name
    new_name = ""
    name = "".join(re.findall("[a-zA-Z0-9]", name))
    name = name.lower()
    for letter in name:
        if random.random() < 0.5:
            new_name += letter
        else:
            new_name += letter.upper()

    return new_name


class TreeWalker(ast.NodeVisitor):
    def __init__(self):
        self.tokens = dict()

    def visit_FunctionDef(self, node):
        self.tokens[node.name] = convert_to_fuckthecase(node.name)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_ClassDef(self, node):
        self.tokens[node.name] = convert_to_fuckthecase(node.name)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_arguments(self, node):
        for a in node.args:
            # print(a.arg)
            self.tokens[a.arg] = convert_to_fuckthecase(a.arg)

    def visit_Assign(self, node):
        try:
            for target in node.targets:
                self.tokens[target.id] = convert_to_fuckthecase(target.id)
        except AttributeError:
            try:
                self.tokens[node.value.id] = convert_to_fuckthecase(node.value.id)
            except AttributeError:
                self.tokens[target.attr] = convert_to_fuckthecase(target.attr)

    def visit_Attribute(self, node):
        self.tokens[node.attr] = convert_to_fuckthecase(node.attr)


try:
    input_file = sys.argv[1]
except IndexError:
    input_file = "example/test.py"

try:
    output_file = sys.argv[2]
except IndexError:
    output_file = "example/output.py"

with open(input_file, 'r') as f:
    code = f.read()

tree = ast.parse(code)
tw = TreeWalker()

tw.visit(tree)

for key in tw.tokens.keys():
    code = re.sub(fr"\b{key}\b", tw.tokens[key], code)

print(code)

with open(output_file, 'w') as f:
    f.write(code)

print(f"\nCode printed to {output_file}")
