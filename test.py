from run import add, subtract, announce
import sys

def test(expected, result):
  if expected == result:
      print("passed")
  else:
      print("failed")
      sys.exit(1)

announce("running test 'add'")

# test add function
test(3, add(1, 2))

# test subtract method
test(1, subtract(2,1))
