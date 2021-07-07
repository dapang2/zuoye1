class House:
    door = ''
    floor = ''

    def cook(self):
        print('我在厨房炸鸡排')

    def sleep(self):
        print('我在卧室睡觉')

bob_house = House()
bob_house.door = 'white'
bob_house.floor = 'black'
mary_house = House()
mary_house.floor = 'black'
mary_house.door = 'white'