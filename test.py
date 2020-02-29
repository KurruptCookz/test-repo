from run import add, subtract, announce
import sys

announce("running test 'add'")
result = add(1, 2)
if result == 3:
  print("passed")
else:
  print("failed")
  sys.exit(1)
