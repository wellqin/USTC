import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

g = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(g)

for score in [33, 99, 77, 70, 89, 90, 100]:
    print(grade(score))