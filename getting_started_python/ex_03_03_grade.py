score = input("Enter Score: ")
s = float(score)
grade = None

if s > 1.0:
    print('score is too high')
elif s >= 0.9:
    grade = 'A'
elif s >= 0.8:
    grade = 'B'
elif s >= 0.7:
    grade = 'C'
elif s >= 0.6:
    grade = 'D'
elif s >= 0.0:
    grade = 'F'
else:
    print('score is too low')

print(grade)