x = input('캐릭터의 이름을 입력하세요: ')


l = [6, 7, 8]
import random
힘= random.choice(l)
지력= random.choice(l)

if 힘>지력 :
        직업 = '전사'
elif 힘==지력 :
        직업 = '궁수'
else :
        직업 = '법사'

print('캐릭터 이름: ', x)
print('캐릭터 정보: 힘(',힘,'), 지력(',지력,')')
print('캐릭터 직업: ',직업)

        
