from run import add, subtract, announce

announce("running test 'add'")
result = add(1, 2)
if result == 3:
  print("passed")
else:
  print("failed")
