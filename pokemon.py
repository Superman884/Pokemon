import pygame
import mouse
import keyboard
from time import sleep
from random import randrange
pygame.font.init()
#fonts
myfont = pygame.font.SysFont('Papyrus', 30,True)
otherfont = pygame.font.SysFont('Arial', 20,True)
win=pygame.display.set_mode((1200,700))
#images
img1=pygame.image.load("hp_thing.png")
img2=pygame.image.load("hp_thing1.png")
img3=pygame.image.load("hp_thing2.png")
bling=pygame.image.load('block.png')
stuff=pygame.image.load('thungy.png')
writing_img=pygame.image.load("other_stuff.png")
bg=pygame.image.load("background.png")
eev_img=pygame.image.load("eevee_img.png")
normal_ani=pygame.image.load("Hit_ani.png")
bite_ani=pygame.image.load("bite_ani.png")
howl_ani=pygame.image.load("howl_img.png")
up_ani=pygame.image.load("up_ani.png")
slash_ani=pygame.image.load('slash_img.png')
thund_real=[pygame.image.load('thunder_img.png'),pygame.image.load('thunder_img2.png')]
fire_ani=pygame.image.load('fire_img.png')
water_ani=pygame.image.load('water_gun.png')
for i in range(2):
	thund_real[i]=pygame.transform.scale(thund_real[i],(80,80))
#variables
numby2=0
width=167
angle=0
c=0
number=0
draw=True
fallen=False
boost=False
move1=''
move1_real=''
move2=''
texty=''
crit=1
run=True
superrun=True
timer=0
pokemony='r'
atk_mod=1
bp2=0
pok1x=680-20
pok1y=380+70
pok2x=1020-50
pok2y=80+80
firex=20
firey=20
ychange=0
numby=0
burntick=False
#classes
class pokeman:
	def __init__(self,x,y,hp,atk,name,effwith='none'):
		self.x=x
		self.y=y
		self.hp=hp
		self.max_hp=self.hp
		self.atk=atk
		self.curr_hp=hp
		self.name=name
		self.effwith=effwith
class block:
	def __init__(self,x,y,name,bp,acc,crit_cha,effect='none',effcha=0):
		self.x=x
		self.y=y
		self.name=name
		self.bp=bp
		self.acc=acc
		self.crit_cha=crit_cha
		self.effect=effect
		self.effcha=effcha
opp_moves=[block(800,800,"tackle",35,95,1),block(800,800,"bite",50,100,2), block(800,800, "poison tail", 45, 80, 15, 'burn', 30)]
pokemon=[pokeman(680,380,100,50,"pikachu"),pokeman(1020,80,200,20,"eevee")]
pokemon_imgs=[pygame.image.load("pikachu_img.png"),pygame.image.load("charm_img.png"),pygame.image.load("squirt_img.png")]
x=randrange(3)
pik_img=pokemon_imgs[x]
pik_img=pygame.transform.flip(pik_img,True,False)
pik_img_real=pik_img
if x==0 :
	blocks=[block(20,350,"headbutt",40,85,1,'flinch',30),block(300,350,"thunder",50,80,2,'paralyz',20)]
	pokemon[0].hp=40
	pokemon[0].max_hp=40
	pokemon[0].curr_hp=pokemon[0].hp
elif x==1:
	blocks=[block(20,350,"howl",20,100,1),block(300,350,"ember",50,100,2,'burn',20),block(20,470,"mega-punch",80,50,2,'none',0)]
	pokemon[0].name='charmander'
	pokemon[0].hp=60
	pokemon[0].max_hp=60
	pokemon[0].curr_hp=pokemon[0].hp
else:
	blocks=[block(20,350,"slash",60,75,15),block(300,350,"water gun",50,100,2)]
	pokemon[0].name='squirtle'
	pokemon[0].hp=100
	pokemon[0].max_hp=100
	pokemon[0].curr_hp=pokemon[0].hp
while run and superrun:
	c+=1
	if c%3==0:
		number+=1
	thund_ani=thund_real[number%2]
	win.blit(bg,(600,0))
	bg=pygame.image.load("background.png")
	win.blit(writing_img,(0,600))
	if pokemon[0].hp==pokemon[0].curr_hp or draw:
		win.blit(pik_img,(pok1x,pok1y))
	if pokemon[1].hp==pokemon[1].curr_hp or draw:
		win.blit(eev_img,(pok2x,pok2y))
	if pokemon[0].curr_hp==pokemon[0].hp and pokemon[1].curr_hp==pokemon[1].hp and timer==0 and move1=='' and move2=='' and burntick==False:
		texty=myfont.render('', False, (255, 0, 0))
		for i in blocks:
			textsurface = myfont.render(str(i.name), False, (0, 0, 0))
			win.blit(bling,(i.x,i.y))
			win.blit(textsurface,(i.x+200/(len(str(i.name))-1),i.y+25))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			superrun=False
		if event.type == pygame.MOUSEBUTTONUP and pokemon[0].curr_hp==pokemon[0].hp and pokemon[1].curr_hp==pokemon[1].hp and timer==0:
			pressed=False
			mousex=pygame.mouse.get_pos()[0]
			mousey=pygame.mouse.get_pos()[1]
			for i in blocks:
				if mousex>i.x and mousex<i.x+200 and mousey>i.y and mousey<i.y+100:
					move1=i.name
					move1_real=move1
					power=i.bp
					accuracy=i.acc
					crity=i.crit_cha
					movef=i.effect
					movefcha=i.effcha
					movie=opp_moves[randrange(3)]
					bp2=movie.bp
					move2=movie.name
					move2_real=move2
					move2crity=movie.crit_cha
					move2f=movie.effect
					move2fcha=movie.effcha
					print(movie.crit_cha)
	if timer>0:
		timer-=1
	if fallen:
		win.blit(howl_ani,(pokemon[0].x+120,pokemon[0].y+120))
		if timer>=25:
			width-=2
			pok1x+=1
		else:
			width+=2
			pok1x-=1
		pik_img=pygame.transform.scale(pik_img_real,(width,201))
	if boost:
		win.blit(up_ani,(pokemon[0].x+10,pokemon[0].y+40))
	if move1=='ember':
		firex=pokemon[0].x+120
		firey=pokemon[0].y+60
	if move1=='water gun':
		firex=pokemon[0].x+120
		firey=pokemon[0].y+30
		ychange=8
	if move1=='howl':
		texty=myfont.render(str(pokemon[0].name)+' used '+str(move1), False, (255, 0, 0))
		atk_mod+=0.4
		move1=''
		timer=50
		fallen=True
		c=30
	elif pokemon[0].hp==pokemon[0].curr_hp and timer==0 and fallen:
		texty=myfont.render(str(pokemon[0].name)+"'s attack rose! "+str(move1), False, (255, 0, 0))
		fallen=False
		timer=50
		boost=True
	elif move1!='':
		texty=myfont.render(str(pokemon[0].name)+' used '+str(move1), False, (255, 0, 0))
		if randrange(100)<accuracy:
			hit=True
			crit=randrange(100)
			if crit<=4*crity:
				crit=1.5
			else:
				crit=1
			if timer<=0:
				pokemon[1].curr_hp-=(((pokemon[0].atk*atk_mod*(power/50))*crit))//1
				if pokemon[1].curr_hp<=-1:
					pokemon[1].curr_hp=-1
				move1=''
				pressed=True
				timer=50
			if randrange(100)<movefcha and pokemon[1].effwith=='none':
				pokemon[1].effwith=movef
				if pokemon[1].effwith=='burn':
					burntick=True
				timer=50
				numby=50
		else:
			texty=myfont.render(str(pokemon[0].name)+' missed ' + move1, False, (255, 0, 0))
			move1=''
			timer=50
			hit=False
	elif crit>1.0 and pokemon[1].curr_hp==pokemon[1].hp and timer==0:
		texty=myfont.render(str('critical hit!'),False,(255,0,0))
		crit-=0.02
	if (numby!=0) and timer==0 and (pokemon[1].hp==pokemon[1].curr_hp or pokemon[0].hp==pokemon[0].curr_hp) and movef!='flinch':
		victim=pokemon[1]
		if victim.effwith=='none':
			victim=pokemon[0]
		texty=myfont.render(victim.name+' was '+victim.effwith+'ed', False, (255, 0, 0))
		numby=0
		print('hello')
	elif move2!='' and pokemon[1].hp==pokemon[1].curr_hp and timer==0:
		move1_real=''
		if pokemon[1].effwith=="paralyz" and randrange(4)==0:
			texty=myfont.render(str(pokemon[1].name)+' was fully paralyzed!', False, (255, 0, 0))
			move2=''
			timer=50
		elif movef=='flinch' and randrange(100)<movefcha and hit:
			texty=myfont.render(str(pokemon[1].name)+' flinched!', False, (255, 0, 0))
			move2=''
			timer=50
		elif movie.acc>randrange(100):
			if randrange(100)<move2fcha and pokemon[0].effwith=='none':
				pokemon[0].effwith=move2f
				# if pokemon[0].effwith=='burn':
				# 	burntick=True
				timer=0
				numby=50
			boost=False
			crit=randrange(100)
			if crit<=move2crity:
				crit=1.5
			else:
				crit=1
			pokemon[0].curr_hp-=((pokemon[1].atk*bp2/50*crit))//1
			if pokemon[0].curr_hp<=-1:
				pokemon[0].curr_hp=-1
			texty=myfont.render(str(pokemon[1].name)+' used '+str(move2), False, (255, 0, 0))
			move2=''
			pressed=True
			timer=50
		else:
			texty=myfont.render(str(pokemon[1].name)+' missed ' +move2, False, (255, 0, 0))
			timer=50
			pressed=True
			move2=''
	elif crit>1.0 and pokemon[0].curr_hp==pokemon[0].hp and pokemon[1].hp==pokemon[1].curr_hp and timer>0:
		texty=myfont.render(str('critical hit!'),False,(255,0,0))
		crit-=0.02
	if move1_real=='mega-punch' and timer>0 and hit:
		bg=pygame.image.load('black.png')
	for pikachu in pokemon:
		win.blit(stuff,(pikachu.x-100,pikachu.y-30))
		win.blit(otherfont.render(str(pikachu.name), False, (0, 0, 0)),(pikachu.x-50,pikachu.y-20))
		for x in range(pikachu.x,pikachu.x+100,1):
			win.blit(img2,(x,pikachu.y))
		for x in range(pikachu.x,int(pikachu.x+(pikachu.hp/pikachu.max_hp*100)//1),1):
			win.blit(img1,(x,pikachu.y))
	if pokemon[0].hp!=pokemon[0].curr_hp and timer!=0:
		if timer>=30:
			pok2x-=2
			draw=True
		if timer<=30 and timer>=10:
			pok2x+=2
		if timer<=10:
			if move2_real=='bite':
				img=bite_ani 
			else:
				img=normal_ani
			win.blit(img,(pok1x+50,pok1y+50))
	if pokemon[1].hp!=pokemon[1].curr_hp and timer!=0 and move1_real!='':
		if move1_real=='thunder':
			draw=True
			win.blit(thund_ani,(pokemon[1].x,pokemon[1].y+150))
		elif move1_real=='water gun':
			firey-=ychange
			if timer>=20:
				draw=True
				firex+=6.1
				ychange-=0.15
			else:
				ychange=-1
				water_ani=pygame.image.load('drops.png')
			win.blit(water_ani,(firex,firey))
		elif move1_real=='ember':
			draw=True
			win.blit(fire_ani,(firex,firey))
			firey-=4.2
			firex+=4.7
		elif timer>=30:
			pok1x-=2
			draw=True
		elif timer<=30 and timer>=10:
			pok1x+=2
		elif timer<=10:
			if move1_real=='bite':
				img=bite_ani
			elif move1_real=='slash':
				img=slash_ani
			elif move1_real=='mega-punch':
				img=pygame.image.load('fist_img.png')
			else:
				img=normal_ani
			win.blit(img,(pok2x+50,pok2y+50))
	water_ani=pygame.image.load('water_gun.png')
	if pokemon[1].effwith=='burn' and timer==0 and pokemon[1].hp==pokemon[1].curr_hp and pokemon[0].hp==pokemon[0].curr_hp and move1=='' and move2=='' and crit<=1.0 and burntick==True:
		pokemon[1].curr_hp-=pokemon[1].max_hp*0.1
		burntick=False
		move1_real=''
		move2_real=''
		texty=myfont.render(pokemon[1].name+' was hurt by its burn!', False, (255, 0, 0))
	if pokemon[1].hp>pokemon[1].curr_hp and timer==0:
		pokemon[1].hp-=1
	elif pokemon[0].hp>pokemon[0].curr_hp and timer==0:
		pokemon[0].hp-=1
	sleep(0.03)
	if texty!='':
		win.blit(texty,(60,620))
	pygame.display.update()
	win.fill((0,0,0))
	if pokemon[0].hp==0:
		texty=myfont.render(pokemon[1].name+' won!', False, (255, 0, 0))
		run=False
	if pokemon[1].hp==0:
		texty=myfont.render(pokemon[0].name+' won!', False, (255, 0, 0))
		run=False
	if c%5==0 and timer<=0:
		draw=not draw
run=True
while run and superrun:
	win.blit(bg,(600,0))
	bg=pygame.image.load("background.png")
	win.blit(writing_img,(0,600))
	win.blit(pik_img,(pok1x,pok1y))
	win.blit(eev_img,(pok2x,pok2y))
	if pokemon[0].hp==0:
		texty=myfont.render(pokemon[1].name+' won!', False, (255, 0, 0))
	if pokemon[1].hp==0:
		texty=myfont.render(pokemon[0].name+' won!', False, (255, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	for pikachu in pokemon:
		win.blit(stuff,(pikachu.x-100,pikachu.y-30))
		win.blit(otherfont.render(str(pikachu.name), False, (0, 0, 0)),(pikachu.x-50,pikachu.y-20))
		for x in range(pikachu.x,pikachu.x+100,1):
			win.blit(img2,(x,pikachu.y))
		for x in range(pikachu.x,int(pikachu.x+(pikachu.hp/pikachu.max_hp*100)//1),1):
			win.blit(img1,(x,pikachu.y))
	win.blit(texty,(150,620))
	pygame.display.update()
	win.fill((0,0,0))
