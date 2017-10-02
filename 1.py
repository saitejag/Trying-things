import winsound
from random import randint
t = 0;
while(t<10000):
    k = randint(2000,3000);
    l = randint(100,500);
    winsound.Beep(k,l);
    #print(k);
    t = t + l;

