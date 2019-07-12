class character:
        def __init__(self,name):
                self.name = name
                self.힘 = '힘'
                self.지력 = '지력'
                self.직업 = '직업'

        def info(self):
                l = [6, 7, 8]
                import random
                self.힘= random.choice(l)
                self.지력= random.choice(l)
                if self.힘>self.지력 :
                        self.직업 = '전사'
                elif self.힘==self.지력 :
                        self.직업 = '궁수'
                else :
                        self.직업 = '법사'
                        print('캐릭터 이름: ', self.name)
                        print('캐릭터 정보: 힘(',self.힘,'), 지력(',self.지력,')')
                        print('캐릭터 직업: ',self.직업)

player = character(input('캐릭터의 이름을 입력하세요: '))
player.info()
        
