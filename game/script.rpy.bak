#define build.google_play_key = ""

screen dest:
    hbox:
        text "{color=#ffffff}붕괴도{/color}"
        
        bar:
            style style.newBar
            xmaximum 300
            value destroy
            range 100 
        text "{color=#ffffff}     융화도{/color}"
        bar:
            xmaximum 300
            value equal
            range 100
image movie = Movie(play="noise.ogv", loops=2, delay=None)
init python:
    import os
    user=None
    location=None
  #  import getpass

image char_nom = "rine_nom.png"
image char_sad = "rine_sad.png"
image char_ang = "rine_ang.png"


label temp:
   # "dkdkdkk"
    $persistent.value_b=renpy.list_saved_games()
    $persistent.check=True
    #"dldlddlld"
    python:
        name=[]
        user = os.getenv('username')
        location="C:/Users/"+user+"/AppData\Roaming/RenPy/Willow-1523110610"
        for root, dirs, files in os.walk(location):
            for fname in files:
                renpy.unlink_save(fname.replace("-LT1.save", ""))
    #"[name]"4
    #"[b]"
    #"에에 [a]"
    return

init python:
    temp2=False
    f_ypos=None
    temp=None
    emotion="nom"
    USB=None
    trigger = True
    home = config.basedir.replace("\\", "/")
    import shutil
    count = 0
# 여기에서부터 게임이 시작합니다.

#######################################
##외부저장소 루트에 char.txt파일 넣으면 작동
#######################################


init:
    python:
        dl=None
        def FileRestore(filename):
            shutil.copy(""+filename, config.basedir)
            trigger = False               
        def check2():
            show_image=False
            dl = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            for i in drives:
                if os.path.isfile(i+"/char_nom.png" ) and os.path.isfile(i+"/char_ang.png") and os.path.isfile(i+"/char_sad.png"):
                  #  print("image found")
                    USB=i
                    show_image=True
                    break
            if show_image:
                #print("real text: " + USB + "/char_"+emotion + ".png")                
                try:
                    d = 1
                    FileRestore(USB + "/char_nom.png")
                    FileRestore(USB + "/char_ang.png")
                    FileRestore(USB + "/char_sad.png")                        
                    #renpy.hide("/char_"+emotion+".png")
                    #renpy.show("/char_"+emotion+".png", at_list=[Transform(pos=(100, 0))])
                except:
                    pass                    
        
        if trigger:
            config.periodic_callback=check2
label check:
    #"[USB]"
    $temp=persistent.name
    if not persistent.ok:
        return
    else:
       # if persistent.check!=True:
           # call temp from _call_temp
        call game3 from _call_game3
label chsetting:
    #show mon_rine 
    $preferences.text_cps=40
    scene bg_willow
    $temp=renpy.input("이름 입력")
    "이름은 [temp].{p=1.0}맞는가요?"
    menu: 
        "네":
            return
        "아니오":
            call chsetting from _call_chsetting

label check2:
    python:        
        for root, dirs, files in os.walk(location):
            for fname in files:
                time=os.stat(location+"/"+fname).st_atime
                for index in persistent.value_b:
                    if(index==time):
                        renpy.quit

label start:
    if os.path.isfile(home+"/char_nom.png"):
        image char_nom = home+"/char_nom.png"
        image char_sad = home+"/char_sad.png"
        image char_ang = home+"/char_ang.png"
    $renpy.music.stop(2.0)
    $renpy.music.play('Mr.J2_1.mp3', 'music')    
    $renpy.fix_rollback() 
    call check from _call_check       
    call chsetting from _call_chsetting_1
    #if persistent.USB!=None:
       #show seng_nom2 at Position(xalign=.0, yalign=.0)
    window show
    scene warning with dissolve
    $renpy.pause(5.0)
    nvlnarr "열심히 살아가야 하는 이유는 무엇인가.{p=1.0}하루하루 살아가는 삶 속에서 견디기 힘든 고난이 있다 하여도{p=1.0}우리는 나아가야만 하는가?"
    nvl clear
    window hide
    scene bg_black
    show screen curious_button
    play sound "alarm.mp3"
    $renpy.pause(2.0)
    play sound "alarm.mp3"
    $renpy.pause(2.0)
    play sound "alarm.mp3"
    "알람 소리."
    "꿈 없는 잠에서 깨어났다.{p=1.0}찌뿌둥한 몸을 뻗어 굳은 근육을 풀었다.{p=1.0}눈을 떴다."
    scene bg_room_night
    show seng_nom at right
    with irisout
    seng "잘 잤어?"
    main "뭐, 그럭저럭이지."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    $renpy.pause(2.0)
    play sound "doorclosed.mp3"
    scene bg_bathroom with dissolve
    "남은 잠기운을 지우기 위해 세수했다."
    play sound "washing.mp3"
    $renpy.pause(2.0)
    play sound "washing.mp3"
    $renpy.pause(2.0)
    play sound "doorclosed.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_room_night
    show seng_nom at right
    with dissolve
    seng "오늘도 먼저?"
    main "응."
    "나는 약을 삼켰다."
    seng "선생님한테는 내가 이야기할까?"
    main "부탁할게."
    "시작하는 기분이 나쁘지 않다.{p=1.0}오늘은 괜찮은 하루가 될 수 있을지도 모르겠다."
    play sound "doorclosed.mp3"
    $renpy.pause(2.0)
    hide seng_nom
    hide bg_room_night
    play sound "walk_slow.mp3"
    "내려왔다."
    $renpy.pause(2.0)
    scene bignightschool with dissolve
    play sound "walk.mp3"
    "달렸다."
    $renpy.pause(6.0)
    scene bignightschool
    play sound "walk.mp3"
    $renpy.pause(6.0)
    "숨이 턱까지 차오르며 폐가 찢어질 듯 아팠다.{p=1.0}무시하고 달렸다."
    scene bignightschool
    play sound "walk.mp3"
    $renpy.pause(6.0)
    stop sound
    hide bignightschool with fade
    window show
    nvlnarr "우리들은 태어나 앞으로 전진한다.{p=1.0}학습하고, 말하고, 만나고, 헤어지고, 상처입고, 상처주며 끝을 향한다."
    nvlnarr "인생이라 불리는 밤잠 속 꿈이 죽음이라는 아침을 맞이해 안개처럼 흩어져 사라질 때까지.{p=1.0}우리들은 묵묵히 나아간다."
    nvl clear
    window hide
    play sound "shower.mp3"
    scene bg_bathroom with fade
    "뜨거운 물이 나의 몸을 기분좋게 데워 주었다.{p=1.0}땀이 씻겨 나가고 비누의 향기가 몸을 덮었다."
    seng "아직도 씻는 중이야?"
    main "어? 응. 금방 나갈게."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "doorclosed.mp3"
    "잠깐의 안식을 끝내고 밖으로 나왔다."
    scene bg_room_night
    show seng_nom at right 
    with fade
    $renpy.pause(2.0)
    scene bg_room_night at search
    "방 안을 탐색했다."
    $renpy.pause(3.5)
    show seng_nom at right 
    seng "찾는 게 이거지?"
    "나에게 약을 건네는 성."
    main "아, 고마워"
    "그것을 물 없이 삼켰다."
    scene bg_black with wipeleft
    "기숙학원의 하루는 일찍 시작된다.{p=1.0}사감 선생님께 인사하고 연구실에 도착.{p=1.0}불을 켰다."
    scene bg_club with wiperight
    "20분 후면 아침 점호가 시작된다.{p=1.0}어제 정리하다 말았던 연구 레포트를 갈무리하고 조사 내용을 확인하기 시작했다."
    $renpy.pause(5.0)
    play sound "bell_nomal.mp3"
    main "아."
    $renpy.pause(2.0)
    "종이 쳤다."
    "자리에서 일어나 운동장으로."
    scene bg_black with fade
    window show
    nvlnarr "그래요. 저에게도 소중한, 상처 입힐 수 없는 사람이 있었던 시절이 있었어요.{p=1.0}짧고 빠르게 흘러간, 제가 행복했었다 착각한 시간들이 있었어요."
    nvlnarr "이봐요 당신.{p=1.0}당신이 지금 서 있는 곳은 환상의 한 가운데인가요? 아니면 진실 속인가요?"
    nvl clear
    window hide
    scene bg_classroom with wipeleft  
    "일과의 지루한 수업들.{p=1.0}선생님의 나른한 목소리가 수면과 비수면의 경계에 있는 나를 수면 속으로 끌어들이려 하고 있다."
    "당분간은 착한 아이 코스프레를 이어가야 하는데..."
    main "으음..."
    "미리 책상 위에 놓아 두었던 초콜릿을 입 안에 넣었다.{p=1.0}당이 공급되며 순간적으로 잠이 달아났다.{p=1.0}효과는 얼마 가지 않겠지만 이 시간이 내가 오늘 듣는 마지막 의무교과이다."
    "이것만 끝난다면 연구실로 갈 수 있다."
    play sound "pen.mp3"
    $renpy.pause(2.0)
    play sound "bell_nomal.mp3"
    "선생" "오늘은 여기까지 수업하겠습니다.{p=1.0}학생분들은 교실에서 나가셔도 좋습니다."
    $renpy.pause(2.0)
    play sound "people.mp3"
    "시끄럽다."
    main "시끄러운건... 질색인데 말이지..."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    show seng_nom at right with dissolve
    "어디선가 성이 나타나 나의 어깨를 살짝 잡았다."
    seng "연구실로 가자.{p=1.0}여기 있어 봤자 기분만 더 나빠질거야."
    main "응. 그러자."
    play sound "walk_slow.mp3"
    scene bg_middle
    show seng_nom
    with dissolve
    "햇빛이 짜증날 정도로 얼굴을 따갑게 쑤셨다.{p=1.0}성은 아무 말도 하지 않고 옆에서 따라오고 있다."
    seng "날씨 좋네."
    main "...글쎄."
    play sound "walk_slow.mp3"
    "산자락의 겨울은 언제나 우중충하고 춥다.{p=1.0}이런 밝은 날은 드문데, 왜 짜증만 나는 것일까.{p=1.0}그런 생각을 하며 묵묵히 걸었다."
    $renpy.pause(2.0)
    scene bg_stair
    show seng_nom at right
    with dissolve
    play sound "walk_slow.mp3"
    "누군가 계단을 내려오는 소리가 난다."
    $renpy.pause(2.0)
    show rine_nom at center with dissolve
    "만나고 싶지 않은 사람의 얼굴이다."
    rine "[main]? 성?"
    "...이리로 오지 말았어야 했다."
    seng "[main]. 어서 가자."
    rine "잠깐! 할 이야기가 있어!"
    seng "미안해. 오늘은 좀 그래...{p=1.0}나중에 이야기하자."
    hide rine_nom
    show rine_ang at center
    rine "거짓말."
    main "..."
    seng "...너. 약속을 깰 생각이야?"
    rine "물론 그럴 생각은 없어.{p=1.0}하지만 너희. 그날 무슨 일이 있었는지 나한테 똑바로 설명해 줘."
    seng "리네. 제발... 오늘은 안 돼..."
    rine "밖에서 무슨 일이 벌어지고 있지?{p=1.0}나는 왜 이 안에 갇혀 살아야 하지?{p=1.0}아니, 애당초 이 학교는 무슨 목적으로 만들어졌지?"
    main "말할 수 없어."
    seng "[main]!"
    main "가만히 있어, 성."
    main "더 이상 내 기분을 상하게 하지 말아줘." 
    rine "배신자."
    "나는 주먹을 뻗었다."
    play sound "jab.mp3"
    $renpy.pause(2.0)
    main "경고했어. 듣지 않은 건 너고."
    rine "........"
    main "제발. 피차 피곤해 질만한 일은 하지 말자고."
    hide rine_ang
    show rine_nom at center
    rine "오늘은 여기까지.{p=1.0}하지만 다음에 만나면 똑바로 답해줘.{p=1.0}내가 언제까지 여기서 이렇게 가만히 있을 거라고 생각해?"
    hide rine_nom
    play sound "walk.mp3" 
    seng "[main], 괜찮아?"
    main "안 괜찮아."
    "가슴이 당긴다."
    main "성. 미안... 아무래도 올 것 같아."
    seng "여기서? 아, 이런...{p=1.0}곤란한데..."
    "뜨겁다.{p=1.0}몸이 불타는 것 같다."
    play sound "jab.mp3" 
    scene bg_black with fade
    "어둡다.{p=1.0}머리가 띵하다."
    window hide
    play sound "scream.mp3"
    show screen suprisedaruma2
    $renpy.pause(.9)
    hide screen suprisedaruma2
    "놀라지 않았다.{p=1.0}흔히 일어나는 일 중 하나일 뿐이다."
    main "이제 그만하지 않을래? 나는 그만 일어나고 싶은데."
    strange "큰 착각을 하고 있군.{p=1.0}지금 이 몸의 주인은 네가 아니라 나일텐데?"
    "\'약을 먹었으니 괜찮겠지\'.{p=1.0}너무나 안일한 생각이었다.{p=1.0}조금 흥분한 것만으로도 그녀는 순식간에 나의 몸을 빼앗았다."
    main "너와 싸우고 싶지 않아.{p=1.0}비켜줘."
    strange "몸을 되찾고 싶다면, 날 힘으로 저지하면 되잖아?{p=1.0}네겐 충분히 그럴 힘도 있고."
    main "말했잖아.{p=1.0}싸우고 싶지 않아."
    strange "...지금까지 수십번이나 해 온 일이잖아." 
    main "부탁이야..."
    strange "마음에는 안들지만... 뭐, 한 번 정도는 괜찮겠지."
    scene bg_black at earthquake
    $renpy.pause(2.0)
    "시야가 빠르게 점멸한다."
    window hide
    scene bg_black at earthquake
    $renpy.pause(2.0)
    scene bg_black with Fade(1.0, 1.0, 0.5, color="#FFFFFF")
    window show 
    nvlnarr "나는 지켜야 할 의무에서 도망쳐, 지켜야 할 사람을과, 지켜야 할 곳을 지키지 못했다.{p=1.0}내가 살아가야 할 이유는 모두 불타 사라졌다.{p=1.0}그러한데, 나는 어찌하여 아직 죽지 않고 살아있는가."
    nvl clear
    window hide
    scene bg_club
    show seng_nom at right
    with fade
    seng "아, [main]. 괜찮아?"
    main "...조금 불쾌한 것 말고는 전부 괜찮아.{p=1.0}네가 날 옮긴거야?"
    seng "응. 넌 가벼우니까."
    "왜소한 체구가 이럴 땐 좋군.{p=1.0}나는 자리에서 일어났다.{p=1.0}연구를 마저 해야한다."
    seng "아, 저번부터 네가 계속하고 있던 연구 있잖아."
    main "응."
    seng "그건 이렇게 하면 풀 수 있지 않을까?"
    play sound "pen.mp3"
    "복잡한 수식을 적는 그녀."
    $renpy.pause(2.0)
    main "뒤집자고? 두 성질을?"
    seng "응. P속성 원소는 전기 충격만 줘도 주변 원소와 결함해서 반전하잖아.{p=1.0}그걸 역이용 해서 연쇄 붕괴를 해결하면 간단하잖아."
    main "......."
    play sound "pen.mp3"
    "계산했다."
    $renpy.pause(2.0)    
    main "바보 같아."
    seng "...?{p=1.0}뭐가?"
    main "P 원소의 반전을 왜 아예 배제하고 있었던 거지... 나는..."
    seng "어떨 것 같아?"
    main "어쩌고 자시고도 없어.{p=1.0}가장 간결하고 명쾌한 답인걸."
    "나는 보고서의 결론 부분을 수정했다."
    main "이때 P속성 원소의 흡착성에 의해 주변 원소들이 흡착되며 이것에 전기충격을 주는 것으로 연쇄 붕괴를 해결할 수 있다."
    hide seng_nom
    show seng_smile at right
    "우리는 웃었다."
    main "덕분에 난제를 하나 해결했네.{p=1.0}답례로 오늘 밥은 내가 살게."
    seng "고맙게 먹을게~"
    play sound "walk_slow.mp3"
    "갈무리한 레포트를 들고 교{rt}기{/rt}무{rt}무{/rt}실{rt}처{/rt}로 향했다."
    $renpy.pause(2.0)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_hallway
    show seng_nom at right with dissolve
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    "창문으로 운동장에서 뛰노는 1학년들이 보였다."
    seng "참혹하네."
    main "응... 그러게..."
    seng "이 밖에서 일어나고 있는 일을 저 아이들은 상상이나 하고 있을까?"
    main "절대 못하겠지."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wiperight
    $renpy.pause(5.0)
    scene bg_teacher
    show seng_nom at right
    with wipeleft
    main "선생님."
    show read_nom at Position(xalign=.5, yalign=1.0) with dissolve
    teacher "아, [main] 양. 성 양.{p=1.0}무슨 일이시죠?"
    main "완성했습니다."
    teacher "예?"
    seng "연구를 완성했습니다.{p=1.0}검산도 마쳤어요.{p=1.0}확인을 부탁드리겠습니다."
    "안톤은 떨리는 손으로 종이를 건네받았다."
    window show
    play sound "pen.mp3"
    $renpy.pause(2.0)
    play sound "pen.mp3"
    $renpy.pause(2.0)
    play sound "pen.mp3"
    $renpy.pause(2.0)
    teacher "........"
    seng "어떤...가요?"
    teacher "...완벽...해..."
    main "........"
    teacher "간결하고, 양산 가능하며, 이해하기 쉬워...{p=1.0}이건 바로 통과시키겠습니다."
    hide seng_nom
    show seng_smile at right
    seng "예!"
    play sound "pen.mp3"
    "안톤은 그 보고서에 서명했다."
    $renpy.pause(2.0)
    teacher "위에는 제가 올리겠습니다."
    main "용건은 이게 답니다.{p=1.0}저희는 이만 물러가겠습니다."
    teacher "네."
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_hallway 
    show seng_nom at right 
    with dissolve
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "bell_nomal.mp3"
    "적절한 타이밍에 종이 울렸다."
    $renpy.pause(2.0)
    main "아까 밥 사준다고 했지?{p=1.0}가자. 사줄게."
    hide seng_nom
    show seng_smile at right
    seng "응!"
    play sound "walk.mp3"
    hide seng_smile
    "달려나갔다."
    main "기다려. 같이 가야지."
    play sound "walk.mp3"
    $renpy.pause(2.0)
    window hide
    scene bg_black with wiperight
    $renpy.pause(5.0)
    scene bg_meal
    show seng_smile at right
    with wipeleft
    main "뭐 먹을건데?"
    seng "우동!"
    main "나도 그걸로 할까나."
    "나는 우동 두그릇을 주문하고 자리에 앉아 기다렸다."
    seng "뭔가 되게 옛날로 돌아간 것 같아."
    main "응?"
    seng "있었던 일들도 전부 거짓말 같고 말이야."
    main "그것들은 전부 실제로 일어났던 일이야.{p=1.0}기억을 부정하는 것 만큼 위험한 것 없어, 성."
    seng "그렇겠지 역시?"
    main "당연하지."
    play sound "alarm.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    "우동 두 그릇을 받아왔다."
    $renpy.pause(2.0)
    main "먹자."
    play sound "pasta.mp3"
    $renpy.pause(2.0)
    hide seng_smile
    show seng_nom at right
    seng "[main]."
    main "응."
    seng "우리랑 같이 들어오지 못한 사람들은 어떻게 됐을까?"
    main "...죽었겠지.{p=1.0}그런 지옥도에서 살아남을 수 있을거라고 생각되진 않아."
    seng "역시... 그럴까..."
    main "왜, 궁금해?"
    seng "조금..."
    "바깥의 동생을 생각하는 것일까."
    play sound "pasta.mp3"
    $renpy.pause(2.0)
    "부자연스러운 침묵이 우리 사이에 감돈다."
    play sound "pasta.mp3"
    $renpy.pause(2.0)
    scene bg_black with fade
    $renpy.pause(4.0)
    scene bg_meal with fade
    show seng_sad
    seng "밥 잘 먹었어."
    "그렇지 않다는 것을 내가 잘 알고 있다."
    main "........"
    "괜찮을까..."
    hide seng_sad
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    window show
    nvlnarr "\"명심해. 절대로, 절대로 나를 따라오지 마.{p=1.0}너는 이곳에 남아서 나를 대신해 모두를 지켜주렴.{p=1.0}알겠니?\""
    nvlnarr "아아, 주인님... 주인님...{p=1.0}당신의 최후를 저는 지키지 못하였습니다...{p=1.0}그대의 몸이 산산히 조각나 흩날릴 때도, 저는 그곳에 있지 못하였습니다..."
    nvl clear
    window hide
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_middle with dissolve
    $renpy.pause(2.0)
    scene bg_hallway with dissolve
    "식사를 끝마치고 연구실로 돌아왔다."
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_club with dissolve
    "아무도 없다.{p=1.0}...찾으로 가야 하려나...?"
    menu:
        "찾으러 간다":
            "걱정되서 안되겠다.{p=1.0}그녀가 있을만한 곳을 전부 뒤져보자."
            play sound "walk.mp3"
            $renpy.pause(2.0)
            scene bg_black with dissolve
            play sound "walk.mp3"
            $renpy.pause(2.0)
            play sound "walk.mp3"
            $renpy.pause(2.0)
            play sound "walk.mp3"
            $renpy.pause(2.0)
            "없다. 아무 곳에도 없다.{p=1.0}...설마...!"
            play sound "walk.mp3"
            "나는 달렸다. 전속력으로.{p=1.0}늦지 않기를 바라며 달렸다."
            $renpy.pause(2.0)
            scene bg_top
            show seng_sad at right
            with fade
            seng "......."
            main "성... 너..."
            seng "...[main]. 결국 날 찾았구나."
            main "멈춰."
            seng "아니, 못 멈춰."
            main "제발."
            seng "미안, [main]."
            "...늦었다."
            "성의 인상이 변한다."
            hide seng_sad
            show seng_another at right
            anotherseng "......."
            main "성... 너..."
            anotherseng "오랜만이야, [main]."
            main "...왜..."
            anotherseng "왜긴? 난 언제나 이 안에 있었어."
            main "갑자기 왜... 다시... 나타난거야..."
            anotherseng "어머, 섭섭한 소리 하지 말아.{p=1.0}날 부른건 성이었어."
            main "거짓말 하지 마.{p=1.0}성이 정신적으로 힘들어 하는 와중에 네가 몸을 빼앗은 거잖아."
            anotherseng "아니라니까."
            main "믿을 수 없어."
            anotherseng "뭐... 지금까지 내가 한 짓들이 있으니까, 믿어달라는 건 무리려나."
            main "...저번과 달리 그리 호락호락하게 당하진 않을테니까..."
            anotherseng "아, 굳이 싸울 준비 할 필요 없어.{p=1.0}싸울 생각 없거든."
            main "왜 온거야."
            anotherseng "성이 날 불렀다니까?"
            main "무엇을 하려는 거지?"
            anotherseng "사람을 찾으러 갈거야."
            main "성은 동생을 찾기 위해 널 불렀군."
            anotherseng "그래."
            main "정말로... 나갈 셈이야?"
            anotherseng "성이 원하는 일이야."
            main "......."
            anotherseng "더 이상 볼일 없으면  난 간다."
            main "기다려!"
            play sound "walk.mp3"
            hide seng_another
            $renpy.pause(2.0)
            "달려간다."
            "쫒아가 봤자 소용 없을 것이다.{p=1.0}나와 저{rt}다{/rt} {rt}른{/rt}녀석{rt}성{/rt}과의 실력차는 압도적이다.{p=1.0}이번에는 나를 죽이겠다는 살기가 없었지만, 쫒아간다면 싸우게 되겠지."
            "정면으로 싸우게 된다면... 죽을 것이다.{p=1.0}하지만 바{rt}종{/rt}깥{rt}지{/rt}의 일을 읽을 수 있는 내가 없다면 그녀 역시 살아돌아오진 못할 터."
            main "정말... 제멋대로라니까..."
            play sound "walk_slow.mp3"
            "기숙사로 돌아갔다."
            scene bg_black with wiperight
            $renpy.pause(5.0)
            play sound "doorclosed.mp3"
            $renpy.pause(2.0)
            scene bg_room with wipeleft
            "신발장 옆에 기대어 놓은 그{rt}궤{/rt}것{rt}검{/rt}을 들었다.{p=1.0}시간을 베어내는 검인 이것이 있다면 그녀를 되돌릴 수 있을 것이다."
            main "<나의 검은 {rt}스파다{/rt}모든것을 베{rt}디{/rt}어내고 {rt}디스트로{/rt}{rt}지오네{/rt} 시간을 거스른다>."
            play sound "sword.mp3"
            show cg_crash with Dissolve(2.0)
            $renpy.pause(1.0)
            play sound "timebreak.mp3"
            scene bg_roomblack with Fade(8.0, 0.0, 8.0, color="#fff")
            main "<돌아와 나의 시간과 겹쳐라, 성.>"
            play sound "explosion.mp3"
            scene bg_room with Dissolve(5.0)
            "시간이 바뀌었다."
            main "정말아지, 못할 짓만 시키네..."
            "몸이 차갑게 식었다.{p=1.0}빠른 속도로 아픔이 퍼쳐나갔다."
            "깊게 숨을 들이쉬고, 내쉬었다."
            main "젠장...{p=1.0}진정해... 한..."
            "......."
            "......."
            "...머리가 멍해진다."
            main "가만히... 있어..."
            strange "거절하겠어.{p=1.0}몸을 빼앗을 절호의 기회를 왜 그냥 날리겠어?"
            main "지금만은... 방해하지 말아줘..."
            strange "내가 왜 굳이 너의 사정을 봐 줘야 하지?"
            main "부탁이야... 지금은 안돼..."
            strange "저번에도 그런 식으로 말했잖아?"
            main "아직은... 안돼..."
            strange "배신자.{p=1.0}나를 버리고 다른 아이와 노닥거리다니."
            main "...어쩔 수 없어.{p=1.0}이렇게 되는 걸 원하지 않았더라면 애시당초 나와 그녀가 만나는 것을 방해했어야지."
            strange "........"
            "머리부터 발끝까지 스치는 고통."
            strange "네 몸을 빼앗고 싶어.{p=1.0}이제 그만하고 나를 받아들여.{p=1.0}지금 네가 가지고 있는 것과는 비교조차 되지 않을 힘을 선물해줄게."
            main "아니."
            strange "살아남은 모든 인간들을, 모든 재앙들을, 모든 망령들을 쓰러트릴 만한 큰 힘을 줄게."
            main "필요없어."
            strange "시간이 얼마 남지도 않았는데 폐쇠{rt}학{/rt}공{rt}교{/rt}간 안에서 무엇을 할 수 있겠어?{p=1.0}밖으로 나가는게 좋지 않을까?"
            main "...만약 나 혼자였다면 당연히 그렇게 했겠지.{p=1.0}하지만 그녀가 있는 이상은 아니야."
            strange "변했구나..."
            main "그래. 난 변했어.{p=1.0}네게 휘둘리기만 하는 꼬마는 사라졌다고."
            strange "........"
            "그녀가 잠잠해졌다."
            "시간을 잘라내어 그녀가 밖으로 나갔다는 사실을 지웠으니 그녀는 지금 연구실에 있을 것이다."
            main "가 볼까나."
            $destroy+=10            
        "찾으러 가지 않는다.":
            "어차피 기다리다 보면 돌아올 것이다.{p=1.0}더 이상 그녀는 나에게 보호 받아야 하는 어린아이가 아니다.{p=1.0}더군다나 언제까지 그녀의 옆에 붙어 있을 수수는 없는 노릇."
            $equal+=10
    show screen dest
    "*붕괴도에 대하여*"
    "붕괴도는 \[의문의 목소리\]와 [main]간의 몸에 대한 영향력을 의미합니다.{p=1.0}붕괴도의 값이 작으면 작을수록 [main]의 영향력이 높으며, 크면 클수록\[의문의 목소리\]의 영향력이 크다는 것을 의미합니다."
    "*융화도에 대하여*"
    "융화도는 \[의문의 목소리\]가 [main]의 인격에 얼마나 동화되었나를 의미합니다.{p=1.0}융화도가 가득 찬다면 \[의문의 목소리\]의 인격은 완전히 [main]의 인격에 동화되어 융합될 것입니다."
    scene bg_club with dissolve
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    show seng_nom at right with dissolve
    "성이 돌아왔다."
    seng "으으... 삭신이야..."
    main "성."
    seng "응?"
    main "나가고 싶니?"
    seng "어딜?"
    main "이 학교 바깥으로 말이야."
    seng "...분명 내가 구하지 못한 소중한 사람들이 \'바깥\'에 많이 있는 건 틀림없어.{p=1.0}하지만 내가 이곳에 이렇게 살아 있는 것은 그들이 자신들 스스로를 희생시켜 나를 빼내 주었기 때문이야."
    seng "그들의 희생을 의미 없는 것으로 만들 순 없어."
    main "음..."
    seng "나의 동생, 나의 어머니, 나의 친구... 그리고... 나의 아버지...{p=1.0}많은 사람이 나를 위해서..."
    main "그래서, 그들을 구할 수 있을지도 모르는 가능성을 포기하겠다고?"
    seng "...응. \'바깥\'에서 살아남을 확률이 너무 희박해. "
    main "\'그{rt}다른{/rt}쪽{rt} 성{/rt}\'의 힘을 빌릴 생각은 하지 않는거야?"
    seng "그 녀석의 힘을? 당연하지.{p=1.0}이 몸... 아직은 넘겨줄 수 없는걸." 
    main "그렇구나."
    "대화가 끊겼다."
    play sound "pen.mp3"
    $renpy.pause(2.0)
    play sound "alarm.mp3"
    "휴대전화가 울렸다."
    $renpy.pause(2.0)
    show prin with moveinbottom
    $renpy.pause(1.0)
    show ms_prin1 with dissolve
    "호출...인가."
    hide ms_prin1
    hide prin with moveoutbottom
    main "가자, 성."
    seng "응? 어디로?"
    main "교장실로. 가고 싶지 않지만 계약에 얽메여 이상 어쩔 수 없지."
    seng "그래, 가자."
    hide seng_nom
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    scene bg_black
    $renpy.pause(7.0)
    scene bg_prin 
    show prin_nom 
    show seng_nom at right
    with wipeleft
    prin "늦어!"
    main "무엇 때문에 부른신 거죠."
    prin "이제 아예 내 말을 무시하는군.{p=1.0}이래서 머리 검은 짐승은 들여놓는게 아니라고 했는데."
    main "미안하지만 전 흑발이 아니라 청발이라고요."
    prin "이젠 말대꾸까지.{p=1.0}재워주고 먹여주고 가르쳐준 은혜를 이렇게 갚는거냐."
    main "........"
    seng "용건이 뭐죠."
    prin ".......{p=1.0}밖으로 나가줘야겠어."
    main "계약 위반이로군요.{p=1.0}선생님께서 그렇게나 싫어하는."
    prin "그렇게 멀리까지 나갈 필요는 없어.{p=1.0}학교 앞 구공원까지만 나가도 충분하니까."
    main "내키지 않는군요.{p=1.0}성, 네 생각은 어때?"
    seng "애당초 약속을 지키지 않은 건 선생님 쪽이야.{p=1.0}우리가 들을 이유는 없어."
    prin "어린 녀석들이 쌍으로..."
    main "대체 왜 우리가 밖으로 나가야 하는지, 그 이유만이라도 들어보죠."
    prin "겔칸{rt}동{/rt}학{rt}쪽{/rt}원에서 사자를 보내왔어.{p=1.0}예정대로 진행된다면 3시간 후에 도착하겠지."
    main "그렇다면 더더욱이나 저희가 나갈 이유는 없지 않은가요."
    prin "다른 선생들은 다 일이 있어서 급한대로 연{rt}관{/rt}구{rt}리{/rt}회{rt}자{/rt} 중에서 최강인 너희들을 불렀어.{p=1.0}문제라도 있나?"
    "문제가 많다.{p=1.0}너무나도 많아서 지적하는 것조차 불가능 할 정도이다."
    seng "정말 가만히 듣고 있자니 말도 안되는 억지를 펼치고 계시네요.{p=1.0}저희 연구회 전원이 힘을 합친다고 해도 선생님 한 분에게 못 미친다고요."
    prin "너희들에겐 \'다른 인격\'도 있잖아?{p=1.0}여차하면 그네들의 힘을 빌리면 될 뿐이야."
    main "...그거.{p=1.0}진심으로 하는 말은 아니겠죠?"
    prin "진심인데?"
    "미친..."
    hide seng_nom
    show seng_ang at right
    seng "정신이 나갔군요."
    prin "응?"
    seng "우리더러 나가 죽으란 것과 무엇이 다르죠?"
    prin "똑같지.{p=1.0}당연한 것 아니야?{p=1.0}애당초 약속이 그랬을텐데?"
    seng "선을 넘고 계시잖아요!{p=1.0}분명히 교외는 대상외라고 했을텐데요!"
    prin "........."
    seng "분명 저희들이 입학할 때 교장선생님과 약속하긴 했어요.{p=1.0}하지만 선생님께서 약속의 내용을 왜곡하고, 어긴다면 저희 역시 약속을 파기할 겁니다."
    prin "젠장... 알았어. 알았다고.{p=1.0}구공원까지 갈 필요도 없어.{p=1.0}교문에서 대기해."
    "성이 무엇인가 말하려 했지만 내가 제지했다."
    main "그 정도라면 하겠습니다."
    seng "[main]!"
    main "내 말 들어줘, 성."
    seng "........."
    hide seng_ang
    show seng_nom at right
    seng "네가... 원한다면..."
    "담담히 이야기 하는 그녀."
    main "이야기는 끝난 것 같네요."
    prin "...혹시나 해서 말하는 거지만, 그 사람한테 진심을 보이면 안된다?"
    main "...걱정 마세요. 그 정도는 저도 알고 있습니다.{p=1.0}만약 제가 진심을 보였다면 그 쪽에서 먼저 그냥 넘길 수 없는 실수를 했겠죠."
    prin "그런 일이 없길 바래야겠군."
    seng "안녕히."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wiperight
    nvlnarr "영웅을 꿈꾸는 인간은 이상을 이루기 위하여 자신을 깎아 남을 조각한다.{p=1.0}자신이 무엇인가를 바꾸고 있다는 도취감에 취해 어느 틈엔가 스스로를 잃어버리고, 자신의 눈을 가려버린다.{p=1.0}다시 눈을 떴을 때. 자신이 이루었다 생각한 얄팍한 유토피아는 무너지고. 참혹한 진실이 스스로를 덮친다."
    nvlnarr "그리고... 그곳에는 파멸이 있을 뿐이다.{p=1.0}명심하라. 인간은 영웅이 될 수 없다.{p=1.0}당신은 영웅을 지망하고 있는가? 어서 빨리 꿈에서 깨기를. 당신이 되려하는 것은 영웅이 아니다."
    nvlnarr "그저 \'영웅\'이란 틀로 잘 포장된 스스로를 잃은 멍청이일 뿐이다.{p=1.0}진정한 영웅이 아닌, 그저 영웅 놀이일 뿐이다."
    nvl clear
    window hide
    "동쪽의 사신을 만나 그를 교내로 안내했다.{p=1.0}교장을 필두로 한 다른 선생들의 환영."
    scene bg_hallway 
    show seng_nom at right
    with wipeleft
    seng "지랄하네."
    main "...그러게..."
    seng "다른 학{rt}감{/rt}교{rt}옥{/rt}의 사람과의 교류도 중요하지만 왜 지금일까..."
    main "........"
    "나는 그녀를 흘끗 보았다."
    "바뀔 기미가 보인다."
    main "성."
    seng "...추해... 추하다고..."
    main "성!"
    seng "추한 것들... 전부 {color=#fff}사라져 버렸으면 좋을텐데...{/color}"
    main "성!"
    seng "......."
    "바뀌었다."
    "우리들, 관리자 안의 신편({font=HigashiOmeGothic.ttf}神片{/font})과도, 진짜 자신과도 다른. 제 3의 인격으로.{p=1.0}성 스스로의 보호본능이 만들어 낸 그녀의 \'증오\'와 \'슬픔\'과 \'폭력\'을 대변하는 인격으로."
    main "......."
    hide seng_nom
    play sound "walk_slow.mp3"
    main "어디가?"
    seng "울적해진... 기분을 풀러..."
    "\'사냥\'에 나서는 걸까.{p=1.0}막아보았자 나만 다칠 것이다.{p=1.0}하지만 막지 않을 순 없다."
    main "어딜 가려고. \'사냥\'하러 갈거야?"
    seng "...응..."
    main "가지 마.{p=1.0}아니, 가면 안 돼."
    seng "비켜 [main].{p=1.0}너까지 증오하고 싶진 않아."
    main "성이 말했어.{p=1.0}괜히 위험을 무릅쓰고 교외로 나갔다가 죽어서 자신을 보내준 가족들의 희생을 쓸모 없는 것으로 만들고 싶지 않다고."
    seng "너도 알잖아. 교문을 넘는 것 정도로 바로 죽지는 않아.{p=1.0}오랜시간 머문다면 역시 위험하겠지만 고작 30분 정도 가지고 죽거나 하진 않아."
    main "바깥의 환경에 대해 이야기 하는 게 아니라는 것을 알고 있잖아."
    seng "너. 내가 학교 주변에 나오는 싸구려들과 붙어도 질거라고 생각해?"
    main "물론 그렇게는 생각하지 않아.{p=1.0}심지가 약한 성이라면 모르겠지만 너는 그렇지 않겠지."
    seng "그럼 왜 내 앞을 막는건데..."
    main "널 걱정하니까."
    seng "...정말이지 쓸모 없는 소리나 하고 있네."
    "그녀의 말이 강한 설득력을 띄기 시작했다."
    seng "나는 나갈거야.{p=1.0}그리고 죽지 않고 살아 돌아올거야.{p=1.0}당연히 이 몸의 주인은 내가 아니니까 진짜가 상처받지 않도록 주의 할 것이고."
    seng "그래도 방해할거라면 맘대로 해."
    "설득당했다."
    "이유를 알 수 없었다."
    "나도 모르게, \'그녀는 밖으로 나가도 된다\'라 납득했다."
    "그녀는 떠났다."
    main "...괜찮...겠지? 적당히 한 두명을 죽이고 나면 진정할...거야..."
    "연구실로 몸을 옮겼다."
    play sound "walk_slow.mp3"
    scene bg_black with wipeleft
    $renpy.pause(5.0)
    scene bg_club with wiperight
    "책꽂이에 꽂힌 책 중 한 권을 뽑아들었다."
    play sound "book.mp3"
    $renpy.pause(2.0)
    nvlnarr "\"어디로 가야 할지 모르겠을 때, 마치 길을 잃어버린 것만 같을 때는 하늘을 보렴. 하늘에 반짝이는 별들이 우리를 올바른 길로 인도해줄거야.\""
    "그녀가 좋아하는 그림책이다.{p=1.0}처음 만났을 때부터 들고 있었던 책."
    play sound "book.mp3"
    $renpy.pause(2.0)
    nvl clear
    window hide
    play sound "walk_slow.mp3"
    "발걸음.{p=1.0}이곳으로 올 사람은 한 명 뿐이다."
    seng "[main]"
    main "........"
    seng "나... 또 저질러 버렸어..."
    main "...괜찮아."
    seng "샤워장으로... 가서... 씻을게..."
    main "응."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    "그녀는 샤워장으로 간 듯 했다."
    main "......."
    play sound "book.mp3"
    $renpy.pause(2.0)
    play sound "book.mp3"
    scene bg_black with fade
    "성을 기다리며 책들을 읽었다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "knock.mp3"
    $renpy.pause(2.0)
    seng "들어갈게."
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_club
    show seng_nom at right 
    with dissolve
    "교복은 만약을 대비하 가지고 있던 것으로 갈아입어 티가 안났지만 분명 비누로 씻었을 텐데도 아주 미약한 피 냄새가 났다."
    main "괜찮아 보이네."
    seng "조금...은..."
    "아까전보다 안정되어 보인다."
    main "수고했어."
    seng "...응..."
    main "피곤하지? 조금 쉬어."
    seng "고마워..."
    "그녀는 의자를 여러개 붙여 만든 간이 침대에 몸을 뉘였다."
    hide seng_nom
    play sound "beep.mp3"
    $renpy.pause(2.0)
    show prin 
    show ms_prin1
    with moveinbottom
    $renpy.pause(1.0)
    show ms_prin2 with dissolve
    "......."
    "성을 바라봤다."
    "곤히 자고 있는 그녀를 이런 귀찮은 일에 휘말리게 할 순 없다."
    hide ms_prin1
    hide ms_prin2
    hide prin 
    with moveoutbottom
    "리네는... 역시... \'본관\'이려나..."
    "그리로 가고 싶지 않다.{p=1.0}만나고 싶지 않은 사람들이 그곳에 있다.{p=1.0}하지만 교장이 명령한다면 어쩔 수 없겠지."
    "가방 속에 약이 들어가있다는 것을 확실히 확인하고 시계와 나이프 역시 챙겼다.{p=1.0}준비 완료. 연구실에서 나왔다."
    play sound "sliding.mp3"
    $renpy.fix_rollback()        
    $renpy.pause(2.0)
    scene bg_hallway with dissolve
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_middle with dissolve
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_stair with dissolve
    "숨이 막혀온다.{p=1.0}무시하고 계단을 올랐다."
    play sound "walk_slow.mp3"
    scene bg_hallway with dissolve
    "시선이... 따갑다.{p=1.0}역시나 무시하고 목표로 했던 사람을 찾기 시작했다."
    show rine_nom at right with dissolve
    main "리네."
    rine "[main]? 갑자기 왜?{p=1.0}아니, 그것보다 네가 왜 여기에 있어?"
    main "할 이야기가 있어.{p=1.0}따라와 줄 수 있어?"
    rine "...딱히 상관 없어."
    play sound "walk_slow.mp3"
    scene bg_stair 
    show rine_nom at right
    with dissolve
    scene bg_inschool 
    show rine_nom at right
    with dissolve
    rine "대체 용건이 뭔데?"
    main "무슨 일이 있었는지 알려줄게."
    rine "뭐?"
    main "알려줄게.{p=1.0}이 학교가 뭘 하는 곳인지.{p=1.0}왜 네가 이곳에 갇혀 있어야 하는지."
    rine "좋아.{p=1.0}그럼 내 의문에 대답해 줘."
    main "어디부터 시작하면 좋을까..."
    $renpy.fix_rollback()        
    call rinedia from _call_rinedia 
label star2:    
    show screen phonebutton
    $renpy.fix_rollback()        
    scene bg_black with wiperight
    play sound "walk_slow.mp3"
    $renpy.pause(5.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    play sound "sliding.mp3"
    $renpy.pause(2.0)
    scene bg_club with wipeleft
    "성은 여전히 잠들어 있다."
    seng "......."
    main "곤히도 자네..."
    seng "[main]."
    "미소를 띄고 있는 그녀.{p=1.0}잠꼬대를 하는 것일까."
    seng "너는 무슨 생각을 하고 있니?"
    main "음?"
    seng "너{rt}{size=15}{b}.{/b}{/size}{/rt}는{rt}{size=15}{b}.{/b}{/size}{/rt} 나를 어디에 이{rt}{size=15}{b}.{/b}{/size}{/rt}용{rt}{size=15}{b}.{/b}{/size}{/rt}하려는 거야?"
    "잠꼬대가 아니다.{p=1.0}이건..."
    seng "힘들어 하는 나를 내버려두고 혼자 어딜 갔다 온 거지?"
    "그 사이에 또 바뀐건가..."
    seng "아파하고, 힘들어하는 유일한 친구를 버리고 넌 어딜 갔다 온 거지?"
    main "리네를 만나고 왔어."
    seng "리네를?{p=1.0}그날 싸우고 말 한 번 섞기를 싫어했던 리네를 네가 만나러 갔다 왔단 말이야?"
    main "응."
    seng "어쨰서지?"
    main "교장이 시켜서..."
    seng "정말일까?{p=1.0}나와 거리를 두기 위해서 내가 정말로 싫어하는 그녀와 손을 잡으려 하는 마음이 전혀 없었다고 할 수 있을까?"
    main "그런 억지를..."
    seng "억지? 억지라고?{p=1.0}과연 그렇다고 단언할 수 있어?"
    main "다... 당연하지!{p=1.0}물론 내가 리네와 화해하려고 한 것에는 내 죄책감도 있어.{p=1.0}하지만 그게 너와의 사이를 벌리는 것과는 상관 없잖아!"
    seng "...글쎄.{p=1.0}두고보지."
    main "......."
    "성의 표정이 편히 풀어졌다."
    "숨소리."
    "확실하게 자고 있다."
    "그녀의 병이 그녀가 더더욱 빨리 바닥으로 떨어지도록 종용하고 있다.{p=1.0}하지만 그런 일은 벌어지지 않을 것이다{p=1.0}내가 옆에 있으니까."
    "내가 그녀를 {color=#DF0101}지킬{/color}테니까."
    play sound "beep.mp3"
    $renpy.pause(2.0)
    show rine with moveinbottom
    $renpy.pause(1.0)
    show ms_rine1 with dissolve
    "리네..."
    show ms_main1 with dissolve
    $renpy.pause(1.0)
    hide ms_rine1
    hide ms_main1
    hide rine 
    with moveoutbottom
    "휴대전화를 집어넣었다."
    "자리에 앉아 아까전에 펼쳐 두었던 책들을 정리했다."
    main "........"
    "과거에도 이런 날이 하루 있었다.{p=1.0}리네. 메세지. 자고 있는 성. 정리..."
    main "그러고보니 꼭 2달인가..."
    "지난간 일에 대한 후회만큼 의미없는 일은 없으나 그날에 대한 후회는 여전히 내 마음속에 남아있다.{p=1.0}아무리 교장이 시켰다고는 해도 그날의 나는 선을 넘었다고 볼 수 밖에 없었다."
    "아픔. 배신. 그리고 눈물."
    "교장은 대체 무슨 생각을 가지고 그런 명령을 내렸을까.{p=1.0}그리고 또 무슨 생각을 가지고 그녀와 화해하라 한 것일까."
    "나는 그날의 일을 \'후회하며 되새겨야 할 일\'로써 받아들일 수 있었지만 성은 그러지 못했다.{p=1.0}유약한 그녀의 심상은 깨져 조각났다."
    "외상후 스{rt}P{/rt}트{rt}T{/rt}레{rt}S{/rt}스{rt}D{/rt} 장애.{p=3.0}그녀를 지금과 같은 모습으로 바꾸어 버린 것.{p=1.0}불안했던 그녀의 심지를 끊어버린 것."
    "나는 그녀의 아픔을 이해할 수 없다.{p=1.0}공감 역시 할 수 없다.{p=1.0}그러니 적어도... 나와 그녀가 연결되어 있는 동안에는"
    "어떤 수단을 써서도 그녀를 지켜야 한다.{p=1.0}선생들과 교장을 적대해야 한다 해도.{p=1.0}이 곳에서 떠나야 한다 해도."
    "{color=#DF0101}나는... 그녀를 지킬 것이다... 이번에는...{/color}"
    main "성..."
    "버석거리고 윤기 없는 그녀의 머리카락."
    main "{color=#DF0101}성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성성...{/color}"
    $destroy+=10
    scene bg_black with fade
    nvlnarr "검의 날이 향하는 곳은 상관없다.{p=1.0}그대가 악인인지 선인인지도 상관없다.{p=1.0}중요한 것은 그대의 가슴이 향하는 곳이 어디인지에 관한 것이다."
    nvlnarr "가슴이 음지를 향한다면 그대가 아무리 올곧은 일을 위히 휘두른다 하여도 그대의 검에는 그림자가 낄 것이다."  
    
    "........{p=1.0}시야가 어둡다.{p=1.0}그런가. 잠들어 버린 것인가.{p=5.0}눈을 뜨려했다."
    scene bg_clubblack with dissolve
    ".......{p=1.0}흑백의 단색.{p=1.0}뭐지...?" 
    show seng_nomi with dissolve
    seng1 "........"
    main "...?"
    "반전...?{p=1.0}그럴 리 없다. 아직 붕괴까지는 여유가 있으니까...{p=1.0}그렇다면 이건... 대체..."
    main "...성?"
    seng1 "......."
    main "왜 그래?"
    seng1 "아파."
    main "뭐?"
    
    $renpy.transition(vpunch)
    show screen itai
    scene bg_clubred
    show seng_nomii
    with vpunch
    window show 
    seng1 "아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아���아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파아파"
    $preferences.text_cps=40
    hide screen itai
    scene bg_black with dissolve
    play sound "mamiru.mp3"
    seng1 "아..."
    $renpy.pause(2.0)
    scene bg_clubblack
    show seng_mamiruii at center 
    with fade
    main "에...?"
    play sound "blooding.mp3"
    scene bg_clubred
    show seng_mamirui at center
    with Dissolve(6.0)
    $renpy.pause(6.0)
    seng1 "대체... 왜..."
    main "무...{w=3.0}무슨..."
    seng1 "왜... 나를... 가만히 놓아 두지 않는거야..."
    main "무슨 소리야!"
    seng1 "너... 왜...{w=3.0}날 못 괴롭혀서 안달인거야..."
    main "뭐?"
    seng1 "너도 알고 있잖아. 내가 \'리네\'의 \'리\'자도 싫어한다는 걸."
    $renpy.fix_rollback()        
    menu:
        "사죄":
            $renpy.fix_rollback()        
            "그녀가 \'리네\'를 싫어하게 만든 것은 '\교장\'이지만 지금은 사죄하는 수 밖엔 없겠지."
            main "잘못했어.{p=1.0}확실히 배려가 부족했단 건 인정할게."
            seng1 "배려? 무슨 배려.{p=1.0}지금 네가 하는 말이 무엇인지는 알고 말하는 거야?"
            main "당연하지.{p=1.0}나는 잘못했다고 말하고 있는거야."
            seng1 "잘못했다고 하면 끝일 것 같아?"
            main "물론 아니지.{p=1.0}하지만 말이야, 내가 리네를 만나고, 그녀와 화해한 이유는 너도 알고 있잖아?"
            seng1 "교장이 시켜서라고?{w=3.0} 거짓말일 가능성이 있는한 나는 믿지 못해."
            main "어쨌든 미안해.{p=1.0}너랑 한마디 상의도 없이 내 멋대로 행동해서.{p=1.0}네가 그런 것 싫어한다는 것을 알고 있었는데...{w=3.0}내가 너무 경솔했어."
            seng1 "...{w=3.0} ...{w=3.0} 정말... {w=3.0}이지... 넌 언제나 그랬어.{p=1.0}화를 내려고 해도 금방 사과하고... {w=3.0}오히려 내가 더 뻘줌하게 만들어 버리지..."
            "나는 고개를 한 번 으쓱했다."
            $equal+=4
        "설득":
            $renpy.fix_rollback()        
            main "성. 네가 \'리네\'를 혐오하도록 만든 사람은 \'교장\'이야.{w=3.0} 네 스스로의 의지가 아니었잖아."
            seng1 "그래서? {p=1.0}내가 \'리네\'를 싫어하는 감정이 진실이 아닌 \'남의 시{rt}페{/rt}선에 의{rt}르{/rt}해 만{rt}소{/rt}들어 {rt}나{/rt}진 것'\n이라고 말하고 싶은거야?"
            main "아니야!"
            seng1 "아니긴!{w=1.0} 맞잖아? 나는 잘못이 없어.{p=1.0}그럼에도 너는 \'교장의 명령\'이라는 미명하에 나를 배신하고 리네와 노닥거릴 속셈이잖아!"
            main "오해야! {w=1.0}아까도 말했잖아!"
            seng1 "나도 말했어! {w=1.0}티끌 하나만큼이라도 의심스러운 구석이 있다면 나는 믿지 않겠다고!"
            main "아니야! 아니라고!!!!!"
            $destroy+=10

    scene bg_club 
    show seng_nom 
    with vpunch
    seng "[main]... {w=1.0}괜찮아?"
    main "음..."
    "몸이 뜨겁다.{p=1.0}악몽...인가..."
    play sound "beep.mp3"
    $renpy.pause(2.0)
    seng "아까 전부터 계속 웅웅거리더라."
    "리네일 것이다."
    seng "저기... [main]..."
    main "응?"
    seng "네가 \'리네\'와 화해한 것은 교장이 시켰기 때문이지, 나를 버리기 위해서인 것이 아닌거지?"
    main "당연하지.{p=1.0}죄책감이 없다고 할 순 없겠지만, 너를 버리기 위해서는 아니라고 단언할 수 있어."
    seng "배신하면 {color=#DF0101}죽여{/color}버릴 테니까..."
    main "약속하겠어.{p=1.0}나는 절대로 너를 배신하지 않을게, 성."
    hide seng_nom
    show seng_smile
    seng "응!"
    play sound "knock.mp3"
    rine "성? [main]?"
    "리네의 목소리.{p=1.0}기다리다 지쳐서 여기까지 온 걸까."
    main "나는 잠깐 빠져 있을게."
    scene bg_black with wiperight
    play sound "door.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(3.0)
    "리네는 다혈질에다 감정을 쉬이 진정하지 못한다.{p=1.0}하지만 그렇기에 뒤끝이 없고 솔직하다.{p=1.0}친구관계에 있어어도 그것은 마찬가지."
    "자신을 계획적으로 따돌리고 상처입힌 성 역시 나처럼 한 번은 용서해 줄 것이다."
    scene bg_hallway
    show seng_smile 
    show rine_nom at right
    with dissolve
    "웃고 있다."
    "한 환{rt}꿈{/rt}상이 끝을 고했다."
    main "{size=4}한 숨 돌릴 수 있으려나...{/size}"
    "성, 리네" "응?"
    main "아무것도 아니야."
    nvl clear
    nvlnarr "\"나는... 행복을 누릴 권리따위...\"{p=1.0}\"없다고 말하고 싶으신거죠? 유감이지만 틀렸습니다.\"{p=1.0}\"나는... 나는 왕을 잡기 위해서...\""
    nvlnarr "\"모든 것을 버렸다고요? 거짓말 하지 마세요. 거짓말쟁이 씨.\"{p=1.0}\".......\""
    nvlnarr "\"스스로도 가슴 아플 정도로 잘 알고 있지 않나요? \'더 이상의 고통은 싫다\'.\'아픔 없는 곳으로 가고 싶다'\. 매일 밤 그렇게 되뇌었다는 것을.{w=1.0} 자, 모든 아픔과 고뇌와 슬픔들을 이곳에 버리고서 저와 함께 떠납시다.{w=1.0} 위로, 당신이 그토록 원하는 \'행복\'이 있는 곳으로.\""
    nvlnarr "\n\nEnd 1. 이기주의자의 이타적 행복"
    nvl clear
    window hide
    show continued with dissolve
    $renpy.pause(3.0)
    scene bg_black with dissolve
    $renpy.pause(5.0)
    show chapter1 with dissolve
    "나는 숨을 골랐다."
    play sound "bow.mp3"
    "???" "{font=Andante.ttf}До свидания.{/font}"
    $renpy.pause(4.0)
    hide chapter1 with dissolve
    "뇌를 꿰뚫었다."
    "자리에서 일어나 달렸다."
    play sound "walk.mp3"
    $renpy.pause(2.0)
    "{color=#088A68}???{/color}" "늬는 바보구나."
    "목소리.{w=1.0} 어디서 나는 거지?"
    "{color=#088A68}???{/color}" "체크 식스.{w=1.0} 저격수라면 당연히 지켜야 할 텐데?"
    "???" "!!!!!!"
    "위다.{p=1.0}재빨리 활에 화살을 먹여 하늘을 노렸다"
    "{color=#088A68}???{/color}" "늦었어."
    play sound "shotgun.mp3"
    $renpy.pause(1.5)        
    play sound "shotgun.mp3"
    $renpy.pause(1.5)        
    play sound "shotgun.mp3"
    $renpy.pause(1.5)        
    "???" "큭..."
    "{color=#088A68}???{/color}" "자, 체크{rt}외{/rt}메{rt}통{/rt}이{rt}수{/rt}트.{w=1.0} 어떻게 할래?"    
    "빠져나갈 길은... {w=1.0}없다."
    "???" "{font=Andante.ttf}Торн-дерево!{/font}"
    play sound "blooding.mp3"
    "나의 몸에서 살을 먹이로 삼아 가시가 돋아났다."
    $renpy.pause(2.0)
    "{color=#088A68}???{/color}" "어쩜 이렇게 막무가내인지. 늬는 죽더라도 혼자 죽지 않겠다는 것이야?"
    "대답하지 않았다. {w=1.0}아니, 할 수 없었다."
    play sound "mamiru.mp3"
    "가시 중 하나가 그녀의 목을 끊었다."
    $renpy.pause(6.0)
    "{color=#088A68}???{/color}" "그런데 말이야. {w=1.0}그거, 소용없어."
    "분명히 목이 잘렸을 터인 그녀가 멀쩡히 말하고 있다.{p=1.0}바닥에 떨어진 목을 주워 봉합."
    "{color=#088A68}???{/color}" "살려주고 싶은 마음이 싹 달아나 버렸어.{p=1.0}정말이지 \'안쪽\' 사람들은 이해할 수 없다니까."
    "머리에 닿는 차가운 금속.{p}펌프 액션 샷건이 내가 다른 이들에게 했던 것처럼 나의 뇌를 박살 낼 것이다."
    "???" "이봐, 에{rt}희{/rt}르{rt}망{/rt}. {w=1.0}하나만 물어봐도 될까?"
    "{color=#088A68}???{/color}" "?"
    "???" "마지막으로 봤을 때랑 상당히 다른 모습이네. {w=1.0}그 동안 무슨 일이 있었는지 짧게 설명해 주지 않을래?"
    "{color=#088A68}???{/color}" "싫어."
    "나는 어깨를 으쓱했다. {w=1.0}아니, 어께\'였던' 것을 으쓱했다."
    play sound "shotgun.mp3"
    $renpy.pause(1.5)        
    play sound "shotgun.mp3"
    $renpy.pause(1.5)        
    play sound "shotgun.mp3"
    $renpy.pause(1.5)
    scene bg_red with Dissolve(4.0)
    "???" "이런 최후도 나쁘진 않아... {w=1.0}어차피 지옥행 티켓은 확정된 것이나 마찬가진데, 이렇게 사랑했던 사람에게 살해당한다니."
    "그 말이 그녀에게 닿았는지 닿지 못하였을지 나는 알지 못하였다."
    "끝."
    $renpy.pause(4.0)
    scene bg_black
    play sound "phonebeep.mp3"
    $renpy.pause(2.0)
    ".......{w=1.0}꿈..."
    scene bg_room with Dissolve(5.0)
    "한낯.{p=1.0}아무 소리도 들리지 않는 고요한 방."
    "날 깨운 휴대폰을 바라봤다.{p=1.0}두 통의 부재중 전화. {w=1.0}성에게서 한 통. 리네에게서 한 통."
    play sound "phonering.mp3"
    $renpy.pause(8.0)
    rine "[main]? {w=1.0}[main]이야?{p=1.0}흥분한 리네의 목소리가 나의 귓청을 찢을 듯 했다."
    seng "리네, 진정해. {w=1.0}그리고 [main]. {w=1.0}너 지금 어디에 있어?"
    main "아무래도 지금까지 잠들어 있었던 모양이야."
    seng "주말이라서 알람을 해제해 놓았던 게 화근이군. {w=1.0}어서 운동장으로 와 줘."    
    main "왜? 리네도 그러고 대체 무슨 일이야?"
    seng "...설명하자면 복잡해.{p=1.0}밑에서 설명해 줄게."
    main "알았어."
    "활동복으로 환복하고 운동장으로 나섰다."
    scene bg_black with wipeleft
    play sound "walk.mp3"
    $renpy.pause(2.0)
    scene bg_shoes with wiperight
    rine "주여..."
    "알아들을 수 없는 말을 빠르게 중얼거리는 리네."
    show rine_ang at right with dissolve
    main "리네!"
    hide rine_ang
    show rine_nom at right
    rine "아... 다행이다..."
    main "무슨 일이야, 이게..."
    rine "객귀들이..."
    main "성은?"
    rine "이미 다른 애들이랑 막으러 갔어."
    play sound "walk.mp3"
    "나는 달렸다."
    $renpy.pause(2.0)
    scene bg_inschool at running with dissolve 
    "실낱같은 희망을 붙잡고 싶었다.{p=1.0}궤검으로 되돌리면 그만인 사태이기를 간절히 바랬다.{p=1.0}그리고 그 희망은 끊어져 바람에 휩쓸려 날아가버렸다."
    main "젠장... 이건..."
    "궤검으로는 되돌릴 수 없다.{p}이미 이 시간은 불가변으로 변했을 것이다."
    "바닥에 떨어진 SMG를 주웠다."
    main "싸우고 싶지 않은데..."
    show mon_rine with vpunch
    main "정말이지... 이 녀석들이 나타나는 시기는 너무 절묘하다니까."
    "쐈다."
    play sound "smg.mp3"
    $renpy.pause(.5)
    play sound "smg.mp3"
    $renpy.pause(.5)
    play sound "smg.mp3"
    $renpy.pause(.5)
    "{color=#FFF000}리네?{/color}" "그래봤자... 남는 것은 아픔 뿐..."
    main "닥쳐. {w=1.0}진짜도 아닌 모조품 주제에."
    "{color=#FFF000}리네?{/color}" "너는... 나의... 아픔... {w=1.0}나는... 너의... 아픔..."
    play sound "smg.mp3"
    $renpy.pause(2.0)
    hide mon_rine with dissolve 
    main "기분 나쁜 녀석들..."
    "{color=#088A68}???{/color}" "왕이 되길 바라지만 그럴 수 없어 흉내내는 것을 당신은 어떻게 생각하나요?"
    "목소리가 나는 곳을 쳐다봤다."
    show bad_nom with dissolve
    "{color=#088A68}???{/color}" "아아, 될 수 있다면 그 무기 좀 내려줬으면 좋겠네요."
    main "개소리 집어쳐."
    "{color=#088A68}???{/color}" "... 그 기세.{w=1.0} 마음에 들었습니다."
    $renpy.pause(2.0)
    "{color=#088A68}???{/color}" "{color=#DF0101}전력을 다해 죽이겠어. {w=1.0}다른 누구도 아닌 늬를.{/color}"
    play sound "shotgun.mp3"
    $renpy.pause(1.5)
    "육중한 샷건의 발포음. {w=1.0}이번엔 아슬아슬하게 걸쳐서 피했지만 근거리 교전이라면 내가 훨씬 불리할 것이다.{p=1.0}총을 갈기며 후퇴"
    play sound "smg.mp3"
    hide bg_inschool
    hide bad_nom 
    scene bg_inschool at backrunning
    show bad_noms
    $renpy.pause(1.5)
    "{color=#088A68}???{/color}" "훌륭한 판단입니다만... {w=1.0}다른 사람이면 몰라도 저에게는 소용 없답니다."
    "총구가 나의 심장을 겨눈다."
    play sound "shotgun.mp3"
    $renpy.pause(.1)
    show bg_inschool at dodge
    show bad_noms at leftbad 
    with moving
    $renpy.pause(1.5)
    "굴러 피했다."
    "{color=#088A68}???{/color}" "정말... {w=1.0}가만히 좀 있으세요."
    #show screen phonebutton
    main "내가 미치지 않고서야 그런 일 없을거야."
    "{color=#CEF6F5}???{/color}" "이봐! 그만 빠진다! 더 이상 머물면 개죽음 당할 뿐이야!"
    "{color=#088A68}???{/color}" "흠... 아쉽군요. {w=1.0}{color=#DF0101}당신을 제 손으로 직접 찢어 죽이고 싶었는데.{/color}"    
    hide bad_noms 
    play sound "walk.mp3"
    $renpy.pause(2.0)
    play sound "smg.mp3"
    main "어딜!"
    $renpy.pause(1.5)
    "화려하게 회피하며 도주한다. {w=1.0}쫒으려고 했으나..."
    play sound "unsummon.mp3"
    $renpy.pause(2.0)
    "역소환 되어 사라졌다."
    $renpy.pause(3.0)
    main "이런..."
    "그녀가 서 있던 곳에 무엇인가 떨어져 있다."
    show signal with dissolve
    "철로 만들어진 상징이다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    "힘 없는 발소리다."
    show seng_nom at right with dissolve
    seng "[main]..."
    "눈에 띄는 상처는 없는 것 같다."
    main "성, 괜찮아?"
    seng "보시다시피. 검에 살짝 긁히긴 했는데 괜찮아.{p=1.0}그것보다... {w=1.0}응?"
    "내가 들고 있는 것과 똑같은 상징을 들고 있는 성."
    main "그 쪽에도 있었던 거야?"
    seng "응..."
    main "이건... 뭘까..."
    seng "글쎄... 안톤도 이건 처음 본다는 눈치였고..."
    play sound "walk.mp3"
    rine "얘들아! {w=1.0}괜찮아?"
    show rine_sad with dissolve
    seng "응."
    "리네는 시선을 움직이다 내 손바닥에 고정했다."
    $renpy.pause(1.0)
    main "왜 그래? {w=1.0}이걸 보고 무엇인가 떠오르는 게 있어?"
    rine "응... 뭐랄까... 어디선가 본 적 있는 것 같은데..."
    hide rine_sad
    show rine_think
    "리네는 곰곰히 생각하기 시작했다."
    $renpy.pause(2.0)
    show rine_sad 
    rine "...{w=1.0} 미안... 모르겠어... {p=1.0}{size=10}이상하네... 분명 어디선가 본 적이 있었는데... {w=1.0}어디였지... 어디였더라..."
    main "그래? {w=1.0}뭐, 괜찮지 않을까?{p=1.0}안톤에게 부탁하면 분명 알아봐 줄거야."
    seng "그렇네.{p=1.0}안톤이 이게 무엇인지 모른다는 것은 조금 의외였지만 안톤이라면 금방 이게 무엇인지 알아낼 수 있겠지."
    play sound "walk_slow.mp3"
    "우리는 발을 돌려 건물 안으로 들어왔다."
    $renpy.pause(2.0)
    scene bg_shoes
    show seng_nom at center
    show rine_nom at right
    with dissolve
    teacher "모두 무사한가요?"
    show read_nom at left with dissolve
    seng "예."
    teacher "저, 성 양, [main] 양."
    "[main], seng" "네?"
    teacher "교장선생님께서 저번에 여러분들께서 제안했던 기획서를 수락하셨습니다.{p=1.0}곧장 공장지대로 보낼 생각이신 것 같습니다."
    main "그런...데요?"
    teacher "만약에 그렇게 된다면 첫번저 완성품이 제작되기 전까지 이곳을 떠나 공장 내에서 머물러야 합니다."
    seng "예."
    teacher "호위가 둘 붙을 것입니다. {w=1.0}한 명은 저고, 다른 한 명은... "
    show picture with dissolve
    "한 여인의 사진."
    teacher "이 사람입니다."
    seng "누구죠?"
    teacher "\'이스프킨\'이란 이름의 방랑자입니다. {p=1.0}공장지대 남편의 불꽃숲에 사는 관리자라고 하더군요."
    main "불꽃숲...{w=1.0} 여러 이유로 이 학교에 들어오지 않은 채 황야 속에서 살아가는 사람들이 있다는 것은 알고 있습니다.{p=1.0}하지만 불꽃숲 안은 고열 떄문에 사람이 살 수 없을 텐데요."
    teacher "그의 눈은 불꽃을 보고, 그곳에서 나오는 열을 조종할 수 있는 힘이 있습니다."
    main "불꽃을 본다...{w=1.0}라..."
    main "과연. {w=1.0}\'불을{rt}이{/rt} {rt}스{/rt}보{rt}프{/rt}{rt} 킨{/rt}는 자\'라 불릴 만 하군요.{p=1.0}하지만 그게 어떻게 가능하죠?"
    teacher "설명하자면 복잡합니다만... 음...{w=1.0}그래. 손에 닿은 물질의 질량을 조절하는 관리자가 있었죠, 저번에?"
    main '네... 분명 있었었죠.{p=1.0}이름은 기억이 안납니다만...'
    teacher "그것과 비슷합니다.{p=1.0}당신도 알다시피 열과 그 열이 가지고 있는 에너지 역시 흐름에 묶여있는 존재지요."
    main "즉 그 흐름을 수정해서 출력을 낮추거나 올리거나 한다는 건가요?"
    teacher "바로 그렇습니다.{p=1.0}그럼, 자세한 것이 결정되면 다시 오겠습니다."
    hide read_nom with dissolve
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    seng "우리도 돌아가자.{p=1.0}여기에 계속 있다간 객귀들이 남긴 잔기에 눌릴 것 같아."
    main "나도 그런 것 같아.{p=1.0}어서 여길 떠나자."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wipeleft
    nvlnarr "\"손을 뻗는 것으로도, 겁의 시간을 달려나가도 닿을 수 없는 공간.{p=1.0}그 곳에 나는 나의 모든 것을 묻고 이리로 왔다.\""
    window hide
    "옛날.{p=1.0}나는 한 사람의 도움을 받았다.{p=1.0}이름없는 떠돌이인 그.{p=1.0}그의 손에 몇번이나 구해지며 나는 간신히 지금까지 성장했다."
    "하지만 이제 그는 없다.{p=1.0}그리고 그와의 맹약을 깨고서 다시 이 경계에 섰다."
    "교외.{p=1.0}나는 그와 처음으로 헤어지기 전 약속했다. {p=1.0}\'다시는 바깥으로 나가지 않겠다.\' {w=1.0}그 약속을 이렇게나 빨리 깨게 될 줄이야."
    scene bg_schooldoor 
    show rine_nom at center 
    show seng_nom at right 
    with dissolve
    seng "다녀올게."
    rine "응! 몸 다치지 말고 잘 갔다와!"
    scene bg_black with wiperight
    "교문 앞에는 버스와 닮았지만 곳곳이 철로 된 봉으로 강화된 차에 몸을 실었다."
    play sound "car.mp3"
    "출발."
    teacher "한참 걸릴테니 미리 좀 자 두세요."
    main "알겠습니다."
    "나는 눈을 붙였다."
    nvl clear
    nvlnarr "\"화살을 쏘아라,{w=1.0} 검을 휘둘러라,{w=1.0} 방패를 높이 들어라!{w=1.0} 약속된 안식이 우리를 기다린다! {w=1.0}끝을 향한 행군을 시작하자!{w=1.0} ypa!{w=1.0} ypa!{w=1.0} ypa!\"{p=1.0}       -\'첫 군주\' 레폰체리아 벨로도디아-"
    nvl clear 
    window hide
    "???" "저 아이가 [main]..."
    "처음 듣는 목소리. {p=1.0}나는 눈을 떴다."
    "등에 검을 메고 있다.{p=.5}흥미롭게 생긴 검인걸. "
    scene bg_bus 
    show guard_nom
    with irisout
    guard "안녕, [main]."
    main "당신이... 이스프킨이군요."
    guard "응."
    "뒤에서 성과 안톤이 소곤거리는 소리가 들린다."
    guard "그래, 내 이름은 \'이스프킨\'. {w=1.0}하지만 될 수 있다면 \'안타{rt}썩{/rt}슈{rt}은{/rt}프{rt}불{/rt}라{rt}꽃{/rt}인\'이라고 불러줬으면 좋겠어."
    "냄새가 난다. {w=1.0}그녀의 온 몸에서 나는 냄새 때문에 질식할 것 같았다.{p=1.0}\'검정\'과 \'빨강\', 그리고 \'보라\'로 이루어진 피와 죽음의 냄새. 그것이 그녀가 살아온 인생이 무엇이었는지 단적으로 알려주었다."
    main "(뭐... 뭐야... 이건... 이 사람은 지금까지... 얼마나 많은 사람을 {color=#DF0101}살해{/color}한거지?)"
    "우리와 나이 차가 그렇게 큰 것 같지는 않았다.{p=1.0}그런데... 어째서 이런 압도적인 차이가...?"
    main "네...{w=1.0}?"
    guard "랄까, 그냥 해 본 소리야."
    "부자연스로운 웃음을 짓는다.{p=1.0}나는 깨달았다. {w=1.0}그녀는 \'동류\'다.{p=1.0}나와, 성과, 리네와 동일한, 자신만의 아픔을 가지고 있는 {w=1.0}자신을 완성하지 못하는 미완성품."
    "그녀의 눈동자 속에 머무는 것은... {w=1.0}\'광기\'이다.{p=1.0}모든 것을 파괴하고 싶어하는, 원초적인 욕구들의 집합체."
    "무심코 그녀의 검에 시선이 갔다."
    scene bg_bus with pixellate
    "뭐지...? 이 현기증은..."
    guard "그렇게 빤히 보니까 {w=1.0}조금 부끄러운걸?"
    main "아, 죄송합니다."
    "시선을 거두었다."
    teacher "이제 거의 도착했습니다. 내릴 준비를 해야 할 것 같군요."    
    main "그나저나 여기는 길의 정비가 아주 잘 되어 있군요.{p=1.0}표지판도 제대로 서 있고 말이죠."
    guard "그건 당연한 거야. {w=1.0}공장지대는 아직 찾는 사람들이 많이 있으니까.{p=1.0}\'객귀\'들을 막기 위한 병기들의 생산 역시 아직까지는 정상적으로 이어지고 있고 말이야."
    main "그렇군요."
    scene bg_black with wiperight
    $renpy.pause(3.0)
    "버스에서 내렸다."
    play sound "car.mp3"
    $renpy.pause(2.0)
    "버스가 다시 출발하고 우리는 교사 안으로 들어갔다."
    guard "교사 밖으로는 나가지 않는 게 좋아. {w=1.0}학교 구역을 제외한 다른 구역들 말이야."
    "이스프킨이 말했다."
    main "왜 그러죠?"
    guard "...별로... {w=1.0}좋은 꼴은 못 볼거야."
    seng "알겠습니다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    "안톤은 이 학교의 교장과 다른 선생들과의 회담이 있다고 말하며 그리로 가고 이곳에는 우리 셋만 남았다."
    seng "여기서 가만히 이러고 있는 것도 그러니까 배정된 숙소로 가 있어요."
    guard "그래. {w=1.0}그렇게 나쁜 생각은 아니네."
    scene bg_room2
    show seng_nom at center
    show guard_nom at right
    with wipeleft
    "귀빈실.{p=1.0}나는 쓴웃음을 지을 수 밖에 없었다."
    guard "왜 그렇게 기분 나쁘게 웃어?"
    main "아뇨, 귀빈실에는 안 좋은 추억이 좀 있어서 말이죠."
    guard "너도 그래? {w=1.0}우연이네."
    main "당신도요?"
    guard "응. {w=1.0}뭐, 내 경우를 따지자면 귀빈실 자체 보다는 이곳, 공장지대에 악연이 있는 것에 가깝겠지만."
    seng "무슨 일 있었나요?"
    guard "...응. {w=1.0}이곳에서 좀... 껄끄러운 일이 있었어."
    $renpy.fix_rollback()        
    menu:
        "캐묻는 것은 실례이다. 더 이상은 알려 하지 말자.":
            $renpy.fix_rollback()        
            main "그랬군요..."
            guard "...큭. {w=1.0}지금 와서 생각하자면 우스운 일이었지...{p=1.0}{size=5}하지만 그 일이 없었더라면 인류가 이 개고생을 할 이유가 없었겠지{/size}"
        "설명해 주실 수 있으신가요?":
            main "무슨 일이 있었는지 이야기 해 주실 수 있으신가요?"
            guard "........"
            main "불쾌하셨다면 죄송해요."
            guard "아니야, 딱히 불쾌해 할 일도 아니니까.{p=1.0}대략적으로만 설명해 줄게.{w=1.0} 여긴... 내가 첫 살인을 했던 장소야."
            seng "네?"
            guard "바로 이 귀빈실이야. {w=1.0}벌써 3년이나 흐른 이야기지만."
            main "에..."
            guard "옛날 이야기는 여기까지."
            $renpy.fix_rollback()        
            $destroy+=3
            "그녀는 분명히 말했다.{p=1.0}\'살인\'이라고..."
            "무슨 일이 있었던 거지? {w=1.0}아니, 내가 알려고 해도 되는 일인가?"
    "분위기가 묘해져 버렸다."
    guard "자, 옛날 이야기는 여기까지 하자."
    $renpy.pause(8.0)
    play sound "knock.mp3"
    "???" "[main] 님, 성 님. {w=1.0}당신들이 보호자 분께서 당신들을 호출하셨습니다.{p=1.0}같이 가 주실 수 있으실까요?"
    seng "알겠습니다."
    main "다녀오겠습니다, 이스프킨."
    guard "그래..."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_inschool 
    show seng_nom
    with dissolve
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_middle
    show seng_nom
    with dissolve
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_hallway 
    show seng_nom
    with dissolve
    play sound "jab.mp3"
    $renpy.pause(2.0)
    teacher "저는 인정할 수 없습니다! {w=1.0}그런 것 따위, 용납 불가능합니다!"
    "{color=#000FFF}???{/color}" "닥쳐!"
    teacher "이런 식이라면 저는 더 이상 할 말이 없습니다." 
    play sound "doorclosed.mp3"
    show read_ang at right with dissolve
    teacher "{size=10}병신들..."
    main "예?"
    hide read_ang 
    show read_nom at right
    with dissolve
    teacher "아, [main] 양, 성 양. 헛걸음하게 만들어 버렸군요.{p=1.0}...돌아가주세요. 저 곳은 여러분이 있을 장소가 아닙니다."
    main "하지만..."
    teacher "괜찮습니다. 가주셔요."
    $renpy.fix_rollback()        
    menu:
        "알겠습니다.":
            $renpy.fix_rollback()        
            main "숙소로 돌아가면 될까요?"
            teacher "예. {w=1.0}저는 찾아야 할 것이 있으니 조금 있다 가도록 하겠습니다."
            hide read_nom with dissolve
            play sound "walk_slow.mp3"
            $renpy.pause(2.0)
            main "우리가 참견할 일은 아니야. {w=1.0}안톤에게도 안톤만의 사정이 있겠지.{p=1.0}이곳은 우리가 있던 학교가 아니라 외지니까 일단은 그의 말을 듣자."
            seng "분명 방금 전의 표정... 평소랑 달랐었지?"
            seng "네가 그렇게 말한다면야."
        "안톤? 표정이 별로 좋지 않은데요.":
            $renpy.fix_rollback() 
            main "저 안에서 큰 소리가 났었는데 무슨 일 있었나요?"       
            teacher "당신들이 알아야 할 일은 아닙니다."
            "그가 처음으로 나의 질문에 대답을 하지 않았다."
            main "알려주세요."
            seng "네, 알려주셨으면 합니다."
            teacher "[main] 양, 성 양. {w=1.0}예전부터 말하려 했지만 참아왔던 말인데, 이제는 해야 할 것 같습니다.{p=1.0}이것은 당신들이 알아서는 안되는 문제입니다. {w=1.0}당신들은 이해할 수 없고, 또 이해해서도 안되는 그런 이야기입니다."
            teacher "저 같은 선생들은 모든 위협들로부터 여러분들을 보호하고 꿈과 희망을 전하는 사람입니다.{p=1.0}아직은 여러분들까지 아파야 할 이유는 없습니다. {w=1.0}힘든 것들은 제가, 선생님들이 전부 해결할테니까, 여러분들은..."
            seng "그만하시죠."
            main "...안톤. {w=1.0}당신의 마음은 십분 이해합니다. 당신에게 있어서 저와 성은 첫 제자이겠지요.{p=1.0}하지만 안톤. 여기에 온 것은 제가 그 논문을 제출했기 때문입니다. {p=1.0}여기서 생기는 모든 일에 대한 책임이 당신에게만 있는 것이 아닌, 저에게도. 성에게도 있는 것이라고 생각합니다."
            teacher "...감사합니다, [main] 양... 하지만 정말로... 이것은 당신들이 발을 들여선 안 될 일입니다.{p=1.0}죄송합니다. 아무리 \'당신들을 위해서\'란 이유가 있다 하여도 사실을 숨겨선 안되겠지만... {w=1.0}알려 하지 말아주시길 부탁드리겠습니다."
            "그의 웃음에 씁쓸함이 돌고 있다.{p=1.0}그가 나에게, 성에게 숨기려 하는 것은 우리가 알아서 좋을 것이 없는 일이겠지.{w=1.0} 하지만..."
            main "...알겠습니다. "
            teacher "먼저 숙소로 돌아가 기다려 주십시오. {w=1.0}저는 찾아야 할 것을 찾은 후 돌아가겠습니다."
            hide read_nom with dissolve
            play sound "walk_slow.mp3"
            $renpy.pause(2.0)
            seng "[main]."
            main "응?"
            seng "궁금한 것 아니었어?"
            main "궁금해."
            seng "그런데 왜 안톤을 붙잡지 않았어?"
            main "그는 우리 학교의 어떤 선생님들보다 우리를 보호하려고 노력하고 있어.{p=1.0}지금은... 그 노력을 존중해주자."
            seng "...알았어."
            $firstcurious="안톤이 우리에게 숨기고자 하는 것은 무엇일까?"
            $temp2=True
    scene bg_black with wipeleft
    play sound "walk_slow.mp3"
    if temp2==True:
        "안톤. {w=1.0}당신의 노력에, 수고에 언제나 감사하고 있습니다. 그리고...{w=1.0} 죄송합니다."
    $renpy.pause(2.0)
    play sound "door.mp3"
    scene bg_room 
    show seng_nom
    with wiperight
    $renpy.pause(2.0)
    "방에 들어왔을 때 이스프킨은 없었다."
    seng "이스프킨은 어디 갔지?"
    main "잠깐 기분전환 삼아 산책이라도 나갔겠지."
    seng "그런가?" 
    "바깥의 길도 모르니 방 안에 가만히 있는 것에 성도 동의하여 우리는 안에서 대기했다."
    "쓸모 없는 잡담들." 
    $renpy.pause(4.0)
    play sound "door.mp3"
    show guard_nom at right with dissolve
    guard "뭐야, 한참 걸릴 줄 알았더니 금방 왔네?"
    seng "예. 안톤이 우리를 되돌려 보냈습니다."
    guard "그런가... {w=1.0}안톤이 그런 것인가..."
    "그녀는 중얼거렸다."    
    hide guard_nom
    guard "{size=10}기다리는 건 딱 질색인데... {w=1.0}대체 무슨 생각을 하고 있는거야...{/size}"
    "그녀는 불안한 듯 하다. {w=1.0}계속 무엇인가 중얼거리며 바닥에 앉아 있다."
    "1시간, {w=1.0} 2시간. {w=1.0}시간은 계속 흘러갔고 영원히 이어질 것 만 같았던 기다림 끝에 안톤이 문을 열었다."
    play sound "door.mp3"
    $renpy.pause(2.0)
    show read_nom at right with dissolve
    show guard_nom at left with dissolve
    guard "안톤!"
    teacher "아, 모두 모여 있네요."
    "안톤은 만족스러운 표정이다.{p=1.0}찾으려 했던 것을 찾아낸 듯 하다."
    teacher "오, 벌써 시간이 이렇게 됐군요. {w=1.0}뭐라도 사드리겠습니다. 같이 가시죠."
    guard "나는 됐어."
    teacher "괜찮으시겠습니까? 무언가 먹지 않아도?"
    guard "배가 별로 고프지도 않고, 고프면 내 돈으로 사 먹어도 되니까."
    teacher "그렇다면야... {w=.5}알겠습니다."
    play sound "door.mp3"
    scene bg_inschool
    show read_nom at right 
    show seng_nom
    with dissolve
    $renpy.pause(1.5)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_meal 
    show read_nom at right 
    show seng_nom
    with dissolve
    teacher "무엇을 드시겠어요?"
    seng "글쎄요..."
    "나는 가격표를 훑어 그 중 가장 익숙하고 싼 것을 골랐다."
    main "저는 스프로 하겠습니다."
    seng "저도 그렇게 할게요."
    teacher "그렇게 싼 것 시킬 필요 없는데... {w=.5}...알겠습니다."
    "안톤은 카운터에 가 주문하고 세 개 스프를 받아 왔다."
    play sound "phonebeep.mp3"
    $renpy.pause(2.0)
    teacher "네. 안티 벨라우인의 안톤, 전화 받았습니다. {w=1.0}예. 알고 있습니다. {w=1.0}예? 아니오, 아닙니다... {w=1.0}네... 알겠습니다..."
    hide read_nom
    show read_ang at right with dissolve
    teacher "{size=5}젠장... 부흥회 녀석들... 일을 얼마나 키울 셈이야...{/size}{w=.5}...미안합니다. 아무래도 일이 생겨서 가봐야 할 것 같습니다."
    hide read_ang        
    play sound "walk.mp3"
    "안톤이 급히 길을 떠났다."
    seng "...방금 그 표정..."
    main "응... {w=.5}누구한테인지는 모르겠지만 분명 화가 나 있었어."
    if firstcurious!=None:
        main "살짝 쫒아가 보자."
        "우리들은 자리에서 일어났다."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_ground
        show seng_nom
        with dissolve
        guard "어딜 가려고?"
        show guard_nom at right with dissolve
        "이스프킨이 말을 걸어왔다.{p=1.0}명백히 우리를 가로막는 것이다."
        main "비켜주시면 안될까요?"
        guard "어딜 가는 지 들어보고."
        "그녀는 자신만만하다. {w=1.0}...물러나야 하나..."
        seng "......."
        guard "무엇인가 떳떳하지 못한 짓을 하려고 했구나. {p=1.0}미안하지만 안톤으로부터 너희들을 보호해 달라는 부탁을 들어서 말이야.{p=1.0}그에게 진 빚을 갚기 전까지는 난 최선을 다해 너희들을 지키겠어."
        main "...그런...가요..."
        guard "그래. 돌아가서 씻고 자렴. {w=1.0}너희들이 자는 동안 숙소의 경계는 내가 할 테니까."
        seng "...알겠습니다."
        play sound "walk_slow.mp3"
        "우리들은 숙소로 향했다."
        hide seng_nom
        $renpy.pause(2.0)
        "그들은 안전하게 빠져나갔다."
        guard "하하... 죽기 위한 싸움이라... 멋지군...{p=1.0}아주 마음에 들어... {w=1.0}속죄를 위한, 더 없이 완벽한 무대가 준비되다니."
        play sound "walk.mp3"
        guard "다 들려... 다 들린다고..."
        $renpy.pause(2.0)
        "암살자들" "죽여라!"
        guard "춤춰라... 미친 듯이 춤춰라. 그리고서 한 송이의 꽃을 피워라... 빨간... 아주 빨간... {w=1.0}{color=#DF0101}피의 장미를.{/color}"
        play sound "bigbell.mp3"
        guard "끝으로 인{rt}인{/rt}도하는 마{rt}컴{/rt}지막 장미!"
        $renpy.pause(10.0)
        "???" "아."
        play sound "blooding.mp3"
        hide guard_nom
        scene bg_nightschoolred with Dissolve(6.0)
        show guard_nom at right 
        "암살자들의 피가 땅을 적셨다."
        "이런 녀석들만 온다면 날이 밝을 때까지도 버틸 수 있다.{p=1.0}하지만 문제는..."
        guard "진짜배기가 안 나왔다는 건데... {w=1.0}안톤... 나라도 버틸 수 있는 한계가 있어... {p=1.0}부탁이니 내 힘이 다하기 전에 끝내줘..."
        play sound "walk.mp3"
        $renpy.pause(2.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "mamiru.mp3"
        $renpy.pause(1.0)
        "베었다."
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "mamiru.mp3"
        $renpy.pause(1.0)
        "한 명 더."        
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "slash.mp3"
        $renpy.pause(1.0)
        play sound "mamiru.mp3"
        $renpy.pause(1.0)
        "다시 한 명."
        ".{w=.5}........{w=.5}.............."
        scene bg_black with fade
        "얼마나 긴 시간이 흘렀을까."        
        "서서히 휘두르는 팔에 감각이 마비되어 간다."
        "내가 베어온 수많은 사람들과 같이. {w=1.0}나 역시 똑같은 운명을 맞이할 것이다.{p=1.0}결국... 실패하였다."
        show guard_nom at Position(xalign=.5, yalign=1.0)
        play sound "bite.mp3"
        $renpy.pause(1.0)
        play sound "bite.mp3"
        $renpy.pause(1.0)
        play sound "bite.mp3"
        $renpy.pause(1.0)
        play sound "blooding.mp3" 
        show guard_nomred at Position(xalign=.5, yalign=1.0) with Dissolve(4.0)
        play sound "jab.mp3"
        hide guard_nom
        hide guard_nomred
        $renpy.pause(2.0)         
        scene bg_bigdoor with Dissolve(4.0)
        scene bg_bigdoor at walk
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        teacher "이 앞이려나요..."
        show read_nom at center2 with dissolve
        play sound "door.mp3"
        scene bg_black with dissolve
        "어둡다. 매우 어둡다.{p=1.0}한 치 앞도 보이지 않을 정도이다."
        "{color=#F0F8FF}???{/color}" "이봐, 도둑고양이."
        teacher "...?!"
        "목소리가 들렸다."
        "{color=#F0F8FF}???{/color}" "여긴 왜 왔지?"
        teacher "찾을 물건이 있어서 왔습니다."
        "{color=#F0F8FF}???{/color}" "그런가. 너 역시 마찬가지인 것인가."        
        teacher "당신이 방해하신다면... {w=.5}별로 원하지는 않지만 당신과 교전할 수 밖에 없습니다."
        "{color=#F0F8FF}???{/color}" "진정해. 나는 네게 소식을 전해주기 위해 왔을 뿐이니까."
        teacher "소식...인가요?"
        "{color=#F0F8FF}???{/color}" "쓸데없는 호기심이 고양이를 죽이지. 조심하라고.{p=1.0}네 계획을 아는 사람이 너 뿐이 아닐테니까."
        teacher "네?"
        "{color=#F0F8FF}???{/color}" "\'유리잔의 나이트를 위하야. 그 이름없는 왕을 위하야.\'"
        teacher "이봐요! 당신은 누구죠? 왜 그 시를 알고 있는 것이죠?"
        "{color=#F0F8FF}???{/color}" "......."
        teacher "거기 아무도 없어요?"
        "{color=#F0F8FF}???{/color}" "......."
        teacher "빠져나간건가..."
        "차가운 정적만이 방 안에 감돌고 있다.{p=.5}나는 미리 계산했던 대로 세 걸음을 걸어가 손을 뻗었다.{p=.5}딱딱한 나무의 감촉."
        play sound "chest.mp3"
        $renpy.pause(2.0)
        scene bg_bigdoor 
        show read_nom at center2
        with dissolve
        teacher "이건..."
        "편지...?"
        play sound "book.mp3"
        $renpy.pause(2.0)
        $preferences.text_cps=40
        $preferences.text_cps=0
        nvlnarr "스스로 가야할 길을 잊은 도둑고양이여, 명심하게나.\n한 때 철저히 지켜지던 비밀도 결국에는 밝혀졌음을.\n그대가 꾸민 일 역시 그대만이 알고 있는 것이 아닐지니, 언제나 주위를 잘 살피며 나아가게나."
        nvlnarr "PS. 유리잔의 심상은 깨져 기사를 안에서부터 죽여나갔다. 왕도를 걷는 왕을 쫒아 그를 죽이려 했건만, 자신이 왕도의 끝에 도달하여 왕관을 쓴 채 죽음을 맞이한 것이다."
        $preferences.text_cps=40        
        teacher "....... {w=1.0}핫!"
        play sound "walk.mp3"
        $renpy.pause(1.0)
        scene bg_ground 
        show read_nom
        with dissolve
        $renpy.pause(.5)
        teacher "......."
        hide read_nom
        show read_ang
        teacher "이스프킨..."
        guard "......."
        "맥을 짚었다.{p=1.0}끊어진 채 아무 반응도 보이지 않는 맥."
        teacher "누가... {w=.5}누가... 이런 끔찍한 짓을..."
        "범인은 자명했다."
        "가방을 열었다.{p=1.0}떨리는 손으로 병의 뚜껑을 열어 이스프킨의 영혼을 병에 담았다."
        teacher "금방... 금방... 되살려 드리겠어요... 그때까지만..."
        "뚜껑을 닫아 가방에 넣고 숙소로 뛰었다."
        play sound "walk.mp3"
        scene bg_ground at running
        $renpy.pause(1.5)
        scene bg_ground at running
        teacher "제발... 아이들만은..."
        "아이들만은 건드리지 않았기를..."
        $renpy.pause(.4)    
        scene bg_black with wipeleft
    play sound "walk.mp3"
    $renpy.pause(5.0)
    scene bg_room 
    show seng_nom at right
    with wiperight
    "밖에서 빠른 걸음소리가 들린다.{w=.5}총성과 뜀박질..."
    "누구지?"
    $renpy.fix_rollback()        
    menu:
        "문을 연다.":
            $renpy.fix_rollback()        
            play sound "door.mp3"
            $renpy.pause(2.0)
            show read_nom with dissolve
            teacher "{size=5}하느님 감사합니다...{/size}몸은 괜찮은가요?"
            main "왜 그러세요? 숨도 꽤 몰아쉬게 계신데, 달려 오셨나요?"
            teacher "다행히군요... 여기는 아무 일도 없었나요..."
            if temp2==True:
                "우리를 막아섰던 이스프킨에게 무슨 일이 있었던 것일까?"
                teacher "주무시는데 깨워서 죄송합니다. 계속 주무셔요."
                $renpy.fix_rollback()        
                menu:
                    "이스프킨은 어디에 있죠?":
                        $renpy.fix_rollback()        
                        main "이스프킨은 어디에 있죠? 당신과 함께 있을 것이라 생각했는데..."
                        teacher "그녀는... 지금 학교지대를 벗어나 공장까지 갔습니다."
                        main "왜죠?"
                        teacher "제가 무언가 부탁했기 때문이죠."
                        main "그 부탁이 무엇인가요?"
                        hide read_nom
                        show read_think
                        teacher "........"
                        "무언가 고민하는 듯 하다."
                        hide read_think
                        show read_nom 
                        teacher "이것과 똑같이 생긴 병을 가져와 달라고 했습니다."
                        "가방에서 꺼내져 내 눈 앞에 놓인 것은 투명한 핑크색 액체처럼 보이는 것을 담고 있는 병이었다."
                        seng "이건..."
                        main "무엇인지 알 것 같아?"
                        seng "응..."
                        "머뭇거림."
                        main "무엇이길래 그래?"
                        seng "영혼... 저건...{w=.5} 인간의 영혼이야..."
                        teacher "네. 당신이 말했듯이 이것은 사람의 영혼을 담아 놓은 병이지요."
                        seng "이게 왜 당신께 있는 것이죠?"
                        teacher "교장선생님의 명령...{w=.5}이라고 한다면 믿어 주실건가요?"
                        main "그럴 리가요."
                        teacher "...하지만 사실은 사실입니다.{p=.5}나머지는 좋을 대로 생각해 주세요."
                        main "........"
                        $secondcurious="안톤은 어째서 사람의 영혼이 든 병을 가지고 있을까?"
                        teacher "아, 그렇지. {w=.5}이것을 가지고 계세요. 제가 달라고 할 때까지만."
                        seng "...별로 내키진 않지만... 알겠습니다."
                        $thirditem="영혼이 담긴 병"
                        "그는 채 우리가 무엇을 말하기도 전에 나가버렸다."
                    "알겠습니다.":
                        $renpy.fix_rollback()        
                        main "그럼 알겠습니다. 당신은 안 주무시나요?"
                        teacher "아직은요."
                        "성이 의심스러운 눈초리로 쳐다본다. 손을 뻗어서 제지."
                hide read_nom
                hide read_smile
                play sound "walk_slow.mp3"
                $renpy.pause(2.0)
                play sound "door.mp3"
                $renpy.pause(2.0)
        "경계한다.":
            $renpy.fix_rollback()   
            play sound "knock.mp3"
            teacher "[main] 양, 성 양. {w=.5}안톤입니다. 거기 안에 계시나요?"
            seng "안톤이라는데 열어야 하는 거 아니야?"
            main "잠깐 기다려."
            play sound "knock.mp3"
            teacher "제발... 안에 계신다면 대답해 주세요..."
            main "당신은 누구인가요?"
            teacher "아, 무사하셨군요... "
            "...우리들의 안위를 제일 먼저 걱정했다.{p=.5}진짜...인가...?"
            play sound "door.mp3"
            show read_nom with dissolve
            $renpy.pause(2.0)
            teacher "성 양... [main] 양... 무사하셨군요..."
            seng "무슨 일이죠? 아까전엔 총성까지 들리던데..."
            teacher "우리와 똑같습니다. {w=.5}아마 무기 양산을 방해하려는 목적이겠죠."
            "객귀들의 침입인가..."
            teacher "지금은 전부 사라졌습니다만... 다시 올지 오지 않을 지 잘 모르겠습니다.{p=.5}혹여 총성이 들리더라도 너무 놀라지 마시고 이 곳에 있으면 될 겁니다."
            main "밖으로 피난하는게 안전하지 않을까요?"
            teacher "아뇨. 바깥은 돌아다니는 파수들을 제외하곤 거의 아무도 없습니다. 하지만 이곳은 마법과 경비병들이 지키고 있죠.{p=.5}괜찮을 겁니다."               
            seng "알겠습니다. 그리 하지요."
            hide read_nom 
            play sound "door.mp3"
            $renpy.pause(2.0)
    main "무슨 일이 일어나고 있는걸까?"
    seng "글쎄. 우리는 상상하지 못할 큰 일일지도 모르지."
    main "걱정 마. 이번에는 내가 지켜줄테니까."
    hide seng_nom
    show seng_smile at right
    seng "응!"
    scene bg_black with dissolve
    "(다음날 아침)"
    scene bg_room 
    show seng_nom with dissolve
    with dissolve
    play sound "knock.mp3"
    teacher "안톤입니다."
    $renpy.pause(2.0)
    play sound "door.mp3"
    show read_nom at right with dissolve
    teacher "어제 밤에는 제대로 못 주무셨죠?"
    seng "조금... 수면 부족 상태이긴 해요."
    teacher "그런 때에 이런 부탁 드려서 정말 죄송하지만, 저랑 같이 누굴 좀 만나로 가야 할 것 같습니다."
    main "누구죠?"
    teacher "공장지대의 공장장입니다. {w=.5}제가 보여준 설계도와 제 설명만으로는 부족한지 여러분을 만나고 싶다고 하더군요."
    main "그렇다면 가겠습니다."
    "나는 가방을 들었다."
    play sound "walk_slow.mp3"
    scene bg_inschool with dissolve
    $renpy.pause(2.0)
    play sound "door.mp3"
    $renpy.pause(2.0)
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    scene bg_black with wipeleft
    $renpy.pause(3.0)
    scene bg_library 
    show factory_nom at center2   
    show seng_nom at right
    with wiperight
    "서재."
    factory "당신들이 이것을 처음으로 기획한 사람이군요?"
    seng "그렇습니다."
    factory "제가 여쭙고 싶은 것은 여기 이 부분입니다."
    "그가 짚은 부분은 기관부였다."
    main "이곳이요?"
    factory "예. 여기에 당신들이 기입한 이 부품의 규격을 구하는 수식을 도저히 이해할 수 없습니다."
    "설명했다."
    factory "그런가요...{p=.5}알겠습니다. 그렇다면 그리 알고 작업하도록 하죠. {w=.5}시제품은 2주 뒤면 그쪽에 도착할 겁니다."
    main "알겠습니다."
    play sound "door.mp3"
    scene bg_hallway 
    show seng_nom at center
    show read_nom at right  
    with dissolve
    teacher "잘 끝났나요?"
    main "네."
    teacher "후아... 이제 이 곳에서 해야할 일은 얼추 끝났군요. {w=.5}차가 도착하는 대로 이곳에서 떠날 수 있겠어요."
    seng "거기서 여기까지 오는데 2시간 정도 걸렸으니, 지금 차량을 요청해도 2시간이 비는군요."
    teacher "그렇군요. 흠... {w=.5}그렇다면 그 동안은 자유시간으로 합시다. 학교가 있는 곳을 벗어나지 않는 범위 내에서 자유롭게 놀도록 하세요."
    seng "알겠습니다."
    teacher "저는 이곳의 선생님들과 할 이야기가 있으니 자리를 비우겠습니다."
    play sound "walk_slow.mp3"
    hide read_nom 
    $renpy.pause(2.0)
    if temp2 != False:
        call antoncurous
    else:
        call antonnocurious
    $deleteSave()
    $renpy.quit()
    
    label game3: 
        call afterreset
        "???" ".......{w=.5} ....... {w=.5}....... {w=.5}....... {w=.5}....... {w=.5}....... {w=.5}End."
        $renpy.full_restart()