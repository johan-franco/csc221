from gasp import *

def moan():
    print("Python is useless \nAnd so are these worksheets")



# (300,250), 200 is what we used 
#x =input("Insert x position of face")
#y = input("Insert y position of face")
#size = input("How big do you want the face?")

x = 300
y = 250
size = 200



face_cords = (int(x),int(y))
face_rad = int(size)

eyesize = face_rad/8
lefteyex  = face_cords[0] - (face_rad/2)
righteyex = face_cords[0] + (face_rad/2)
eye_ypos = face_cords[1] + (face_rad/4)

print(eye_ypos)

x_nose_end = eyesize + lefteyex 
y_bottom_nose = (face_cords[1] - face_rad) + (face_rad*(3/4))

arc_ypos = face_cords[1]*6/5
arc_rad  = face_rad
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
Arc((lefteyex,200), 150, 110,70)
Arc((righteyex,200), 150, 110,70)

#Ears
Arc((face_cords[0]+size,300),50, -90,120)
Arc((face_cords[0]-size,300),50, 270,60)
update_when('key_pressed')     
end_graphics()

moan()