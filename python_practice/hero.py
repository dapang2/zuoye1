class Hero:
    power = 0
    hp = 0
    tc = ''

    def fight(self, e_hp, e_power, name):
        final_hp = self.hp - e_power
        e_final_hp = e_hp - self.power
        if final_hp > e_final_hp:
            print(f'{name}赢了')
        if final_hp < e_final_hp:
            print("敌人赢了")
        if final_hp == e_final_hp:
            print("平了")

    def speak_lines(self):
        print(self.tc)
