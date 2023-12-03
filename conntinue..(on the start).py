import pygame
import time

# УСТУПЫ

class balk:
    wh = -150
    wh1 = 450
    sho = 50
    lon = 600
a =0
class balk1():
    wh = 800
    wh1 = 450
    sho = 50
    lon = 600

#команды

touch = False
def hpbar(hp,wh,wh1):
    pygame.draw.rect(govne,(125,125,125),(wh-26,wh1-26,100,12))
    pygame.draw.rect(govne,(255,0,0),(wh-26,wh1-26,hp,12))


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



    pygame.draw.rect(govne,(0,0,255),(bwh,bwh1,blon,bsho))
    touchB(wh,wh1,lon,sho,bwh,bwh1,blon,bsho)










 # ДЛЯ ПЕРЕМЕННЫХ!
dis = 1250
dis1 = 750
FPS = 60
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

wright = True
defwright = False
#ENEMYS
class enemy:

    elon = 37
    esho = 37
    ewh = 0 + esho
    ewh1 = dis1 - elon
    espeed = 4
    eded = False
    ejump2 = 10
    ecollis = False
    ecolisspeed =30
    defecolisspeed = ecolisspeed
    ehp=100
    ejump = False
    elll = False
    efall = False
    ejumps = 10
    enemys = []
wave = 1

class enemyS(enemy):
    sword = 1
    sewh = 1000
    sewh1 = 200
    selon = lon
    sesho = sho





class enemyJ(enemy):
    ejump = False
    ejumps = 10









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
    k = pygame.key.get_pressed()



    # КЛЮЧИ!
    if speed == 0:


        if jumps2 >= 0:

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
                enemy.ewh = 0 + enemy.esho
                hp = 100
            elif k[pygame.K_ESCAPE]:
                bejim =False






    elif speed != 0:
        if wh1 >dis1 -  sho:
            wh1 = dis1 -sho

        if k[pygame.K_LEFT] or k[pygame.K_a] and wh >= 0:
            wh -=speed
            if wh < 0:
                wh = 0
            wright = False




        if k[pygame.K_ESCAPE]:
            bejim = False

        if k[pygame.K_RIGHT] or k[pygame.K_d] and wh <= dis - lon:
            wh +=speed
            if wh > dis - lon:
                wh = dis - lon
            wright = True

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



        if wh1 + sho < dis1 and jump == False and touch == False:



            fall = True

            wh1 -= jumps * 4
            if lll == True:
                jumps += 1
            jumps -=1
            if jumps <= -10:
                jumps = -9

            lll = not (lll)
            if jump == True:
                speed = 5
        if wh1+sho>dis1:
            wh1= dis1 - sho
        if wh1+sho == dis1 or touch == True:
            speed = 8
        if jumps !=0 and fall == False and jump == False:
            jumps = 0










            #НАПАДЕНИЕ ВРАГА!
        if wh > enemy.ewh:
            enemy.ewh += enemy.espeed
        elif wh < enemy.ewh:
            enemy.ewh -= enemy.espeed
        if enemy.ehp <= 0:
            enemy.eded = True



        if wh + lon >= enemy.ewh and wh <= enemy.ewh + enemy.elon and wh1 <= enemy.ewh1 + enemy.esho and wh1 + sho >= enemy.ewh1 and fall == True or enemy.eded == True:

            if enemy.eded == False:
                jump = True
                coolj =0
                jumps = 10
                enemy.ehp -=50
                enemy.elon *= 2
                enemy.esho -= 19

            if enemy.ejump2 >= -20 and enemy.eded:

                enemy.espeed = 0

                enemy.ewh1 -= (enemy.ejump2 * 3)
                enemy.ejump2 -= 1

            else:
                enemy.eded = False
                wave += 1


                pygame.draw.rect(govne,(255,0,0),(enemyS.sewh , enemyS.sewh1, enemyS.selon,enemyS.sesho))

        elif wh + lon >= enemy.ewh and wh <= enemy.ewh + enemy.elon and wh1 <= enemy.ewh1 + enemy.esho and wh1 + sho >= enemy.ewh1 and fall == False  and enemy.eded == False and jerk == False and enemy.ecollis == False:


            hp -= 50



        if hp <=0:
            ded = True
            print("you dead! if you want continue press \"Y\" else press \"ESCAPE\"")
            speed = 0
            enemy.ehp = 100
            hp = 0

        if wh1 + sho == dis1 or touch == True:
            fall = False

        touch = False

        if wh + lon >= enemy.ewh and wh <= enemy.ewh + enemy.elon and wh1 <= enemy.ewh1 + enemy.esho and wh1 + sho >= enemy.ewh1 and fall == False  and enemy.eded == False and jerk == True and enemy.ecolisspeed > 0 and enemy.ecollis ==False:


            enemy.ecollis = True
            jerk = False
            if wright == True:
                defwright = True
            else:
                defwright=False
            enemy.ehp -=25


        elif enemy.ecolisspeed ==0:
            enemy.ecollis = False
            enemy.ecolisspeed = enemy.defecolisspeed
            defwright = False
        if enemy.ecollis == True:
            if defwright == True :
                enemy.ewh += enemy.ecolisspeed
                enemy.ecolisspeed -= 1

            if not(defwright) :
                enemy.ewh -= enemy.ecolisspeed
                enemy.ecolisspeed -= 1













































        # Kлючи!
        #ПЕРСЫ


    govne.fill((255,255,255))

    createB(balk1.wh,balk1.wh1,balk1.lon,balk1.sho)
    createB(balk.wh, balk.wh1, balk.lon, balk.sho)

    a = 0

    print(hp)
    hpbar(hp,wh,wh1)
    hpbar(enemy.ehp,enemy.ewh,enemy.ewh1)
    b = pygame.draw.rect(govne,(0,0,255),(balk.wh,balk.wh1,balk.lon,balk.sho))
    you = pygame.draw.rect(govne,(0,0,0),(wh,wh1,lon,sho))
    en = pygame.draw.rect(govne,(255,0,0),(enemy.ewh,enemy.ewh1,enemy.elon,enemy.esho))
        #ПЕРСЫ


    pygame.display.update()





