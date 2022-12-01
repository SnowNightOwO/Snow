import ast

def get_stud():#學號
 txt="1b"
 data = open(txt).read().split("\n")
 stud = data[:-1]
 return stud
cp_stud = get_stud()
    
cp_w11_quiz_="1btest.json"

def get_score(json):#考試結果
    person = 0
    score = 0
    json_data = open(json).read()
    big_dict = ast.literal_eval(json_data)
    testuser = big_dict["body"]["testuser"]
    quiz_dict = {}
    for i in testuser:
        stud_id = testuser[i]["user_name"]
        stud_score = int(float( testuser[i]["total_score"]))
        quiz_dict[stud_id] = stud_score
        person = person + 1
        score = score + stud_score
    return quiz_dict, person, score
    
#cp_quiz, num_stud, total_score = get_score(cp_w10_quiz_url)
cp_quiz, person, score = get_score(cp_w11_quiz_)
cp_abs = []
for stud in cp_stud:
    try:
        print(stud, cp_quiz[stud])
    except:
        # 缺考者沒有 quiz 成績
        print(stud, "缺")
        cp_abs.append(stud)
print ("\n參考人數%s"%(person))
print ("\n以下為總分%s"%(score))  
print("\n考試平均分數為:", int(score/person))
#列出缺考名單
print("="*20)
print("以下為 w11 缺考名單:")
for stud in cp_abs:
    print(stud)