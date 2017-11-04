#! encoding = utf8
# multithread:selling tickets with ten agents
from threading import Thread,Lock
import random,time

num_agents=10
num_tickets=[100]

def sell_tikets(agent_id,nt,lock):
    total = 0
    while 1:
        with lock:
            if nt[0]>0:
                print("Agent %d sells a ticket No.%d")%(agent_id,nt[0])
                nt[0]-=1
                total+=1

            elif nt[0]==0:
                break

        time.sleep(random.random()*(1+agent_id/2))

    print ("Agent %d done. Total sells %d tickets")%(agent_id,total)

for i in range(num_agents):
    t=Thread(target=sell_tikets,args=(i,num_tickets,Lock()))
    t.start()