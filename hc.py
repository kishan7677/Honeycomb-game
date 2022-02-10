import pygame
import random
pygame.init()
win =pygame.display.set_mode((500,500))
pygame.display.set_caption("honeycamp")
tree_x=550
tree_y=0
tree1_x=950
tree1_y=0
comb_x=100
comb_y=200
score=0
bg_audio=pygame.mixer.Sound(r"A:/honey/bee1.mp3")
score_audio=pygame.mixer.Sound(r"A:/honey/yep.wav")
crash_audio=pygame.mixer.Sound(r"A:/honey/crash.wav")
image=pygame.image.load(r"A:/honey/cloud3.jpg")
bird=pygame.image.load(r"A:/honey/bird.jpeg")
bar=pygame.image.load(r"A:/honey/tree.jpeg")
bar1=pygame.image.load(r"A:/honey/tree1.jpeg")
gameover=False
run= True
clock=pygame.time.Clock()
bg_audio.play(10)

while run:
    win.blit(pygame.transform.scale(image,(500,500)),(0,0))
    tree_x-=5
    tree1_x-=5
    comb_y+=10
    pygame.time.delay(70)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_UP):
                comb_y-=20
                comb_y-=20
                
    if(tree_x>540):
        tree_h1=random.randint(0,300)
        tree_h2=500-tree_h1-150
        
    if(tree1_x>540):
        tree1_h1=random.randint(0,300)
        tree1_h2=500-tree1_h1-150
        
    if(tree_x==-200):
        tree_x=600
        
    if(tree1_x==-200):
        tree1_x=600

    win.blit(pygame.transform.scale(bar,(100,tree_h1)),(tree_x,tree_y))
    win.blit(pygame.transform.scale(bar1,(100,tree_h2)),(tree_x,tree_h1+150))
    win.blit(pygame.transform.scale(bar,(100,tree1_h1)),(tree1_x,tree1_y))
    win.blit(pygame.transform.scale(bar1,(100,tree1_h2)),(tree1_x,tree1_h1+150))
    win.blit(pygame.transform.scale(bird,(50,50)),(comb_x-25,comb_y-25))
    pygame.display.update()
    win.fill((0,0,0))

    if(tree_x==70 or tree1_x==70):
        score+=1
        score_audio.play()
    if(comb_y<25 or comb_y>475):
        gameover=True
        
    elif (((tree_x >= 25) and (tree_x <= 125)) and ((comb_y >= tree_h1+150-25 and comb_y <= 475) or (comb_y >= 25 and comb_y <= tree_h1 + 25))):
       gameover=True
       
    
    elif (((tree1_x >= 25) and (tree1_x <= 125)) and ((comb_y >= tree1_h1+150-25 and comb_y <= 475) or (comb_y >= 25 and comb_y <= tree1_h1 + 25))):
       gameover=True
    
    if gameover:
        crash_audio.play()
        bg_audio.stop()
        print("score="+str(score))
        pygame.time.delay(2000)
        crash_audio.stop()
        run=False
    
    
pygame.quit()

       

