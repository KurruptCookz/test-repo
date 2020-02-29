from run import add, subtract, announce
import sys

def test(name, expected, result):
  announce("running test '{}'".format(name))
  if expected == result:
      print("passed")
  else:
      print("failed")
      sys.exit(1)

# test add function
test("add", 3, add(1, 2))

# test subtract method
test("subtract", 1, subtract(2,1))
