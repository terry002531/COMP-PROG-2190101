# def read_answers():
#     N = int(input())
#     answers = []
#     for _ in range(N):
#         sid, ans = input().split()
#         answers.append([sid, ans])
#     return answers
#
#
# def marking(answer, solution):
#     # 返回答对题目的数量
#     score = 0
#     for i in range(len(solution)):
#         if answer[i] == solution[i]:
#             score += 1
#     return score
#
#
# def grading(score):
#     # 分数是百分制
#     # >=80 A, >=70 B, >=60 C, >=50 D, else F
#     bands = [(80, "A"), (70, "B"), (60, "C"), (50, "D")]
#     for a, g in bands:
#         if score >= a:
#             return g
#     return "F"
#
#
# def scoring(answers, solution):
#     scores = []
#     L = len(solution)
#     for sid, ans in answers:
#         sc = marking(ans, solution) / L * 100
#         grade = grading(sc)
#         scores.append([sid, sc, grade])  # [学号, 分数(百分比), 等级]
#     return scores
#
#
# def report(scores):
#     for sid, sc, grade in scores:
#         print(sid, sc, grade)
#
#
# def sort(scores):
#     # 分数降序；如果分数相同，学号降序
#     scores.sort(key=lambda x: (x[1], x[0]), reverse=True)
#
#
# # ===== main =====
# solution = input().strip()
# answers = read_answers()
# scores = scoring(answers, solution)
# sort(scores)
# report(scores)

def read_answers():
    N = int(input())
    answers = []
    for k in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers

def marking(answer, solution):
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score

def grading(score):
    g = [[80,"A"], [70, "B"], [60, "C"], [50, "D"]]
    for a,b in g:
        if score >= a:
            return b
    return "F"

def scoring(answers, solution):
    scores = []
    l = len(solution)
    for sid, ans in answers:
        score = marking(ans, solution) / l * 100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores

def report(scores):
    for sid, sc, grade in scores:
        print(sid, sc, grade)

def sort1(scores):
    x = []
    for sid, score, grade in scores:
        x.append([score, sid, grade])
    x.sort(reverse = True)
    for i in range(len(x)):
        scores[i] = [x[i][1], x[i][0], x[i][2]]

solution = input()
answers = read_answers()
scores = scoring(answers, solution)
sort1(scores)
report(scores)


