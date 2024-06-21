class Team:

    def __init__(self, team):
        self.team = team

    def driver_wins(self, num):
        circuits = {
            1:{"Suzuka":True},
            2:{"Monaco":False}
        }

        circuit = circuits[num]

        if circuit == True:
            return self.name + "は" + circuit[circuit] + "で勝利しています"
        elif circuit == False:
            return self.name + "は" + circuit[circuit] + "で敗北しています"
