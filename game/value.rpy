init python:
    destroy = 0
    equal = 0
    rine_dia = 0

image side read nom:
    "scgread_nom.png"

image side prin nom:
    "scgprin_nom.png"
    
image side seng nom:
    align(.9, 1.0)
    "seng_nom.png"

image side rine nom:
    align(.9, 1.0)
    "rine_nom.png"

image side rine ang:
    align(.1, 1.0)
    "rine_ang.png"

image side seng smile:
    "seng_smile.png"

image side seng sad:    
    "seng_sad.png"

image side seng ang:
    "seng_ang.png"

image bignightschool:
    zoom 2.0
    align (.5, .5)
    "bg_nightschool.jpg"
    linear 0.4 align (.5, .3)
    linear 0.4 align (.5, .5)
    repeat(6.0)

transform running:
    zoom 2.0
    align(.5, .5)
    linear 0.4 align (.5, .3)
    linear 0.4 align (.5, .5)
    repeat(1.6)

image bg_roomblack = im.MatrixColor("bg_roomc.jpg", im.matrix.saturation(0.0))
image bg_clubblack = im.MatrixColor("bg_club.jpg", im.matrix.invert())
define bg_clubblack = im.MatrixColor("bg_club.jpg", im.matrix.saturation(0.0))
image seng_nomi = im.MatrixColor("seng_nom.png", im.matrix.invert())
image bg_clubred =  im.MatrixColor(bg_clubblack, im.matrix.colorize("#DF0101", "#1C1C1C"))
image seng_nomii = im.MatrixColor("seng_nom.png", im.matrix.colorize("#DF0101", "#1C1C1C"))
image seng_mamiru = im.Crop("seng_nom.png", (0, 254, 250, 307))
define seng_mamiru = im.Crop("seng_nom.png", (0, 254, 250, 307))
image seng_mamirui = im.MatrixColor(seng_mamiru, im.matrix.colorize("#DF0101", "#1C1C1C"))
image seng_mamiruii = im.MatrixColor(seng_mamiru, im.matrix.invert())
image mon_rine = im.MatrixColor("rine_ang.png", im.matrix.colorize("#DF0101", "#000000"))
image bg_red = im.MatrixColor("bg_black.png", im.matrix.colorize("#f00000", "#DF0101"))
image side another nom:
    "seng_another"

init python:
    #style.default.line_leading = 12

    style.my_style=Style(style.default)
    #style.say_thought.line_leading=10
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 10
    style.ruby_style.yoffset=-20
    style.default.ruby_style=style.ruby_style


image daruma_nomalhover = im.MatrixColor("daruma_nomal.png", im.matrix.invert())

transform goaway:
    linear 1.0 align(.5, -3.0)

transform earthquake:
    "bg_black.png"
    pause (0.01)
    "bg_white.png"
    pause (0.01)
    repeat(20.0)
transform search:
    align(1.0, .5)
    linear 1.0 zoom 2.0
    linear 1.0 align(.0, .5)
    linear 1.0 align(1.0, .5)
    linear .5 align(.5, .5)
    linear 1.0 zoom 1.0
#
init python:
    temp=None
    rine = Character("리네", color="#DF0101", image="rine")
    main = Character("[temp]", color="#6E6E6E")
    seng = Character("성", color="#91ff6d", image="seng")
    teacher=Character("안톤", color="#000000", image="read")
    anotherseng=Character("???", who_color="#3b0b30", what_color="#3b0b30", image="another")
    strange = Character("의문의 목소리", who_color="#0404B4")
    prin = Character("교장", color="#660099", image="prin")
    seng1 = Character("성?", what_color="#DF0101", who_color="#DF0101")
    style.window.left_padding=30
    a=0
    b=0

define right = Position(xalign=1.0, yalign=1.0)
define left = Position(xalign=.1, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define nvlnarr=Character(None, kind=nvl)

screen itai:
    hbox:
        text "{color=#DF0101}아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파{/color}"
