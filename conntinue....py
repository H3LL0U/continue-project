import pygame
import time

# УСТУПЫ
level = 1
a = 0
class balk:
    def __init__(self,wh,wh1,lon,sho,color,level):
        self.wh = wh
        self.wh1 = wh1
        self.lon = lon
        self.sho = sho
        self.color = color
        self.level = level
    def drawbalk(self,govne):
        pygame.draw.rect(govne,(self.color),(self.wh,self.wh1,self.lon,self.sho))
ledge = []
workonetime=1
shields=[]


class weapons:
    def __init__(self,wh,wh1,lon,sho,level):
        self.wh = wh
        self.wh1 = wh1
        self.lon = lon
        self.sho = sho
        self.color = (125,125,125)
        self.jump = False
        self.jumps = 0
        self.coolj = 0
        self.touch = False
        self.lll = False
        self.level = level


    def drawweapon (self,govne):
        pygame.draw.rect(govne,(self.color),(self.wh,self.wh1,self.lon +5,self.sho))
        pygame.draw.rect(govne,(self.color),(self.wh,self.wh1,self.sho,self.lon))
    def weaponinhandright(self,govne):

        pygame.draw.rect(govne,(self.color),(wh + sho//2,wh1 + lon //2,self.lon+5,self.sho))
        pygame.draw.rect(govne, (self.color), (wh + sho // 2, wh1 + lon //2, self.sho,self.lon))
    def weaponinhandleft(self,govne):


        pygame.draw.rect(govne,(self.color),(wh +sho//2 - lon + 5,wh1+lon//2,self.lon +5,self.sho))
        pygame.draw.rect(govne,(self.color),(wh+sho//2 - lon + self.lon + 5  ,wh1 + lon //2 ,self.sho,self.lon))





class teleport:
    def __init__(self,wh,wh1,color,level):
        self.wh = wh
        self.wh1 = wh1
        self.color = color
        self.lon = 85
        self.sho = 60
        self.level = level
    def draw(self,govne):

        pygame.draw.rect(govne,(125,125,125),(self.wh,self.wh1,self.sho,self.lon))
        pygame.draw.rect(govne,(self.color),(self.wh + 5,self.wh1 +5,self.sho-10,self.lon-10))

teleportscolors = []
teleports = []
unpress = False

















class bullet:
    def __init__(self,wh,wh1,speed,rad,bulletgo):
        self.wh = wh
        self.wh1 = wh1
        self.speed = speed
        self.rad = rad
        self.color = (125,0,0)
        self.bulletgo = bulletgo

    def drawbullet(self,govne):
        pygame.draw.circle(govne,(self.color),(self.wh,self.wh1),self.rad)
cooldownshot1 = 30
cooldownshot = 30
cooldownshot2 = 30
bullets = []











wipwip =[]



#команды

touch = False
def hpbar(hp,wh,wh1,maxhp,sho):
    pygame.draw.rect(govne,(125,125,125),(wh+ sho//2-50,wh1-26,100,12))
    pygame.draw.rect(govne,(255,0,0),(wh+sho//2-50,wh1-26,100*hp//maxhp,12))


def touchB(wh,whe1,lon,sho,dwh,dwh1,dlon,dsho):

    global a
    global wh1
    global touch


    if touch == True:
        a = 1


    if a == 0:

        if whe1 + sho <= dwh1 + 37 and whe1 + sho >= dwh1 and wh <= dwh + dlon and dwh <= wh + lon:
            wh1 -= wh1 -dwh1 + sho

            touch = True





def createB(bwh,bwh1,blon,bsho):




    touchB(wh,wh1,lon,sho,bwh,bwh1,blon,bsho)






levelshelperjjj = 1






 # ДЛЯ ПЕРЕМЕННЫХ!
dis = 1250
dis1 = 750
FPS = 70
clock = pygame.time.Clock()
#ГГ(ГЛАНЫЙ ГЕРОЙ)

cooldownj = FPS
lon = 50
sho = 75
speed = 8
wh = dis1 - lon
wh1 = 50
jump = False
jumps = 0
helperj = False
jumps2 = 10
cooldownj2 = 1
jerk = False
jerks = 10
coolj = 15
defcoolj = FPS
lll = False
fall = False
hp = 100
ded = False
unkillcool = 0
color = (0,0,0)
cooldownhelper = 0
hands = []
hands1 = []



wright = True
defwright = False
#ENEMYS
ene = []
spawncoold = 30
class enemy:
    def __init__(self,ewh,ewh1,esho,elon,ecolor,espeed,ehp,emaxhp,level,edefspeed):
        self.ewh=ewh
        self.ewh1 = ewh1
        self.esho = esho
        self.elon = elon
        self.espeed = espeed
        self.ecolor = ecolor

        self.eded = False
        self.ehp = ehp
        self.emaxhp = emaxhp
        self.ejump2 = 10
        self.ecollis = False
        self.ecolisspeed = 30
        self.defecolisspeed = 30
        self.efall = False
        self.ecoolj =150
        self.ejumps = 0
        self.elll = False
        self.ejump = False
        self.etouch = False
        self.level = level
        self.ea = 0
        self.cantmoverightXD = False
        self.cantmoveleftXD = False
        self.edefcoolj = 150
        self.ecantmoveleftXD = False
        self.ecantmoverightXD = False
        self.ewright = False
        self.edefspeed = edefspeed
        self.helllllllperrrrr = False



    def draw(self,govne):
        pygame.draw.rect(govne,(self.ecolor),(self.ewh,self.ewh1,self.elon,self.esho))




mouseleftclick = False
mouserightclick = False
shootfromright = False




class shield:
    def __init__(self,wh,wh1,sho,level):
        self.wh = wh
        self.wh1 = wh1
        self.hp = 75
        self.sho = sho
        self.color = (0,0,125)
        self.level = level


    def drawshield(self,govne):
        pygame.draw.rect(govne,self.color,(self.wh,self.wh1,self.hp,self.sho))
    def takeshield(self,wh,wh1,sho,lon):
        if wh + lon >= self.wh and wh <= self.wh + self.hp and wh1 <= self.wh1 + self.sho and wh1 + sho >= self.wh1 and len(hands1)<3:
            shields.pop(shields.index(self))

            if len(hands1)==1:
                hands1.append(shieldinMYhand(round(20 - lon + wh +5),round(wh1),True))
            if   len(hands1)==0:
                hands1.append(shieldinMYhand(round(20 + lon + wh),round(wh1),False))




class shieldinMYhand:
    def __init__(self,wh,wh1,left):

        self.hp = 75
        self.wh = wh
        self.wh1 = wh1
        self.sho = 5
        self.shieldinleft = False
        self.shieldinright = False
        self.color = (0,0,125)
        self.left = left

    def calculatewh1(self):
        self.wh1 =wh1+ (sho - self.hp)//2
        if len(hands1)==2 and self.left == False or len(hands1)==1 and wright :
            self.wh = 20 + lon + wh
        if len(hands1)==2 and self.left or len(hands1)==1 and wright == False:
            self.wh = 20 - lon + wh + 5












    def drawshieldinhand(self, wh, wh1, lon, sho, govne):
        
        if len(hands1) > 0 and wright == True or len(hands1) == 2 and self.left == False:

            pygame.draw.rect(govne, self.color, (self.wh, self.wh1 , self.sho, self.hp))
            self.shieldinright = True


        else:
            self.shieldinright = False
        if wright == False and len(hands1) > 0 or len(hands1) == 2:
            pygame.draw.rect(govne, self.color, (self.wh, self.wh1, self.sho, self.hp))
            self.shieldinleft = True


        else:
            self.shieldinleft = False

class wall:
    def __init__(self,wh,wh1,lon,sho):
        self.wh = wh
        self.wh1 = wh1
        self.lon = lon
        self.sho = sho
        self.color = (125,125,125)
        self.touch = False
        self.etouch = False
        self.e = False
    def draw(self,govne):
        pygame.draw.rect(govne,self.color,(self.wh,self.wh1,self.lon,self.sho))
walls = []
cantmoverightXD = False
cantmoveleftXD = False
helperr = False


b = 0



# ДЛЯ ПЕРЕМЕННЫХ
pygame.init()
govne = pygame.display.set_mode((dis,dis1))
pygame.display.set_caption("just go...")

bejim  = True

while bejim:




    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bejim = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                mouseleftclick = True

            if event.button == 3:
                mouserightclick = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:

                mouseleftclick = False
            if event.button == 3:
                mouserightclick = False

        if event.type == pygame.KEYUP and event.key == pygame.K_e:
            unpress = False



    k = pygame.key.get_pressed()


    spawncoold-=1




    if k[pygame.K_f] and spawncoold <= 0:
        spawncoold = 30


        ene.append(enemy(round(dis -37),round(dis1-600),60,37,(255,0,0),4,100,100,level,4))
    #уровни


























        









    if wipwip == []:
        wipwip.append(weapons(round(600), round(-1000), 15, 6, level))

    if wh + lon >= dis:
        level += 1
        wh=0




    if level > levelshelperjjj:
        levelshelperjjj = level

    if level == 1 and workonetime == 1 and level >= levelshelperjjj:
        ledge.append(balk(round(800), round(450), 600, 50, (0, 0, 255), level))
        ledge.append(balk(round(-150), round(450), 600, 50, (0, 0, 255), level))

        wipwip.append(weapons(round(600), round(dis1 - 12), 15, 6, level))


        shields.append(shield(round(100), round(100), 5, level))

        teleports.append(teleport(round(0), round(450 - 85), (191, 5, 247), level))
        teleports.append(teleport(round(1000), round(dis1 - 85), (191, 5, 247), level))

        ene.append(enemy(round(dis - 37), round(dis1 - 600), 60, 37, (255, 0, 0), 3, 100, 100, level,3))

        workonetime += 1
    if level == 2 and workonetime == 2 and level >= levelshelperjjj:
        wipwip = []

        workonetime += 1
        ledge = []
        ledge.append(balk(round(dis // 2 - 50), round(450), 100, 37, (0, 0, 255), level))
        teleports = []
        shields = []
        ene = []
        ene.append(enemy(round(0), round(0), 100, 61, (255, 125, 125), 3, 300, 300, level,3))

        walls.append(wall(round(450),round(-150),61,600))
        walls.append(wall(round(-150), round(450), 660, 60))





#keys
    if speed == 0:



        if jumps2 >= 0 or wh1 < dis1:

            wh1 -=(jumps2 *2)
            jumps2 -= 1
        elif jumps2 <0 and jumps2 > -20:
            wh1 -= (jumps2 * 2)
            jumps2 -= 1








        else:



            if k[pygame.K_y]:
                speed = 6
                wh = dis1 - lon
                jumps2 = 10
                hp = 100
                ene = []

                unkillcool = 150


            elif k[pygame.K_ESCAPE]:
                bejim =False






    elif speed != 0:
        if wh1 >dis1 -  sho:
            wh1 = dis1 -sho

        if k[pygame.K_LEFT] and cantmoveleftXD == False or k[pygame.K_a] and wh >= 0 and cantmoveleftXD == False:
            wh -=speed
            if wh < 0:
                wh = 0
            wright = False
        if k[pygame.K_RIGHT] and cantmoverightXD ==False or k[pygame.K_d] and wh <= dis - lon and cantmoverightXD==False:
            wh +=speed
            if wh > dis - lon:
                wh = dis - lon
            wright = True
        # UI ВРАГА И ФИЗИКА


        for kurwa in ene:

            if kurwa.ewh1 < dis1:
                if wh > kurwa.ewh and kurwa.cantmoverightXD == False:





                    kurwa.ewh += kurwa.espeed
                    kurwa.ewright = True

                if wh < kurwa.ewh and kurwa.cantmoveleftXD == False:


                    kurwa.ewh -= kurwa.espeed
                    kurwa.ewright = False

            elif kurwa.ewh1 > dis1:
                ene.pop(ene.index(kurwa))
            if kurwa.ehp <= 0:
                kurwa.eded = True
                kurwa.ehp = 0
            for kir in walls:
                if kurwa.etouch == True:
                    kurwa.ea = 1

                if kurwa.ewh1 + kurwa.esho <= kir.wh1 + 37 and kurwa.ewh1 + kurwa.esho >= kir.wh1 and kurwa.ewh <= kir.wh + kir.lon and kir.wh <= kurwa.ewh + kurwa.elon:
                    kurwa.ewh1 -= kurwa.ewh1 - kir.wh1 + kurwa.esho
                    kurwa.etouch = True
                    kir.etouch = True
                    kurwa.efall = False
                kurwa.ea = 0





            if wh + lon >= kurwa.ewh and wh <= kurwa.ewh + kurwa.elon and wh1 <= kurwa.ewh1 + kurwa.esho and wh1 + sho >= kurwa.ewh1 and fall == False and jerk == False and kurwa.ecollis == False and kurwa.eded ==False and unkillcool == 0:
                print(kurwa.ewh1)
                hp -= 50
                unkillcool = 150




            if hp <= 0:
                ded = True
                print("you dead! if you want continue press \"Y\" else press \"ESCAPE\"")
                speed = 0
                kurwa.ehp = 100
                hp = 0




            if wh + lon >= kurwa.ewh and wh <= kurwa.ewh + kurwa.elon and wh1 <= kurwa.ewh1 + kurwa.esho and wh1 + sho >= kurwa.ewh1 and fall == True and unkillcool ==0 or kurwa.eded == True :

                if kurwa.eded == False:

                    jump = True
                    coolj = 0
                    jumps = 10
                    kurwa.ehp -= 50

                    kurwa.esho -= 13

                if  kurwa.eded:


                    kurwa.espeed = 0

                    kurwa.ewh1 -= (kurwa.ejump2 * 3)
                    kurwa.ejump2 -= 1

                else:
                    kurwa.eded = False

            if wh + lon >= kurwa.ewh and wh <= kurwa.ewh + kurwa.elon and wh1 <= kurwa.ewh1 + kurwa.esho and wh1 + sho >= kurwa.ewh1 and fall == False and kurwa.eded == False and jerk == True and kurwa.ecolisspeed > 0 and kurwa.ecollis == False and unkillcool== 0 and hands1 == []:
                kurwa.ecollis = True
                jerk = False
                if wright == True:
                    defwright = True
                else:
                    defwright = False
                kurwa.ehp -= 25
                print("ok")


            elif kurwa.ecolisspeed == 0:
                kurwa.ecollis = False
                kurwa.ecolisspeed = kurwa.defecolisspeed
                defwright = False
                shootfromright = False

            if kurwa.ecollis == True:
                if defwright == True or shootfromright:
                    kurwa.ewh += kurwa.ecolisspeed
                    kurwa.ecolisspeed -= 1

                elif not (defwright):
                    kurwa.ewh -= kurwa.ecolisspeed
                    kurwa.ecolisspeed -= 1






            #здесь физика!!!и прыжок
            if kurwa.efall == False:
                kurwa.ecoolj -= 1

            if kurwa.ecoolj < 0:
                kurwa.ecoolj = 0

            if kurwa.ecoolj == 0:


                if not (kurwa.ejump) and kurwa.espeed != 0:

                    if kurwa.ewh + kurwa.esho > wh and kurwa.ewh < wh + sho and kurwa.ewh1 + kurwa.elon > wh1+sho:

                        kurwa.ejumps = 11

                        kurwa.ejump = True

                else:

                    if kurwa.ejumps >= 0:

                        kurwa.ewh1 -= kurwa.ejumps * 4
                        if kurwa.elll == True:
                            kurwa.ejumps += 1
                        kurwa.ejumps -= 1

                        kurwa.elll = not (kurwa.elll)
                        if kurwa.ejump == True:
                            kurwa.espeed = kurwa.edefspeed//100 *70

            if kurwa.ejumps == -1:
                kurwa.ejump = False
                kurwa.ecoolj = 150



            if kurwa.ewh1 + kurwa.esho < dis1 and kurwa.ejump == False and kurwa.etouch == False and kurwa.eded == False:


                kurwa.efall = True

                kurwa.ewh1 -= kurwa.ejumps * 4
                if kurwa.elll == True:
                    kurwa.ejumps += 1
                kurwa.ejumps -= 1
                if kurwa.ejumps <= -10:
                    kurwa.ejumps = -9

                kurwa.elll = not (kurwa.elll)
                if kurwa.ejump == True:
                    kurwa.espeed = kurwa.edefspeed//100 *70
            if kurwa.ewh1 + kurwa.esho > dis1 and kurwa.eded == False:
                kurwa.ewh1 = dis1 - kurwa.esho
                kurwa.efall = False


            if kurwa.ewh1 + kurwa.esho == dis1 or kurwa.etouch == True:
                kurwa.espeed = kurwa.edefspeed
            if kurwa.ejumps != 0 and kurwa.efall == False and kurwa.ejump == False:
                kurwa.ejumps = 0

                # реакция на пулю для врага
            for xd in bullets:
                if  xd.wh + xd.rad >= kurwa.ewh and xd.wh <= kurwa.ewh + kurwa.elon and xd.wh1 <= kurwa.ewh1 + kurwa.esho and xd.wh1 + xd.rad >= kurwa.ewh1  and kurwa.eded == False and unkillcool==0:
                    kurwa.ehp -= 25

                    kurwa.ecollis =True
                    if xd.bulletgo == "right":
                        kurwa.ecolisspeed = 10
                        shootfromright = True
                    else:
                        kurwa.ecolisspeed = 10

                    bullets.pop(bullets.index(xd))
            if True:
                for kik in hands1:

                    if len(hands1)>0  or len(hands1) ==2 :



                        if kik.wh >= kurwa.ewh and kik.wh +kik.sho <= kurwa.ewh + kurwa.elon and kik.wh1 <= kurwa.ewh1 + kurwa.esho and kik.wh1 + kik.hp >= kurwa.ewh1 and kurwa.eded == False :

                            kurwa.ecollis = True












                            if kik.left and len(hands1)==2 or len(hands1)==1 and wright==False:
                                ecolisspeed = 25
                                print("work")
                            elif kik.left == False and len(hands1)==2 or len(hands1) == 1 and wright:
                                kurwa.ecolisspeed = 25
                                shootfromright = True
                            if jerk == False:
                                kik.hp -= 20

                            elif jerk and jerks !=0:
                                kurwa.ehp -= 25
                                kik.hp -= 10
                                jerk = False
                                jerks = 0







                    if kik.hp <=0:
                        hands1.pop(hands1.index(kik))




































        #НЕУЯЗВИМОСТЬ

        if unkillcool == 150:
            jump = True
            jumps = 5
        if unkillcool != -0:
            unkillcool -= 1




        #keys
        if k[pygame.K_ESCAPE]:
            bejim = False



            #РЫВОК
        cooldownj -= 1


        if cooldownj < 0:
            cooldownj = 0
        if cooldownj == 0:
            if not(jerk):

                if k[pygame.K_LSHIFT] or k[pygame.K_RSHIFT]:

                    jerk =True
            else:
                if wright == True and jerks >0:
                    wh += (jerks*2) +5
                    if wh > dis - lon:
                        wh = dis - lon
                    jerks -=1
                elif jerks <=0:
                    jerk = False
                    jerks =10
                    cooldownj = FPS




                        # ЛЕВЫЙ РЫВОК
                elif wright == False and jerks >0:
                    wh -=(jerks*2) +5
                    if wh <0:
                        wh = 0
                    jerks -=1
                elif jerks <=0:
                    jerk = False
                    jerks= 10
                    cooldownj =  FPS * 7














    #ПРЫЖОК

        if fall == False:
            coolj -=1





        if coolj < 0:
            coolj = 0

        if coolj ==0:

            if not(jump) and speed != 0:

                if k[pygame.K_SPACE]:
                    jumps =11

                    jump = True

            else:




                if jumps >= 0:

                    wh1-= jumps *4
                    if lll == True:
                        jumps +=1
                    jumps -=1

                    lll = not(lll)
                    if jump == True:

                        speed = 5


        if jumps == -1:
            jump =  False
            coolj =  15




        #ПАДЕНИЕ



        if wh1 + sho < dis1 and jump == False and touch == False :



            fall = True

            wh1 -= jumps * 4
            if lll == True:
                jumps += 1
            jumps -=1
            if jumps <= -7:
                jumps = -6

            lll = not (lll)
            if jump == True:
                speed = 5
        if wh1+sho>dis1:
            wh1= dis1 - sho
        if wh1+sho == dis1 or touch == True:
            speed = 8
        if jumps !=0 and fall == False and jump == False:
            jumps = 0










            # УМЕРТВЛЕНИЕ????XD




        if hp <=0:
            ded = True

            speed = 0
            kurwa.ehp = 100
            hp = 0

        if wh1 + sho == dis1 or touch == True:
            fall = False

        touch = False



















































    govne.fill((255,255,255))


#4 ledges and walls when u touch walls and not
    for kurwa in ene:
        kurwa.etouch = False


    for heh in ledge:
        createB(heh.wh, heh.wh1, heh.lon, heh.sho)







        for kurwa in ene:

            if kurwa.etouch == True:
                kurwa.ea = 1


            if kurwa.ewh1 + kurwa.esho <= heh.wh1 + 37 and kurwa.ewh1 + kurwa.esho >= heh.wh1 and kurwa.ewh <= heh.wh + heh.lon and heh.wh <= kurwa.ewh + kurwa.elon:

                kurwa.ewh1 -= kurwa.ewh1 - heh.wh1 + kurwa.esho
                kurwa.etouch = True
                kurwa.efall = False
            kurwa.ea = 0










    for kir in walls:
        touchB(wh, wh1, lon, sho, kir.wh, kir.wh1, kir.lon, kir.sho)
        if wh1 + sho <= kir.wh1 + 37 and wh1 + sho >= kir.wh1 and wh <= kir.wh + kir.lon and kir.wh <= wh + lon:

            kir.touch = True
        else:
            kir.touch = False








    a = 0




#неуязвимость
    for heh in ledge:
        heh.drawbalk(govne)
    if unkillcool !=0 and unkillcool / 15 == int(unkillcool /15) or cooldownhelper >=1:
        if unkillcool !=0 and unkillcool / 15 == int(unkillcool /15):
            cooldownhelper = 7
        color = (255,255,255)

        cooldownhelper -= 1
    else:
        color = (0,0,0)
#teleport

    for qwe in teleports:
        qwe.draw(govne)
        if k[pygame.K_e] and wh + lon >= qwe.wh and wh <= qwe.wh + qwe.lon and wh1 <= qwe.wh1 + qwe.sho and wh1 + sho >= qwe.wh1 and unpress == False:
            teleportscolors.append(qwe.color)
            teleportscolors.append(teleports.index(qwe))
            unpress = True


            print("ok")

        if teleportscolors != [] and teleportscolors[0] == qwe.color and teleportscolors[1]!= teleports.index(qwe) :
            wh = qwe.wh + qwe.sho - lon
            wh1= qwe.wh1 +qwe.lon - sho
            teleportscolors = []






    you = pygame.draw.rect(govne,(color),(wh,wh1,lon,sho))
    # полет пули для 1 руки
    for kurwa in ene:
        hpbar(kurwa.ehp, kurwa.ewh, kurwa.ewh1,kurwa.emaxhp,kurwa.elon)
        kurwa.draw(govne)
    for piu in wipwip:

        if len(hands) == 1:
            if wright == True:
                piu.weaponinhandright(govne)
            else:
                piu.weaponinhandleft(govne)












#полет пули для 2х рук

        if len(hands) ==2:
            piu.weaponinhandright(govne)
            piu.weaponinhandleft(govne)










        
        piu.drawweapon(govne)




# выпускание пули
        if mouseleftclick == True and cooldownshot == 0 and len(hands)==1 and wright == False or mouserightclick == True and cooldownshot == 0 and len(hands)==1 and wright == False:
            print("yes")
            bullets.append(bullet(round(wh +sho//2 - lon + 5), round(wh1 + lon // 2), 15, 4,0))
            cooldownshot =30


        elif mouseleftclick == True and cooldownshot == 0 and len(hands) == 1 and wright  or mouserightclick == True and cooldownshot == 0 and len(hands) == 1 and wright :
            bullets.append(bullet(round(wh + sho//2+5), round(wh1 + lon // 2), 15, 4, 0))
            cooldownshot = 30




        if mouseleftclick == True and cooldownshot1 == 0 and len(hands)==2:

            bullets.append(bullet(round(wh +sho//2 - lon + 5), round(wh1 + lon // 2), 15, 4,"left"))
            cooldownshot1 = 30

        if mouserightclick == True and cooldownshot2==0 and len(hands)==2:
            bullets.append(bullet(round(wh + sho//2+5,wh1 + lon //2), round(wh1 + lon // 2), 15, 4,"right" ))
            cooldownshot2= 30
        for xd in bullets:
            if xd.wh > dis or xd.wh < 0:
                bullets.pop(bullets.index(xd))

    cooldownshot -= 1
    cooldownshot1 -= 1
    cooldownshot2 -= 1
    if cooldownshot == -1:
        cooldownshot = 0
    if cooldownshot1 == -1:
        cooldownshot1 = 0
    if cooldownshot2 == -1:
        cooldownshot2 = 0


    for l in shields:

        l.drawshield(govne)
        l.takeshield(wh,wh1,sho,lon)

    for kik in hands1:
        
        kik.calculatewh1()
        kik.drawshieldinhand(wh, wh1, lon, sho, govne)
#управление пулей тд куда она летит
    for xd in bullets:

        if xd.bulletgo == "left" or wright ==False and xd.bulletgo == 0:
            xd.wh-=xd.speed
            if xd.bulletgo == 0 and wright ==False:
                xd.bulletgo = "left"
        elif xd.bulletgo == "right" or wright and xd.bulletgo == 0:
            xd.wh += xd.speed
            if xd.bulletgo == 0 and wright:
                xd.bulletgo = "right"
        xd.drawbullet(govne)


        # ОРУЖИЕ
    for piu in wipwip:
        if wh + lon >= piu.wh and wh <= piu.wh + piu.lon and wh1 <= piu.wh1 + piu.sho and wh1 + sho >= piu.wh1 and len(hands) <=1:
            wipwip.pop(wipwip.index(piu))
            hands.append("pistol")

    # wallwallwallwallXD
    for kir in walls:


        if wh + lon >= kir.wh and wh <= kir.wh + kir.lon and wh1 <= kir.wh1 + kir.sho and wh1 + sho >= kir.wh1  :


            if wh1 < kir.wh1 + kir.sho and jump == True and wh + lon > kir.wh + 1 and wh < kir.wh + kir.lon - 1 and kir.touch == False and helperr == False and wh1 - 37 < kir.wh1+kir.lon and wh1 >0:

                jump = False
                fall = True
                jumps = 0
                wh1 = kir.wh1 + kir.sho + 1
                coolj = defcoolj





            elif wh + lon >= kir.wh and kir.touch == False and wright :

                jerk = False
                jerks = 0
                cantmoverightXD = True


                helperr = True
                wh = kir.wh - lon

            elif wh <= kir.wh + kir.lon and kir.touch == False and wright ==False  :
                wh = kir.wh +kir.lon
                jerk = False
                jerks = 0
                cantmoveleftXD = True

                helperr = True
            if helperr:
                break







        else:
            cantmoverightXD = False
            cantmoveleftXD = False
    helperr = False
    for kurwa in ene:
        for kir in walls:

            if kurwa.ewh + kurwa.elon >= kir.wh and kurwa.ewh <= kir.wh + kir.lon and kurwa.ewh1 <= kir.wh1 + kir.sho and kurwa.ewh1 + kurwa.elon >= kir.wh1:

                if kurwa.ewh1 < kir.wh1 + kir.sho and kurwa.ejump == True and kurwa.ewh + kurwa.esho > kir.wh + 1 and kurwa.ewh < kir.wh + kir.lon - 1 and kir.etouch == False and kurwa.ehelperr == False and wh1 - 37 < kir.wh1 + kir.lon:

                    kurwa.ejump = False
                    kurwa.efall = True
                    kurwa.ejumps = 0
                    kurwa.ewh1 = kir.wh1 + kir.sho + 1
                    kurwa.ecoolj = kurwa.edefcoolj

                elif kurwa.ewh <= kir.wh + kir.lon and kir.etouch == False and kurwa.ewright == False:
                    kurwa.ewh = kir.wh + kir.lon

                    kurwa.ecantmoveleftXD = True

                    kurwa.ehelperr = True



                elif kurwa.ewh + kurwa.elon >= kir.wh and kir.etouch == False and kurwa.ewright:

                    kurwa.ecantmoverightXD = True

                    kurwa.ehelperr = True
                    kurwa.ewh = kir.wh - kurwa.elon




                else:
                    kurwa.ehelperr = False

                if kurwa.ehelperr:
                    break







                else:
                    kurwa.ecantmoverightXD = False
                    kurwa.ecantmoveleftXD = False
    for kurwa in ene:

        kurwa.ehelperr = False


    for kir in walls:
        kir.draw(govne)


    hpbar(hp, wh, wh1, 100, lon)

    pygame.display.update()





