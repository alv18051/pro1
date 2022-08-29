#Programa principal
import random
from shaders import *
from gl import *
from obj import *
from texture import *
width = 1080  #alto de la pantalla
height = 1920 #ancho de la pantalla
rende = Renderer(height,width)

rende.background = Texture("back.bmp")
rende.glClearBackground()

rende.active_shader = pride
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/campfireS.obj",translate=V3(0,0,-13),rotate=V3(0,90,0),scale=V3(4,4,4))

rende.active_shader = thermal
rende.active_texture = Texture("Mouse_D.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(3,0,-5),rotate=V3(0,-90,0),scale=V3(1,1,1))

rende.active_shader = nightVision
rende.active_texture = Texture("Kitty_001_DIFF.bmp")
rende.glLoadModel("models/KittyS.obj",translate=V3(-5,0,-10),rotate=V3(0,90,0),scale=V3(1,1,1))

rende.active_shader = colorblind
rende.active_texture = Texture("Sting_Base_Color.bmp")
rende.normal_map = Texture("models/Sting_Normal.bmp")
rende.glLoadModel("models/swordS.obj",translate=V3(2.5,0.2,-10),rotate=V3(0,90,90),scale=V3(1,1,1))

rende.active_shader = aura
rende.active_texture = Texture("handgun_Te.bmp")
rende.normal_map = Texture("models/handgun_No.bmp")
rende.glLoadModel("models/gunS.obj",translate=V3(-3,0.5,-10),rotate=V3(0,0,0),scale=V3(7,7,7))





rende.glFinish("./salida.bmp")