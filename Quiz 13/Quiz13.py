def robotStep(steps, S):
  N = len(steps)
  sols = [[[] for n in range(N + 1)] for s in range(S + 1)]
  for n in range(0, N + 1):
    sols[0][n].append([])

  for s in range(1, S+1):
    for n in range(1, N+1):
      without_last = sols[s][n - 1]
      if (steps[n - 1] <= s):
          with_last = [list(sol) + [steps[n-1]] for sol in sols[s - steps[n - 1]][n]]
      else:
          with_last = []
      sols[s][n] = without_last + with_last

  return sols[S][N]

print("For n=1")
print(len(robotStep([1,2,3], 1)))
print(robotStep([1,2,3], 1))

print("For n=2")
print(len(robotStep([1,2,3], 2)))
print(robotStep([1,2,3], 2))

print("For n=3")
print(len(robotStep([1,2,3], 3)))
print(robotStep([1,2,3], 3))

print("For n=4")
print(len(robotStep([1,2,3], 4)))
print(robotStep([1,2,3], 4))

print("For n=5")
print(len(robotStep([1,2,3], 5)))
print(robotStep([1,2,3], 5))