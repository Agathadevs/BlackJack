import time
import os
import random
import sys

class BlackJack:
    def __init__(self):
        self.player=int(input("玩家人數:"))
        self.player_data={input(f"玩家{n}:"):f"玩家{n}" for n in range(1,self.player+1)}
        self.makers=input(f"庄家:")
        self.money={f"玩家{n}下注金額":int(input(f"玩家{n}的下注金額:")) for n in self.player_data.keys()}
        self.insurance={}
        self.ps=[]
        self.ms=[]
        self.end_={}

        self.makers_data=[self.makers]
        self.cards=[{"A":[1,11]},
                      2,3,4,5,6,7,8,9,10,
                    {"J":10,"Q":10,"K":10}]
       
        self.card_nums=[1,2,3,4,5,6,7,8,9,10,10,10,11]
        self.method={
             "拿牌":"hit",
             "停牌":"stand",
             "分牌":"split",
             "雙倍下注":"double",
             "保險":"insurance",
        }

        self.next={
             "拿牌":"hit",
             "停牌":"stand",
             "雙倍下注":"double",
             "保險":"insurance",
        }

        self.player_cards={}
        self.makers_cards={}
        self.spilt_card={}

        self.ml:int
        self.md:int
        self.pl:int
        self.pd:int
        
    def change_(self):
        for k,v in self.player_data.items():
            if k==self.makers_data[0]:
                  n=str(v)[-1]
                  self.player_data.update({k:f"玩家{n} - > 庄家"})
                
                                   
    def start_label():

                """
< ---------------------------------- >
               start !
< ---------------------------------- >

                """
        
         
    def cards_(self):
        for k,v in list(self.player_data.items()):
            time.sleep(2)
            print(">  庄家開始發牌  <")
            time.sleep(2)
            
            if len(v)>3:
                if v[8]=="庄":
                    self.ml=random.choice(self.card_nums)
                    print(f"庄家:{k} -> 明牌:{self.ml}") 

            else:
                self.pl=random.choice(self.card_nums)
                print(f"玩家:{k} -> 明牌:{self.pl}")
            print("其餘玩家請閉眼睛")
            time.sleep(3)
            
            if len(v)>3:
                if v[8]=="庄":
                    self.md=random.choice(self.card_nums)
                    print(f"庄家:{k} -> 暗牌:{self.md}",end='',flush=True)
            else:
                self.pd=random.choice(self.card_nums)
                print(f"玩家 {k} -> 暗牌:{self.pd}",end='',flush=True)
                
            if (n:=isinstance(self.ml,int)):
                if len(v)>3:
                    mc= { f"{k}的卡牌":
                            [
                                self.ml,
                                self.md,
                            ]
                        }
                    self.makers_cards.update(mc)
                    
            if (n:=isinstance(self.pl,int)):
                if len(v)<4:
                    pc= { f"{k}的卡牌":
                            [
                                self.pl,
                                self.pd,
                            ]
                        }
                    self.player_cards.update(pc)

            time.sleep(2)
            sys.stdout.write('\r' + ' ' * len(""))
            sys.stdout.flush()
        sys.stdout.write('\r' + ' ' * len("")) 
        print(" ------------------")
        time.sleep(1)
        print("-> 牌已由庄家發完 <-")
        time.sleep(1)
        print(" ------------------")
        

    def hit(self,player):
        if player[0] in self.player_data.keys():
            hit_card=random.choice(self.card_nums)
            self.player_cards[f"{player[0]}的卡牌"].append(hit_card)
            time.sleep(1)
            print("已成功加牌!")
            print("--------------")
            

    def stand(self,player):
        label=f"{player[0]}玩家 -> 選擇停牌"
        print(label)
        print("--------------")

    
    def split(self,player):
        print(f"{player[0]}玩家已經選擇分牌")
        n=input()
        if n in self.next.keys():
            while n not in self.method.keys():
                print("❌請選擇此列表其中一項:",list(map(lambda s:s,self.method)))
            match n:
                case "拿牌":
                    BlackJack.hit(player)
                case "停牌":
                    BlackJack.stand(player)
                case "雙倍下注":
                    BlackJack.double(player)
                case "保險":
                    BlackJack.insurance(player)
        print("--------------")
        
    
    def double(self,player):
        for i in self.player_data.keys():
            if player[0]==i:
                new_data={f"玩家{i}下注金額":self.money[f"玩家{i}下注金額"]*2}
                self.money.update(new_data)
                BlackJack.hit(player)
        print("--------------")
        

    def insurance(self,player):
        for i in self.player_data.keys():
            if player[0]==i:
                new_data={f"玩家{i}保險金額":self.money[f"玩家{i}下注金額"]//2}
                self.insurance.update(new_data)
        print("已保險成功")
        print("--------------")

    
    def hit_(self,player):
        if player in self.makers_cards.keys():
            hit_card=random.choice(self.card_nums)
            self.makers_cards[f"{player[0]}的卡牌"].append(hit_card)
            print("已成功加牌!")
            print("--------------")


    def request(self):
        time.sleep(1)
        for i in ["請玩家選擇:"]+list(map(lambda s:s,self.method)):
            print(i,end=" ")
        print()
        
    def request_(self):
        for k,v in self.player_cards.items():
            if len(v)<4:
                print(k+"選擇了:",end=" ")
                n=input()
                while n not in self.method.keys():
                    print("❌請選擇此列表其中一項:",list(map(lambda s:s,self.method)))
                if n in self.method.keys():
                    match n:
                        case "拿牌":
                            BlackJack.hit(self,player=k)
                        case "停牌":
                            BlackJack.stand(self,player=k)
                        case "分牌":
                            if v[0]==v[1]:
                                BlackJack.split(self,player=k)
                            else:
                                print(f"- > {k[0:1]}玩家選擇分牌無效!")
                        case "雙倍下注":
                            if (sum(v)==9 or 10 or 11):
                                BlackJack.double(self,player=k)
                            else:
                                print("選擇無效")
                        case "保險":
                            for k,v in self.makers_cards.items():
                                if v[0]==11:
                                    BlackJack.insurance(self,player=k)
        for k,v in self.makers_cards.items():
            if len(v)>4:
                if sum(self.makers_cards.get(k))<17:
                    BlackJack.hit_(k)
             
    def compare(self):
        for k,v in self.makers_cards.items():
            self.ms.append(sum(v))
            print(f"{k[0]}玩家點數:{sum(v)}")
        for k,v in self.player_cards.items():
            if sum(v)>self.ms[0]:
                print(f"{k[0]}玩家獲勝庄家!")
            elif sum(v)<self.ms[0]:
                print(f"庄家獲勝{k[0]}玩家!")
            elif sum(v)==self.ms[0]:
                print(f"{k[0]}玩家與庄家平手")
        time.sleep(1)
       
    def start_game(self) -> None:

        """
        role.md
        """
      
    def color(self) -> None:

        """
        card's color
        """
        ...

    def check(self):
        print()
        print("----------------")
        print()
        print(self.player_data)
        print(self.money)
        print(f"庄家 -> {self.makers_cards}")
        print(f"玩家 -> {self.player_cards}")
        
        
if __name__=="__main__":
    BJ=BlackJack()
    time.sleep(1)
    print(BJ.start_label.__doc__)
    time.sleep(1)
    BJ.change_()
    BJ.cards_()
    BJ.request()
    BJ.request_()
    BJ.compare()