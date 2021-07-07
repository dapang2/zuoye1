class bicycle:
    def run(self, miles):
        print(f"用脚骑了{miles}公里，好累呀")

class BEbicycle(bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, add_valme):
        self.valume= add_valme+self.valume

    def run_e(self, miles):
        ele_miles = self.valume*10
        res_mile = ele_miles -miles
        if res_mile >= 0:
            print(f"骑行的总公里数为{miles}")
        else:
            print(f"使用电动车的公里数{ele_miles}")
            self.run(miles-ele_miles)
e = BEbicycle(10)
e.run_e(10000)
