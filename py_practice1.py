teams = {"Ferrari":"SF-24","RedBull":"RB20","VCARB":"VCARB01"}

print("知りたいチーム名を入力してください")

print("Team list:")
for team in teams:
    print(team)

team_input = input(">")

count = 0

for team in teams:
    if team == team_input:
        print(team + "の車は" + teams[team] + "です")
        count = 1
    if count == 1:
        break

if count == 0:
    print("該当するチームがありませんでした")