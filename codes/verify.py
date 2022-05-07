import math

diamond = math.comb(13,3)
spade = math.comb(13,1)
total_outcome = math.comb(52,4)

#Probability of getting one spade and three diamonds is
Pr = diamond*spade/total_outcome
print('Theoritical probability',Pr)
