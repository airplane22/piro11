words = ['hawaii','happy']

words.sort(key=len)

x=''

breaking = 1
                        
for i in range(0, len(words[0])):
        for j in range(1, len(words)):


                if words[j][0:i+1] == words[0][0:i+1] :
                        x = words[0][0:i+1]
                        
                elif words[j][0:i+1] != words[0][0:i+1]:
                        if i>= 0:
                                x = words[0][0:i]

                                breaking = 0
                                break
                                
                        else :
                                x = 100
                                breaking = 0
                                break
        if breaking == 0:
                break
                        
                        
        
        
               
print(x)               



