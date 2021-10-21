# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:49:10 2020

@author: 林致嘉
"""

import random

lotto = []
lotto2 = []
i = 0

while(i < 6):
    if (random.randint(0,1) == random.randint(1,2)):
        k = random.randint(1,38)
        if k not in lotto:
            lotto.append(k)
            i+=1
lotto2.append(random.randint(1,8))

print("第一區:")
print(sorted(lotto))
print("第二區:")
print(lotto2)

    