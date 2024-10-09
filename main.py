import random
import itertools
from collections import Counter

def Flush(hua_list):
    #7选5
    hua_set = itertools.combinations(Sumhua,5)

    for fi_list in hua_set:
        for fi in range(5):
            if fi_list[fi] != fi_list[fi+1]:
                break
            if fi == 4:
                return True
    return False

#顺子和对子的判断
def Straight_Pair(SumPok):
    #7选5
    PokSet = itertools.combinations(SumPok,5)
    PairDir = {}
    FinLst = []
    global IsFlush
    global Type
    #判断是不是顺子
    for LPokSet in PokSet:
        for RanS in range(0,5):
            if LPokSet[RanS+1] != LPokSet[RanS]:
                break
            if RanS == 4:
                Type = 'Straight'
                FinLst = LPokSet
                if IsFlush:
                    Type ='Flush Straight'
                    FinLst = LPokSet

    #统计有多少个重复的牌，重复了几次
    for LPokSet in PokSet:
        for RanP in range(0,5):
            if LPokSet[RanP] in PairDir:
                PairDir[LPokSet[RanP]] += 1
            else:
                PairDir[LPokSet[RanP]] = 1

        PairSet = set(PairDir.values())

        if 4 in PairDir.values():
            if Type != 'Flush Straight':
                Type = 'Four Of A Kind'
                FinLst = LPokSet
        elif 2 in PairDir.values() and 3 in PairDir.values():
            if Type != 'Flush Straight' and Type != 'Four Of A Kind' and Type != 'Straight':
                Type = 'Full house'
                FinLst = LPokSet
        elif 3 in PairDir.values():
            if Type != 'Flush Straight' and Type != 'Four Of A Kind' and Type != 'Straight' and not IsFlush and Type != 'Full house':
                Type = 'Three Of A Kind'
                FinLst = LPokSet
        #下面这个分支的写法是把PairDir转成set类型后，set类型里面不能有重复的值，如果是两对类型set会比dir短2个
        elif 2 in PairDir.values() and len(PairSet) - len(PairDir) == -2:
            if Type != 'Flush Straight' and Type != 'Four Of A Kind' and Type != 'Straight' and not IsFlush and Type != 'Full house ':
                Type = 'Two Pair'
                FinLst = LPokSet
        elif 2 in PairDir.values():
            if Type != 'Flush Straight' and Type != 'Four Of A Kind' and Type != 'Straight' and not IsFlush and Type != 'Full house' and Type !='Two Pair':
                Type = 'One Pair'
                FinLst = LPokSet

    return FinLst

#因为花色和点数分开要给同花写一个比大小
#传进来的是带花色带点数的列表
#如果两个人都是同花，比较同花大小
def Flush_Compare(SumVal):
    FstLtt = [s[0] for s in SumVal]
    LttCot = Counter(FstLtt)

    MaxCot = max(LttCot.values())
    MaxLtt = [Ltt for Ltt,count in LttCot.items() if count == MaxCot]
    Result = [s for s in SumVal if s[0] in MaxLtt]

    return Result

#最没用的函数，首轮要干的事都在里面
def First_Round():
    global First
    global Money
    global JackPot

    print('先手为：', First)

    for key in Money:
        Money[key] -= 20

    print('已自动下底注')

#还没想好
def Computer(SumCard):
    global IsFlush

    Hua = [s[0] for s in SumCard]
    Pok = [s[1:] for s in SumCard]

    Flush(Hua)
    Fin = Straight_Pair(Pok)

#牌堆，b是黑桃，r是红桃，f是方块，m是梅花
PokerLst = ['b14','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12','b13','r14','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','f14','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','m14','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12','m13']

print('Texas hold \'em Poker 0.1 Beta')
print('说明：')
input('按下任意键进入')

Round = 1
JackPot = 0
MinBet = 20
Restart = 0
random.shuffle(PokerLst)

#发牌
River = PokerLst[:5]
PlayerHand = PokerLst[5:7]
Com1Hand = PokerLst[7:9]
Com2Hand = PokerLst[9:11]
Com3Hand = PokerLst[11:13]

while 1:

    print('回合开始，当前是第',Round,'轮，当前底注为',MinBet)

    if Round == 1:
        First_Round()

    for key in Money:
        if Money[key] <=0:
            if Money[PlayerHand] <=0:
                print('You Lose')
                Restart = 1
            else:
                print('')
    if Restart == 1:
        break

    print('当前牌河\n',River[:Round+2])
    print('手牌',PlayerHand)
    input('输入数字选择你要进行的操作\n1.Raise 2.Flod 3.Check 4.Call')