﻿################################################################################
## Initialization
################################################################################

init offset = -1
#소지 아이템######################
init python:
    firstitem="시간의 궤검-포스키아"
    seconditem="눈의 각인"
    thirditem=None
    forthitem="윤무/시작과 끝의 예속"

#의문점(가칭)#####################
init python:
    firstcurious=None
    secondcurious=None
    thirdcurious=None

#screen menutext:

transform downing:
    align(0.01, -0.3)
    linear 0.5 align (0.01, 0.002)

transform alpha1(sec=.5):
    alpha(0.0)
    pause(sec)
    linear(.5)  alpha(1.0)

transform alpha2(sec=.5):
    alpha(0.0)
    pause(.5)
    linear(sec) alpha(1.0)
transform quake:
    align(.5, .5)
    linear .1 ypos -10
    linear .1 ypos 0
    linear .1 ypos 10
    repeat(10.0)
transform lrquake:
    align(.5, .5)
    linear .1 xpos -10
    linear .1 xpos 0
    linear .1 xpos 10
    repeat(3.0)

transform alphamove():
    #pause(.2)
    linear (1.0) pos(renpy.random.randint(0, 1280), renpy.random.randint(0, 600))
    linear (1.0) pos(renpy.random.randint(0, 1280), renpy.random.randint(0, 600))
    linear (1.0) pos(renpy.random.randint(0, 1280), renpy.random.randint(0, 525))
    repeat(90000)

screen nonreal:
    modal True
    frame:
        align(.5, .5)
        vbox:
            text "{color=#000000}{size=80}데이터 말소됨{/size}{/color}" 
            textbutton "{size=50}{color=#000000}Y{/color}{/size}" action [Hide("nonreal", transition=dissolve), Return()] at center1     
screen curious:
            #group_big
    $f_ypos=renpy.random.randint(0, 720)
    $f_xpos=renpy.random.randint(0, 1280)
    $s_ypos=renpy.random.randint(0, 720)
    $s_xpos=renpy.random.randint(0, 1280)
    $t_ypos=renpy.random.randint(0, 720)
    $t_xpos=renpy.random.randint(0, 1280)
    $f1_ypos=renpy.random.randint(0, 720)
    $f1_xpos=renpy.random.randint(0, 1280)
    $f2_ypos=renpy.random.randint(0, 720)
    $f2_xpos=renpy.random.randint(0, 1280)
                
    #group_small 
    $fs_ypos=renpy.random.randint(0, 720)
    $fs_xpos=renpy.random.randint(0, 1280)
    $ss_ypos=renpy.random.randint(0, 720)
    $ss_xpos=renpy.random.randint(0, 1280)
    $ts_ypos=renpy.random.randint(0, 720)
    $ts_xpos=renpy.random.randint(0, 1280)
    $f1s_ypos=renpy.random.randint(0, 720)
    $f1s_xpos=renpy.random.randint(0, 1280)
    $f2s_ypos=renpy.random.randint(0, 720)
    $f2s_xpos=renpy.random.randint(0, 1280)
##############################################



#    text "[f_ypos]" xpos 100 ypos 100
    modal True

    tag menu
    use game_menu(_("의문점"), scroll=None):
        
        vbox:
            align(.3, .2)
            textbutton "{color=#FFFFFF}의문점들{/color}" at alpha1(sec=.5)
            textbutton "{color=#FFFFFF}[firstcurious]{/color}" at alpha1(sec=.7)
            textbutton "{color=#FFFFFF}[secondcurious]{/color}" at alpha1(sec=.9)
            textbutton "{color=#FFFFFF}[thirdcurious]{/color}" at alpha1(sec=1.1)


        add "mark_1.png" xpos f_xpos ypos f_ypos at alphamove
        add "mark_2.png" xpos s_xpos ypos s_ypos at alphamove
        add "mark_3.png" xpos t_xpos ypos t_ypos at alphamove
        add "mark_4.png" xpos f1_xpos ypos f1_ypos at alphamove
        add "mark_5.png" xpos f2_xpos ypos f2_ypos at alphamove
        #####################################################################################

        add "mark_6.png" xpos fs_xpos ypos fs_ypos at alphamove
        add "mark_7.png" xpos ss_xpos ypos ss_ypos at alphamove
        add "mark_8.png" xpos ts_xpos ypos ts_ypos at alphamove
        add "mark_9.png" xpos f1s_xpos ypos f1s_ypos at alphamove
        add "mark_10.png" ypos f2s_ypos at alphamove

        #vbox:
        #    align(.5, .35)
        #    textbutton "{color=#FFFFFF}소유물{/color}" at alpha1(sec=1.3)
        #    if firstitem == None:
        #        textbutton "None" at alpha1(sec=1.5)
        #    else:
        #        textbutton "[firstitem]" at alpha1(sec=1.5) action Show('firstitem', transition=dissolve) 
        #    if seconditem == None:
        #        textbutton "None" at alpha1(sec=1.7)
        #    else:
        #        textbutton "[seconditem]" at alpha1(sec=1.7) action Show('seconditem', transition=dissolve)
        #    if thirditem == None:
        #        textbutton "None" at alpha1(sec=1.9)
        #    else:
        #        textbutton "[thirditem]" at alpha1(sec=1.7) action Show('thirditem', transition=dissolve)

        # textbutton "[forthitem]" at alpha1(sec=2.1) action Show('forthitem', transition=dissolve)
    

screen firstitem:
    modal True
    if firstitem=="시간의 궤검-포스키아":
        frame:
            align (.5, .5)
            vbox:
                text "{color=#000000}한 이름 모르는 은인에게 선물받은 \'시간을 베어내는 검\'.\n무기로써 사용할 때는 검집에서 검을 뽑지 않는다.\n몇천의 시간을 존재하며 인과의 굴레를 벗어났기에\n검집에서 검을 뽑는 순간 시간에 외도의 균열이 발생\n하여 불가변이 아닌 시간을 되감는다.{/color}"
                textbutton "닫기" action Hide('firstitem') at center1

screen seconditem:
    modal True
    if seconditem=="눈의 각인": 
        frame:
            align (.5, .5)
            vbox:
                text "{color=#000000}교장이 학생들을 감시하기 위해 몸에 새긴 소형 천리안.\n그 어떤 시간에 어떤 형태이던 굴레 안에 존재하기만 한다면\n대상의 상태와 위치를 즉시 파악함과 동시에 특정 능력들을 봉인한다.{/color}"
                textbutton "닫기" action Hide('seconditem') at center1

screen thirditem:
    modal True
    if thirditem=="영혼이 담긴 병" and truething==False:
        frame:
            align(.5, .5)
            vbox:
                text "{color=#000000}분홍빛을 띄는 영혼이 담긴 투명한 유리병이다.{/color}"
                textbutton "닫기" action Hide('thirditem') at center1
    if thirditem=="영혼이 담긴 병." and truething==True:
        frame:
            align(.5, .5)
            vbox:
                text "{color=#000000}섬망{font=HigashiOmeGothic.ttf}(譫妄){/font}. 맺음 없는 이야기는 없고, 시작되지 않은 이야기 역시 없다.\n갈애의 눈물을 가진 유리잔의 나이트여, 편히 잠드시길.{/color}"
                textbutton "닫기" action Hide('thirditem') at center1

screen forthitem:
    modal True
    frame: 
        align(.5, .5)
        vbox:
            text "{color=#000000}광상{font=HigashiOmeGothic.ttf}(狂想){/font}. 그리고 그 끝.\n대지의 의지를 가졌던 강철의 폰이여, 편히 잠드소서{/color      }"    
            textbutton "닫기" action Hide('forthitem') at center1
#휴대폰###########################
screen phonebutton:
    textbutton "휴대전화" xalign .10 yalign .04 action[Hide('phonebutton'), Show('phone', transition=wipeup)] 
   # $renpy.transition("vpunch")

init python:
    r_ms=False
    s_ms=False

screen phone:
    modal True
    #$renpy.transition('vpunch')
    add "phone.png" xalign .8 yalign 1.0
    textbutton "닫기" xalign .96 yalign .04 action[Hide('phone'), Show('phonebutton', transition=wipedown)]
    vbox:
        align(.61, 0.46)
        spacing(20)
        if rine_dia==0:
            textbutton "리네"
        else:
            textbutton "리네" action Show('inrine')

        textbutton "성" action Show('inseng', transition=Dissolve(.2))
    
screen inrine:
    if r_ms==False:
        frame:
            align(.727, 0.5)
            vbox:
                text "{color=#000000}연락 불가능{/color}"
                textbutton "       Y" action Hide('inrine')





screen inseng:
    if s_ms==False:
        frame:
            align(.727, 0.5)
            vbox:
                text "{color=#000000}연락 불가능{/color}"
                textbutton "       Y" action Hide('inseng', transition=Dissolve(.2))
##################################

image daruma_kickhover = im.MatrixColor("daruma_kick.png", im.matrix.invert()) 

image daruma_kickimage:
    "daruma_kick.png"
    pause(0.07)
    "daruma_kickhover"
    pause(0.07)
    "daruma_kick.png"
    pause(0.07)
    "daruma_kickhover"
    pause(0.07)
    repeat(2.8)
#사이코 퍼즐
screen suprisedaruma:
    add "bg_black"
    modal True
    imagebutton idle "daruma_nomal" hover "daruma_nomalhover" action [Hide('suprisedaruma'), Show('suprisedaruma2')]

screen suprisedaruma2:
    add "daruma_kickimage"

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)


style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
         #   if persistent.ok and not persistent.trueR:
                #textbutton _("{size=30}Start{/size}") at alpha1(sec=.5) action [Show("nonreal", transition=dissolve)]
            textbutton _("{size=30}Start{/size}") at alpha1(sec=.2) action Start() 

        else:
            textbutton _("{size=30}History{/size}") at alpha1(sec=.4) action ShowMenu("history")

            textbutton _("{size=30}Save{/size}") at alpha1(sec=.6) action ShowMenu("save")

        textbutton _("{size=30}Load{/size}") at alpha1(sec=.8) action ShowMenu("load")

        textbutton _("{size=30}Preferences{/size}") at alpha1(sec=1.0) action ShowMenu("preferences")

        #textbutton ("Update") action updater.Update(url="https://nozomu466.000webhostapp.com/update.json")

        if _in_replay:

            textbutton _("{size=30}End Replay{/size}") at alpha1(sec=1.2) action EndReplay(confirm=True) 

        elif not main_menu:

            textbutton _("{size=30}Main Menu{/size}") at alpha1(sec=1.4) action MainMenu()
            textbutton "{size=30}Curious{/size}" action[Show('curious', transition=dissolve)] at alpha1(sec=1.6)

        textbutton _("{size=30}About{/size}") at alpha1(sec=1.8) action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("{size=30}Help{/size}") at alpha1(sec=2.0) action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("{size=30}Exit{/size}") at alpha1(sec=2.2) action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
   # show sound
    ## This ensures that any other menu screen is replaced
        #$renpy.music.play('foot.mp3', 'music')    
       # $renpy.music.queue('door.mp3', 'music')
       ## $renpy.music.queue('Mr.J tema.mp3', 'music', False)
    #$renpy.music.stop()
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation
    if gui.show_name:

        vbox:
            align(.77, .85)
            text "{font=SDMiSaeng.ttf}{size=72}{color=#FFFFFF}버{w=.5}드{w=.5}나{w=.5}무{w=.5} 꽃{w=.5} 만{w=.5}발{w=.5}할{w=.5} 그{w=.5}날{w=.5}까{w=.5}지{w=.5}{w=.5}...{/color}{/size}{/font}" at alpha1(sec=7.0)



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    color "#fff"
    yalign .995
    size 18
    kerning -1
    xoffset 290

style main_menu_version:
    variant "small"
    xoffset 365


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("버전정보"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("버젼 [config.version!t]\n")

            ## gui.about 의 내용은 보통 options.rpy에 있습니다.
            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임.\n\n[renpy.license!t]")

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 화면") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("측면 되감기")
                    textbutton _("비활성화") action Preference("rollback side", "disable")
                    textbutton _("화면 왼쪽 클릭") action Preference("rollback side", "left")
                    textbutton _("화면 오른쪽 클릭") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("넘기기")
                    textbutton _("읽지 않은 지문") action Preference("skip", "toggle")
                    textbutton _("선택지 이후") action Preference("after choices", "toggle")
                    textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

                ## "radio_pref" 나 "check_pref" 를 추가하여 그 외에도 환경설정
                ## 항목을 추가할 수 있습니다.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("배경음 음량")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("효과음 음량")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("음성 음량")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


#end language_picker


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

init python:
    a=0
    _history_list = [ ]
    _history = True
    message = None

define config.history_callbacks = _history_list



screen history():
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:
            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                if h.who is not None:
                    label h.who:
                        style "history_name"
                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]


                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                $message = h
                vbox:
                    text "[h.rollback_identifier]"
                    textbutton "[h.who]" style "history_name" action [SetVariable("message", h.rollback_identifier), ShowMenu("history_confirm")]
                    text h.what

        if not _history_list:
            label _("기억 정보 없음.")


define gui.history_allow_tags = set()

screen history_confirm:
    modal True
    frame:
        align(.5, .5)
        vbox:
            text "기억을 이 상태로 복원하시겠습니까?"
            hbox:
                xalign .5
                textbutton "Y" action[RollbackToIdentifier(message)]
                textbutton "N"


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    color gui.history_name_color

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")

    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("스크린샷 저장.")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}대사 읽어주기 기능{/a} 토글.")


screen mouse_help():

    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("휠 위로\n롤백 클릭")
        text _("이전 대사로 롤백.")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")


    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("스타트 버튼/가이드 버튼")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    if message == layout.QUIT:
        $message = "데이터 더듬기를 그만두시겠습니까?"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600




