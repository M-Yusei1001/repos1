#辞書
teams = {"Ferrari":"SF-24","RedBull":"RB20","VCARB":"VCARB01"}

print("知りたいチーム名を入力してください")

#チームのリストを提示する
print("Team list:")
for team in teams:
    print(team)

#チーム名の入力待ち
team_input = input(">")

count = 0

#入力 team_input に該当するチームがあれば辞書から型式を出力
for team in teams:
    if team == team_input:
        print(team + "の車は" + teams[team] + "です")

        #該当するチームがあればcountを1にする
        count = 1

    #該当するチームがあったら判別処理を中断    
    if count == 1:
        break

#countが0なら該当するチームがなかったことを表示する
if count == 0:
    print("該当するチームがありませんでした")