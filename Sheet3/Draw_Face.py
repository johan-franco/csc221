from gasp import *

# (300,250), 200 is what we used 
x =int(input("Insert x position of face:\n"))
y = int(input("Insert y position of face:\n"))
size = int(input("How big do you want the face?\n"))

#x = 300 
#y = 200
#size = 300


def face_maker(x , y, s):
    face_cords = (int(x),int(y))
    face_rad = int(size)
    face_dam = int(size) * 2

    eyesize = face_rad/8
    lefteyex  = face_cords[0] - (face_rad/2)
    righteyex = face_cords[0] + (face_rad/2)
    eye_ypos = face_cords[1] + (face_rad/4)

    print(eye_ypos)

    x_nose_end = eyesize + lefteyex 
    y_bottom_nose = (face_cords[1] - face_rad) + (face_rad*(3/4))

    arc_ypos = face_cords[1]*6/5
    arc_rad  = face_rad
    
    if 0 < face_rad < 150:
        arc_ypos = face_cords[1]*11/10
    else:
        pass

    
    ear_y = (size * 5/4) + (face_cords[1]-face_rad)
    ears = size *1/4

    brow_y = size*4/5 + (face_cords[1]-size)
    brow_s = size *3/4

    

    begin_graphics()

    Circle(face_cords, face_rad)

    #Eyes
    Circle((lefteyex, eye_ypos), eyesize)
    Circle((righteyex,eye_ypos),eyesize)

    #Nose
    Line((face_cords[0],eye_ypos), (x_nose_end + (1/10 * face_rad), y_bottom_nose))
    Line(( x_nose_end + (1/10 * face_rad), y_bottom_nose), ((righteyex - eyesize - (1/10 *face_rad)), y_bottom_nose))

    #Mouth
    Arc((face_cords[0], arc_ypos), arc_rad, 230, 310)

    #Eyebrows
    Arc((lefteyex, brow_y), brow_s, 110,70)
    Arc((righteyex,brow_y), brow_s, 110,70)

    #Ears
    Arc((face_cords[0]+size,ear_y),ears, -90,120)
    Arc((face_cords[0]-size,ear_y),ears, 270,60)

    #body
    body = input("Full body? (y/n)\n")
    if body == 'y':
        torso_start  = face_cords[1]-size
        torso_end = torso_start -face_dam

        #torso 
        Line((face_cords[0], torso_start), (face_cords[0], torso_end))

        #arms
        Line((face_cords[0], torso_start - size* 1/4), (face_cords[0]-size, torso_start - size*3/4))
        Line((face_cords[0],torso_start - size * 1/4 ), (face_cords[0]+size, torso_start - size*3/4 ))

        #legs
        Line((face_cords[0], torso_end), ( face_cords[0] - (size*3/4), torso_end-face_dam))
        Line((face_cords[0], torso_end), ( face_cords[0] + (size*3/4), torso_end-face_dam))
    
    #Hat
    hat = input("Hat?(y/n) \n")
    if hat == 'y':
        hat_leftx = face_cords[0] - face_rad/2
        hat_rightx = face_cords[0] + face_rad/2

        hat_basey = face_cords[1] + face_rad
        hat_tip = hat_basey + face_dam/2
        hatsize = size *1/8

        Line((hat_leftx, hat_basey ), (hat_rightx , hat_basey))
        Line((hat_leftx, hat_basey), (face_cords[0], hat_tip))
        Line((hat_rightx, hat_basey), ( face_cords[0], hat_tip))
        Circle((face_cords[0] , hat_tip+hatsize), hatsize)

    update_when('key_pressed')
    end_graphics()
face_maker(x , y, size)