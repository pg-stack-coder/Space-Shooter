class marble:
    def __init__(self):
        self.wheel=input('hello:')
        self.seat=6
class speedy(marble):
    def __init__(self):
        super().__init__()
        self.make='marble'
        self.name='savage speeders'
        self.own='swift'
    def case(self):
        print('speedy a',self.make,'of',self.own,'and we are',self.name)
class rapidly(speedy):
    def __init__(self):
        super().__init__()
        self.lux='extra grip'
        self.features='gradient red'
        self.custom='flames of your choice'
        self.motto='speed to glory'
    def launch(self):
        self.case()
        print('we are happy to announce','\n','rapidly is our latest model','\n',self.lux,'\n',self.features,'\n',self.custom,'\n',self.motto,':)')
a=rapidly()
a.launch()
