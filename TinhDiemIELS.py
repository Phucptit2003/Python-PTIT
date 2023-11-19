# Hàm tính điểm cho kỹ năng Reading và Listening
def calculate_skill_score(correct_answers):
    if correct_answers >=39:
        return 9.0
    elif correct_answers >= 37:
        return 8.5
    elif correct_answers >= 35:
        return 8.0
    elif correct_answers >= 33:
        return 7.5
    elif correct_answers >= 30:
        return 7.0
    elif correct_answers >= 27:
        return 6.5
    elif correct_answers >= 23:
        return 6.0
    elif correct_answers >= 20:
        return 5.5
    elif correct_answers >= 16:
        return 5.0
    elif correct_answers >= 13:
        return 4.5
    elif correct_answers >= 10:
        return 4.0
    elif correct_answers >= 7:
        return 3.5
    elif correct_answers >= 5:
        return 3.0
    elif correct_answers >= 3:
        return 2.5
    else:
        return 0.0

# Hàm tính điểm overall
def calculate_overall_score(reading, listening, speaking, writing):
    skill_scores = [calculate_skill_score(reading), calculate_skill_score(listening), speaking, writing]
    average_score = sum(skill_scores) / 4.0
    
    # Làm tròn điểm theo quy ước chung
    if average_score % 1.0 >= 0.75:
        return int(average_score) + 1.0
    elif average_score % 1.0 >= 0.25:
        return int(average_score) + 0.5
    else:
        return int(average_score)

# Đọc số lượng thí sinh
T = int(input())

# Xử lý từng thí sinh
for _ in range(T):
    reading, listening, speaking, writing = map(float, input().split())
    overall_score = calculate_overall_score(reading, listening, speaking, writing)
    print("{:.1f}".format(overall_score))
