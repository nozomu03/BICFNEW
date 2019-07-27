init python:
    destroy = 0
    equal = 0
    rine_dia = 0
    rine_mis = 0
    anton_miss = 0
    truething=False

    style.newBar=Style(style.bar)
    #style.newBar.thumb=Image("thumb.png")
    #style.newBar.tumb_offset = 13
    style.newBar.left_gutter = 10
    style.newBar.right_gutter = 10
    style.newBar.left_bar = Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    style.newBar.right_bar = Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

    style.Buttoncolor=Style(style.button)
    style.Buttoncolor.background="#ffffff"

image bg_hallway2:
    "bg_hallway.jpg"
    zoom 1.5

image bad_noms:
    align(.5, 1.0)
    "bad_nom.png"
    linear 0.4 zoom .7 align (.5, .7)

image bg_bigdoor:
    align (.5, 1.0)
    zoom 1.2
    "bg_bigdoor.png"

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
    zoom 1.85
    align (.5, .5)
    "bg_nightschool"
    linear 0.4 align (.5, .3)
    linear 0.4 align (.5, .5)
    repeat(6.0)

image bg_nightschool:
 #   zoom 1.1
    align(.3, 1.0)
    "bg_nightschool.jpg"


transform running:
    zoom 2.0
    align(.5, .5)
    linear 0.4 align (.5, .3)
    linear 0.4 align (.5, .5)
    repeat(1.6)

transform backrunning:
    zoom 2.0
    align (.5, .5)
    linear .4 align (.5, .3) zoom 1.4
    linear .4 align(.5, .5)

transform walk:
    align (.5, 1.0)
    linear 2.0 align(.5, .5)
    
transform dodge:
    zoom 2.0
    align (.5, .5)
    linear 0.2 align(.7, .7)
    linear 0.2 align(.9, .5)

image showT:
    additive(1.0)
    "nameless_nom.png"
    linear 3.0 additive(0.0)

image showT2:
    alpha(0.0)
    "nameless_nom.png"
    linear 3.0 alpha(1.0)

image bg_roomblack = im.MatrixColor("bg_roomc.jpg", im.matrix.saturation(0.0))
image bg_clubblack = im.MatrixColor("bg_club.jpg", im.matrix.invert())
image continued2 = im.MatrixColor("continued.png", im.matrix.invert())
image bg_club_morningB = im.MatrixColor("bg_club_morning.jpg", im.matrix.saturation(0.0))

define bg_clubblack = im.MatrixColor("bg_club.jpg", im.matrix.saturation(0.0))
image seng_nomi = im.MatrixColor("seng_nom.png", im.matrix.invert())
image bg_clubred =  im.MatrixColor(bg_clubblack, im.matrix.colorize("#DF0101", "#1C1C1C"))
image seng_nomii = im.MatrixColor("seng_nom.png", im.matrix.colorize("#DF0101", "#1C1C1C"))
image seng_supred = im.MatrixColor("seng_ang.png", im.matrix.colorize("#DF0101", "#1C1C1C"))
image bg_nightschoolred = im.MatrixColor("bg_ground.jpg", im.matrix.colorize("#DF0101", "#1C1C1C"))
image nameless_gray = im.MatrixColor("nameless_nom.png", im.matrix.saturation(0.0))
image bg_namelessG = im.MatrixColor("bg_nameless.jpg", im.matrix.saturation(0.0))
image seng_mamiru = im.Crop("seng_nom.png", (0, 254, 250, 307))
define nameless_mamiru = im.Crop("nameless_nom.png", (0, 254, 320, 307))
image nameless_mamiru = im.MatrixColor(nameless_mamiru, im.matrix.saturation(0.0))
define seng_mamiru = im.Crop("seng_nom.png", (0, 254, 250, 307))
define leftbad = Position(xalign=.1, yalign=.7)#1C1C1C
image seng_mamirui = im.MatrixColor(seng_mamiru, im.matrix.colorize("#1C1C1C", "#DF0101"))
image seng_mamiruii = im.MatrixColor(seng_mamiru, im.matrix.invert())
image mon_rine = im.MatrixColor("rine_ang.png", im.matrix.colorize("#DF0101", "#000000"))
image bg_red = im.MatrixColor("bg_black.png", im.matrix.colorize("#f00000", "#DF0101"))
image guard_nomred = im.MatrixColor('guard_nom.png', im.matrix.colorize("#DF0101", "#000000"))
image side another nom:
    "seng_another"


image cg_blood1 = "cg_blood.png"
image cg_blood2 = "cg_blood.png"
image cg_blood3 = "cg_blood.png"
image cg_blood4 = "cg_blood.png"
image cg_blood5 = "cg_blood.png"
image cg_blood6 = "cg_blood.png"
image cg_blood7 = "cg_blood.png"
image cg_blood8 = "cg_blood.png"
image cg_blood9 = "cg_blood.png"
image cg_blood10 = "cg_blood.png"
image cg_blood11 = "cg_blood.png"
image cg_blood12 = "cg_blood.png"
image cg_blood14 = "cg_blood.png"
image cg_blood15= "cg_blood.png"
image cg_blood16 = "cg_blood.png"
image cg_blood17 = "cg_blood.png"
image cg_blood18 = "cg_blood.png"
image cg_blood19 = "cg_blood.png"
image cg_blood20 = "cg_blood.png"
image cg_blood13 = "cg_blood.png"

#image char_nom = "rine_nom.png"
#image char_ang = "rine_ang.png"
#image char_sad = "rine_sad.png"


init python:
    #style.default.line_leading = 12

    style.my_style=Style(style.default)
    #style.say_thought.line_leading=10
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 10
    style.ruby_style.yoffset=-17
    style.default.ruby_style=style.ruby_style

define moving = MoveTransition(0.4, enter=None, leave=None)

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

transform explosion:
    zoom(1.5)
    align(.5, .5)
    linear .1 align(.5, .7)
    linear .1 align(.5, .5)
    linear .1 align(.5, .3)
    linear .1 align(.5, .5)
    repeat(2.0)

transform sizeing:
    align(.5, .5)
    linear 6.0 zoom 80.0

transform sizeing1:
    xalign .5 yalign .5
    linear 10.0 zoom 80.0
    
init python:
    temp=None
    renpy.music.register_channel("first", "sfx", False)
    renpy.music.register_channel("second", "sfx", False)
    rine = Character("리네", color="#DF0101", image="rine")
    main = Character("[temp]", color="#6E6E6E")
    seng = Character("성", color="#91ff6d", image="seng")
    teacher=Character("안톤", color="#E0F8F7", image="read")
    anotherseng=Character("???", who_color="#3b0b30", what_color="#3b0b30", image="another")
    strange = Character("의문의 목소리", who_color="#0404B4")
    prin = Character("교장", color="#660099", image="prin")
    seng1 = Character("성?", what_color="#DF0101", who_color="#DF0101")
    guard = Character("이스프킨", what_color="#FC9B9B", who_color="#806060")
    factory = Character("안슈아", color="#868A08")
    anothervoice = Character("Ψ", who_color="#000069", what_color="#C65FF9")
    nameless = Character("□□□□", who_color="#3300FF", what_color="#FF0000")
    er = Character("에르", who_color="#088A68", what_color="#FF0000")
    style.window.left_padding=30
    a=0
    b=0

image white1d=im.MatrixColor("bg_white1.png", im.matrix.invert())

screen muzlet(temp="tete"):
    text "{size=40}{color=#FFFFFF}[temp]{/color}{/size}" align(.5, .5)

label psycopuzzle:
    scene bg_white1 with dissolve
    "옛날옛날에 한 작은 마을에 한 꼬마 아이가 살았습니다."
    "그런데..."
    scene white1d with vpunch
    play sound "blooding.mp3"
    show cg_gear at Position(xpos=200, ypos=300) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_gear1 at Position(xalign=.5, yalign=.5) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_gear2 at Position(xpos=798, ypos=300) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_gear3 at Position(xpos=300, ypos=400) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_gear4 at Position(xpos=900, ypos=200) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_gear5 at Position(xpos=1000, ypos=600) with vpunch
    $renpy.pause(2.0)
    play sound "blooding.mp3"
    show cg_red at sizeing with vpunch
    $renpy.pause(10.0)
    "모두모두 사이좋게 죽어버렸답니다."
    "끝"
    centered "얘. {w=.5}이렇게 아무 것도 알려주지 않고 끝나버리는 이야기는 어떻다고 생각해?"
    extend "\n아름답지 않니?{p=.5}응? 그렇지?{w=.5}이것도 마찬가지이지 않을까? {w=.5}이대로 끝난다면 최고지 않을까? {w=.5}정말 멋지겠는걸."
    extend "\n자, 어서. {w=.5}어서, {w=.5}어서, {w=.5}어서, {w=.5}어서, {w=.5}어서, {w=.5}어서, 눌러."
    extend "\n{w=.5}....{w=.5}....{w=.5}....{w=.5}....{w=.5}....{w=.5}....{w=.5}....{w=.5}...."
    extend "\n뭐, 처음부터 상관 없었어."
    extend "\n네가 뭘 어떻게 생각하던지 말이야."
    extend "\n{color=#000000}안녕. 이건 끝이야, 여기서.{/color}"
    call temp from _call_temp_1
    $ persistent.destroy = destroy
    $ persistent.equal = equal
    $ persistent.name = temp
    $ persistent.ok = True
    $renpy.quit()
    return

define right = Position(xalign=1.0, yalign=1.0)
define left = Position(xalign=.1, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define center1 = Position(xalign=.5, yalign=.5)
define center2 = Position(xalign=.5, yalign=.0)


define nvlnarr=Character(None, kind=nvl)
#kkkkkkkkkk
screen itai:
    hbox:
        text "{color=#DF0101}아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파{/color}"

screen aaaaa:
    hbox:
        text "{color=#DF0101}아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아{/color}"
    

init python:
    def deleteSave():
        saveList = renpy.list_slots()
        for i in saveList:
            renpy.unlink_save(i)