label afterreset:        
    if os.path.isfile(home+"/char_nom.png"):
        image char_nom = home+"/char_nom.png"
        image char_sad = home+"/char_sad.png"
        image char_ang = home+"/char_ang.png"
    $renpy.music.play('Mr.J2_1.mp3', 'music')    
    scene bg_black
    call events_run_period from _call_events_run_period
    # "test" "[home]"       
#        show char_nom
    if persistent.trueR:
        centered "다시 왔구나?"
        extend "\n음... 너무 강압적이었던 거려나?"
        extend "\n한 번 정도는 괜찮겠지."
        extend "\n이어해도 좋아."
        extend "\n{color=#DF0101}네 이야기를{/color}."
        $emotion="ang"
        $destroy = persistent.destroy
        $equal = persistent.equal
        show screen dest
        "의문의 목소리" "너는 생각했을 것이다."
        main "......."
        "의문의 목소리" "\'내가 도망치는것은 그네들과의 약속을 지키기 위해서\'라고."
        main "......."
        "의문의 목소리" "네 옆에서 죽었다."
        main "......."
        "의문의 목소리" "제일 먼저 네 어머니가."
        play sound "scream.mp3"
        show cg_blood at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        "의문의 목소리" "그 다음으로 네 동생들."
        play sound "scream.mp3"
        show cg_blood2 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood3 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood4 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        "의문의 목소리" "기타 등등..."
        play sound "scream.mp3"
        show cg_blood5 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood6 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood7 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood8 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood9 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood10 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood11 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood12 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood13 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood14 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood15 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood16 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood17 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood18 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood19 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood20 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        main "{size=5}아니야... 나는... 그러지... 않았어...{/size}"
        "의문의 목소리" "뭐라고?"
        main "{size=10}나는... 그러지 않았어...{/size}"
        "의문의 목소리" "잘 안들리는데?"
        main "나는 그러지 않았어!!!!!!"
        "의문의 목소리" "아니. {w=.5}네가 그랬어."
        main "아니야, {w=.5}아니야, {w=.5}아니야, {w=.5}아니야, {w=.5}아니야!"
        "의문의 목소리" "맞아, {w=.5}맞아, {w=.5}맞아, {w=.5}맞아, {w=.5}맞아, {w=.5}맞아."
        main "......."
        "의문의 목소리" "넌 그들을 \'배신\'했어. {w=.5}널 길러준 어머니를. {w=.5}너와 놀아준 친구들을. {w=.5}너의 소중한 동생들을. 전부."
        main "불가항력... 이었잖아..."
        "의문의 목소리" "과연 그럴까?"
        main "........"
        "의문의 목소리" "네가 달리던 발을 멈추어서 어떤 한 사람을 붙잡았다면.{p=.5}{color=#FF0000}{b}과연 그들은 죽었을까?{/b}{/color}"
        main "아니야.... 아니라고... 그네들이 죽은 것은... 내 책임이..."
        "의문의 목소리" "해답은 너도 알고 있잖아?"
        main "...아..."
        "알고 있었다. {w=.5}나는 도망쳤다. 다른 이들을 제물 삼아, 운명으로부터."
        "의문의 목소리" "그러니, 너는 아무와도 같이 있을 수 없겠지."
        main "........"
        "의문의 목소리" "\'친구\' 한 명 없겠지."
        main "아니."
        "의문의 목소리" "\'성\'? \'리네\'? {p=.5}그들이 정말로 너의 친구일까?"
        main "믿을 수 있어."
        "의문의 목소리" "정말로? 그네들도 그렇게 생각할까? 자신의 목숨을 네게 맡기고 싶어할까?"
        main "당연하지."
        "의문의 목소리" "다짐하지 않았어? 그 날, 네 손으로 \'무명\'을 죽인 날에.{p=.5}아무도 믿지 않고, 모든 것을 의심하여 대비하겠다고?{p=.5}너도 알고 있잖아. \'친구\'라고, \'보호자\'라 믿을 수 있는 사람은 더 이상 이 세상에는 없다는 것을.{p=.5}믿음의 끝에는 \'파국\'과 \'아픔\'만이 있다는 것을."
        "의문의 목소리" "사실은 그렇지? 그들을 신뢰하지 못하지? {p=1.0}{color=#FF0000}{b}의심{/b}{/color}하고 있지?"
        main "........."
        "\'아니다\'라 단언할 수 있다.{p=1.0}\'아니다\'라 단언해야만 한다."
        "의문의 목소리" "너. 정말 이기적이야."
        main "........"
        "의문의 목소리" "남을 완전히 믿지 않으면서 스스로를 속이고, 남들을 속이고.{p=.5}그런게 용서받을 수 있을까?"
        main "아... 아..."
        "말이 나오지 않았다."
        main "(뭐야... 왜... 목소리가...?)"
        "의문의 목소리" "그들이 너를 어떻게 생각하는 지는 나 역시 알 수 없어.{p=.5}하지만 그것이 거짓된, 위선이라고 하여도 베풀어 준 사람한테는 고마워 해야하겠지?"
        main "......."
        main "(아... 그런가...)"
        "나는 깨달았다."
        main "(목소리가 나오지 않는 이유를. {w=.5}말을 할 수 없는 이유를.{p=1.0}마음 속으로 \'인정\'한 것이다. 나의 죄를. 그의 말을.)"
        "의문의 목소리" "죄인에게는 그 자가 지은 죄에 맞는 벌이 있어야 하지. {w=.5}안 그래?"
        "끄덕였다."
        "그가 손을 뻗었다."
        $destroy+=10
        play sound "soul.mp3"
        $destroy+=10
        $destroy+=7
        main "아."
        "따스하다."
        "아프지 않다."
        "그저... 파도 없는 잔잔한 바다에서 느린 보트를 타고서 그 위에 누운 듯한 느낌."
        "아주... 아주 오랜만에 느끼는... 그런 것..."
        "의문의 목소리" "드디어... 몸을... 얻었다..."        
        anothervoice "드디어..."
        "손가락을 움직여 보았다.{p=.5}정상이다.{p=.5}치고 있었던 \'막\'을 거두었다."
        scene bg_floor with irisout
        anothervoice "크으으... 머리야..."
        seng "[main]! 괜찮아? 무사해?"
        anothervoice "......."
        play sound "blanket.wav"
        scene bg_room
        show seng_nom at left
        with dissolve
        $renpy.pause(.2)
        hide seng_nom
        show seng_smile at left
        seng "일어났구나! 다행이다..."
        "나는 손을 휘둘렀다."
        play sound "sword.mp3"
        $renpy.pause(1.0)
        seng "악!"
        "보이지 않는 바람의 칼날이 \'그 녀석\'은 성이라 부르던 소녀의 손등에 상처를 냈다."
        hide seng_smile
        show seng_nom at left
        seng "......."
        anothervoice "......."
        seng "너는... 내 친구가 아니구나."
        anothervoice "인사가 늦었네. 내 이름은 Ψ{rt}한{/rt}.{p=.5}뭐, 당분간은 \'잘 부탁한다\'라고 해 두지."
        hide seng_nom
        show seng_battle 
        "한 발짝 물러서 나를 경계한다.{p=.5}그 모습은 보고서 그녀 역시 또 다른 한 명의 \'관리자\'라고 내심 깨달았다."
        seng "...어째서 [main]의 몸을 빼앗은 거지?"
        anothervoice "그야 나는 \'신편\'이니까.{p=.5}빼앗는 것이 본능인걸?"
        seng "........"
        anothervoice "상처 입힌 건 미안해. 본의가 아니었어."
        "여전히 나를 경계하며 말문을 열지 않고 있다."
        anothervoice "너랑 싸우고 싶지 않아. {w=.5}너는 내가 존재할 수 있게 해주는 숙주의 친구니까."
        seng "나는 너를 신뢰할 수 없어.{w=.5}신편을 믿는 것 만큼 바보같은 일도 없다는 것을 알고 있거든"
        anothervoice "이런. 섭섭한걸. {w=.5}일단은 숙주의 행동 방침을 존중하고 있는데 말이지."
        play sound "drawning.wav"
        $renpy.pause(1.7)
        stop sound
        "성은 발검했다."
        anothervoice "그래서 어떻게 할 거야?{p=.5}그걸로 날 찌르기려도 하려고?"
        seng "당연하지."
        anothervoice "헤? 넌 날 못 찔러."
        seng "아니. 찌를 수 있어."
        anothervoice "못 찔러. 너는 [main]의 몸을 상처 입힐 수 없어."
        seng "아니야!"
        anothervoice "{b}그럼 네 손이 떨고 있는 건 기분 탓일까?{/b}"
        seng "...칫."
        anothervoice "너는 어쩔 수 없이 나에게 협력할 수 밖에 없어.{p=.5}지금은 너를 해치지 않아.{w=1.0} 그런데, 자랑은 아니지만 나. 기분이 상당히 빨리 변하거든.{p=.5}언제 어떻게 변해서 너를 {b}{color=#F00}죽여{/color}{/b}버릴지 몰라."
        play sound "sworddrop.mp3" 
        seng "........"
        $renpy.pause(.5)
        "검이 떨어졌다."
        anothervoice "딱히 다른 사람들한테 피해를 끼칠 생각은 없어.{p=.5}내가 원하는 건 살아가는 것 뿐이니까."
        seng "거짓말."
        anothervoice "믿어 줬으면 좋겠어."
        play sound "walk_slow.mp3"
        "걸음을 내딛었다."
        $renpy.pause(2.0)
        "오랜만의 걸음."
        "\'살아있다\'라는 것을 인식했다."
        play sound "door.mp3"
        seng "어디로 가는거야."
        anothervoice "산책... 이려나..."
        seng "길...을 잃을 일은 없겠군."
        anothervoice "다녀올게."
        play sound "walk_slow.mp3"
        scene bg_hallway2 at walk with dissolve
        "나는 [main]의 기억을 훑었다.{w=.5} 이 몸의 주인이 원래와 다르다는 것을 아는 사람은 성 한 명이면 충분하다."
        play sound "door.mp3"
        show rine_nom at right with dissolve
        $renpy.pause(1.5)
        hide rine_sad
        show rine_nom at right
        rine "[main]!"
        "마침 좋은 상대가 나타났다."
        anothervoice "리네."
        rine "몸은 이제 괜찮은거야?"
        anothervoice "당연하지. 잠깐 기절한 걸로 어떻게 되지는 않아."
        rine "다행이다..."
        menu:
            "잠깐 산책하고 있었는데, 같이 갈래?":
                main "잠깐 산책하고 있었는데, 같이 갈래?"
                rine "아니, 괜찮아."
                anothervoice "그럼 안녕."
            "뭐하고 있었어?":
                main "뭐하고 있었어?"
                rine "연구...{w=.5}려나?"       
                anothervoice "잘 되가?"
                rine "응!{p=.5}{size=3}평소랑 뭔가 다른데...{/size}{p=.5}너는 뭐해?"
                anothervoice "잠깐 산책."
                rine "그럼 잘가!"
                anothervoice "응. 열심히 해!"
                $rine_mis+=3
        hide rine_nom
        scene bg_middle with dissolve        
        play sound "walk_slow.mp3"
        $renpy.pause(1.5)
        "성공적으로 넘긴건가.{p=.5}조금 불안했지만 문제는 없어 보인다."
        play sound "walk_slow.mp3"
        "그대로 몸을 돌려 계단을 내려갔다."
        $renpy.pause(2.0)
        scene bg_inschool with dissolve
        "여기가 운동장인가."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        "퍼석이는 흙이 운동화를 더럽힌다.{p=.5}아니, 더럽히려 했다."
        "흙과, 물과, 피로 더럽혀지고 불에 그을려 형태를 유지하는 것 자체가 신기할 정도인 이 운동화에 약간의 흙이 만든 얼룩은 티 조차 나지 않았다."
        play sound "sandwalk.mp3"
        "자박거리며 갈라지고, 부서지는 흙의 소리."
        $renpy.pause(6.0)
        "흙에 운동화의 자국이 남았다.{p=.5}미묘하게 물기가 남아있는 흙.{p=.5}내가 \'저쪽\'에 있는 동안 비라도 내렸던 걸까."
        anothervoice "그러고보니 오늘이 무슨 요일인지도 모르네..."
        "하지만 중요한 일은 아니다."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        "탁한 공기의 냄새"
        "그대로이다."
        show guard_nom at right with dissolve
        "이스프킨이란 이름의 떠돌이이다."
        guard "{size=10}죽었다 살아난 사람이면 좀 더 새로이 주어진 기회에 감사하며 살아가면 되는데 ... 왜 굳이 피곤하게 사는걸까.{/size}"
        anothervoice "네?"
        guard "오, [main]. 몸은 좀 괜찮아?"
        anothervoice "네. 이제 괜찮아졌어요."
        guard '다행이네. 그래도 너무 무리는 하지 말고.'
        hide guard_nom
        play sound "walk_slow.mp3"
        "중얼거리며 사라지는 이스프킨."
        $renpy.pause(2.0)
        "감회에 젖어있는 것은 여기까지이다."
        "어서 검의 회수를 서두르지 않으면 약속을 지킬 수 없게 되어버린다.{p=.5}운이 좋게도 \'궤\'는 지금 나의 손에 있다.{p=.5}후딱 끝내버리고 원래대로 돌려놓자."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_black with wiperight
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        nvlnarr "사랑. 인간은 누군가를 사랑하기에 약해진다.\n\n-가장 쓸모 없는 감정에 대한 물음에 돌아온 린의 대답.-"
        scene bg_teacher with wipeleft
        play sound "sliding.mp3"
        scene bg_teacher 
        $renpy.pause(1.5)
        anothervoice "저... 선생님?"
        show read_nom at right with dissolve    
        teacher "[main] 양이군요. 움직여도 괜찮은가요?"
        main "멀쩡해요."
        teacher "왜 오신 지 용건을 물어봐도 될까요?"
        main "선생님은 \'다섯 개의 검\'이라는 이야기를 아시나요?"
        teacher "아, 알고 있습니다. 당신의 검인 \'궤\' 역시 그 중 하나이죠."
        main "네. 그... 나머지 검들에 대한 기록된 책 같은 걸 얻을 수 없을까요?"
        teacher "찾아보면 몇 개 나올 것 같지만서도... 왜 그러시죠?"
        main "이스프킨 때문에요."
        teacher "호오... 그건 무슨 뜻이죠?"
        main "그녀에게선 \'냄새\'가 나요."
        teacher "......."
        "그의 눈이 날카로워졌다."
        teacher "......."
        main "........"
        teacher "냄새, 인가요..."
        main "네."
        teacher "무슨 냄새였죠?"
        main "피와 살육과 증오의 냄새.{p=.5}저와 같은 냄새가 났어요. 정상적으로 살아온 사람이라면 절대 풍길 수 없는 냄새죠."
        teacher "지금 같은 시대에 과연 정상적으로 사는 사람이 있을까요?"
        main "안톤. 살인과 살육은 다릅니다. 그 사람은 살인자가 아니에요."
        main "그런 사람이 어떻게 당신과 알고 있는 거죠?"
        teacher "비밀입니다." 
        "비밀... 인가.{w=.5} 확실히 선뜻 말해 줄 만한 일은 아니겠지.{p=.5}어떻게 할까?"        
        #$renpy.fix_rollback()        
        call anton_dia from _call_anton_dia        
        main "그러면 그 이야기는 그만하겠습니다."
        teacher "예, 아무튼 이스프킨 때문에 \'다섯 개의 검\'에 대한 관심이 생겼다고요?"
        main "네. 그 냄새를 맡고 그녀가 등에 지고 있는 것을 다시 보았을 떄 깨달았어요.{p=.5}진품인지 아닌지는 모르겠지만 \'아\'와 비슷하게 생겼더군요."                
        teacher "그건 복제품입니다."
        main "제 \'신편\'의 능력을 기억하시나요?"
        teacher "\'이야기를 듣는다\'. {w=.5}음, 그렇군요."
        main "그 검의 이야기는 저를 아찔하게 만들 정도였습니다.{p=.5}저는 진품이라고 생각했지만 복제품이면서도 그 정도의 힘을 낼 수 있다면, 제 것은 얼마나 큰 힘을 내 줄까요."
        teacher "요컨대 알지 못하는 사용법이 있을지 모르니 검에 대해 자세히 기록된 자료를 읽어보고 싶다는 것이군요."
        main "예."
        teacher "알겠습니다. 찾아 보도록 하죠."
        window hide 
        $renpy.pause(1.5)  
        scene bg_black with dissolve
        show chapter2 with dissolve
        $renpy.pause(1.5)
        hide chapter2 with dissolve
        nvlnarr "그것은 오뉴월에 내리는 눈이었다.{p=.5}온 세상을 순백으로 물들이고, 물들이고, 물들여 곧 시야를 전부 가려냈다."
        nvl clear
        hide window 
        "CV-01" "어쩌시겠습니까?"
        "의장" "음..."
        "CV-01" "시간이 없습니다. 이번에는 다행히 사람 몇 명 죽은 것으로 끝났지만 다음 번엔 어떻게 될 지 모릅니다."
        "의장" "이스프킨... 그 녀석만 없어진다면..."
        "CV-01" "죽이면 되지 않습니까."
        "의장" "소용없어. 죽여봤자 다른 이들이 되살릴거야."
        "CV-02" "학교를 무너뜨립시다."
        "의장" "학교를?"
        "CV-02" "예."
        "의장" "물론 가능하겠지. 하지만 너도 알고 있겠지? 자원은 한정되있어. 무혈로써 승리하는 것은 불가능하더라도 소비하는 자원을 최소화 해야만 해."
        "CV-02" "꼭 물리적으로 치는 것 만이 승리로 향하는 방법은 아닙니다. 제가 무혈 승리를 쟁취해 보이겠습니다."
        "CV-01" "거짓말!"
        "CV-02" "학교라는 것은 본디 관리자들을 보호하기 위해 만들어진 곳. 저들이 찬양해 마지않는 \'첫번째 조커\'가 이루어낸 업적입니다."
        "CV-01" "더 이상 들을 가-"
        "의장" "닥쳐라. 계속해 보도록."
        "CV-02" "다행이도 이번 조커는 우리가 확보했지 않습니까? 그것을 이용하는 겁니다.{p=.5}\'그 녀석\'을 보냅시다. 그에게."
        play sound "jab.mp3"
        scene bg_room with vpunch
        anothervoice "꿈인가..."
        "무명.{p=.5}그녀를 죽이려 한 이이자, 그녀의 멘토이자, 그녀의 어머니."
        "나는 일어섰다."
        seng "유치한 가면 무도회에 어울려 주는 것도 한계가 있어."
        anothervoice "...이 몸을 빌리는 건 이번 달 말일까지야."
        seng "왜?"
        anothervoice "너는 믿지 않겠지만 [main]을 위해서야.{p=.5}그녀가 할 수 없는 일들을 대신 하기 위해서 몸을 빌린 것 뿐이야."
        seng "물론 믿지 않을거야."
        "나는 어께를 으쓱였다."
        play sound "walk_slow.mp3"
        scene bg_hallway
        show read_nom at right 
        with dissolve
        teacher "[main] 양. 최대한 자료를 모아왔습니다."
        "그의 손에 들려 있는 박스 안에는 작은 수첩과 공책, 몇몇개의 책.{p=.5}나는 그것을 수령했다."
        play sound "walk_slow.mp3"
        scene bg_top with dissolve
        "구할 수 있는 것 중에서 축척이 가장 큰 지도와, 컴퍼스, 자. 자료들."
        play sound "pen.mp3"
        "계산했다."
        play sound "pen.mp3"
        "특정했다.{p=.5}나머지 검들이 있을 만한 곳을."
        anothervoice "음..."
        "이것은 무명의 발자취를 쫒는 일이다.{w=.5}나의 입장이 아닌 무명의 입장에서 생각해야만 한다."        
        anothervoice "...역시 여긴가..."
        "\'재액의 화당\'. 누군가 고의로 깎은 것 마냥 날카로운 절벽과 꺼지지 않는 불꽃들과 객귀들이 있는 곳."
        "\'내려갈 때 열 명, 바닥에서 다섯 명 다시 올라오면 한 명\'.{p=.5}정신적으로나 육체적으로나 지치는 원정이다. 거기까지 가는 것으로도 일이겠지."
        anothervoice "준비에 들일 수 있는 시간이 부족해... 최대한 빨리 끝내야 하는데..."
        "혼자서 가는 것은 당연히 불가능하다. 최소한 네 명은 움직여야 한다. 성과 리네의 손을 빌린다 해도..."
        "이스프킨은 데려가는 것은 위험하다. 최근의 그녀는 모르겠지만 그녀의 과거를 아는 입장에서 그녀의 도움을 바라는 것은 최소한의 양심을 파는 행위이다."
        ".......{w=.5}손이 부족하다. 그녀는 내가 돌아왔는 지 모르고 있을 것이다. 그렇다면 여기서 내가 그녀와 손을 잡는다 하여도 나를 비난하는 사람은 없을 것이다."
        "...비난할 사람이 남아 있다면, 이지만."
        "내게 그걸 결론지을 권리가 있을까?"
        "그녀가 죄를 지은 사람은 내가 아닌 그녀들, 이미 죽어버린 그녀들인데."
        "나는, 그녀의 죄를 덮고서 그녀를 이용할 수 있나?"
        "아니, 없다. 나에게는 그것을 결정할 권리가 없다."
        "...{w=.5}...{w=.5}...{w=.5}..."
        "나는 일어섰다."
        "길의 안전을 확인하는 파수가 둘. 싸우기 위한 사람이 하나. 그리고 짐을 들 사람 하나.{p=.5}최소 네 명이다. 이 수를 채우지 않고 가는 것은 죽여달라고 사정하는 것과 다를 바 없다."
        "나머지 한 명을 구해야한다."
        "...하지만, 어떻게?"
        scene bg_black with dissolve
        $firstcurious=None
        $secondcurious=None
        $thirdcurious=None        
        $thirditem=None
        $forthitem=None
        "나는, 잠에서, 깼다."
        scene bg_floor 
        with irisout
        guard "......."
        "일어나지 않고서 천장을 바라보았다."
        "......."
        guard "아아..."
        "어쨌든 일어나야만 하겠지."
        play sound "blanket.wav"
        $renpy.pause(2.0)       
        scene bg_room with dissolve
        "덥고 건조한 날씨다.{p=.5}불 바로 옆에 있기에 당연하다면 당연한 일이지만 익숙해 질 수는 없었다."
        guard "......."
        "머리맡에 놓여 있던 약을 집어들었다."
        #play sound "medicine.wav"
        $renpy.pause(6.0)
        "물 없이 삼켰다.{p=.5}쓴 맛의 여운이 혀에 남았다."
        "밖으로는 여전히 작열하는 불꽃만이 보인다."
        "안톤을 제외하고는 찾는 사람 하나 없는 고독한 이 땅.{p=.5}\'외로움\'을 느끼지 못한다고 한다면 거짓말이 되겠지.{p=.5}그러나 약속은 약속. 이곳을 지키는 것은 나의 의무이다." 
        play sound "walk_slow.mp3"
        "발소리."
        $renpy.pause(2.0)
        guard "무엇을 얻기 위해 왔느냐, 무엇을 잃기 위해 왔느냐. 그대는 안톤인가?"
        anothervoice "...아니요."
        "일전에 안톤에 부탁으로 그와 동했을 때 있었던 아이의 목소리다."
        guard "불꽃과 아픔의 대지에 찾아온 생명이여. 그대의 이름은 [main] 인가?"
        anothervoice "...네."
        guard "생명이여. 이곳에 존재하기 위한 대가를 알고 있는가?"
        anothervoice "알고 있습니다."
        guard "좋다. 그대가 나에게 향하는 것을 허락하겠노라."
        "길잡이를 보냈다."
        scene bg_black with dissolve
        $renpy.pause(4.0)
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        play sound "door.mp3"
        $renpy.pause(2.0)
        scene bg_room
        show guard_nom
        with dissolve
        guard "음?"
        anothervoice "왜 그러시죠?"
        play sound "sword.mp3"
        guard "너는 다른 아이구나."
        anothervoice "네? 무슨 뜻이죠?"
        guard "속일 생각 하지 마."
        anothervoice "...{w=.5}역시 관리자는 관리자라는 건가."
        guard "자, 그럼 하나 묻겠어.{p=.5}너는 누구지?"
        anothervoice "내 이름은 Ψ{rt}한{/rt}. [main]의 신편이지."
        guard ".......{w=.5}... 그녀는 어떻게 했어?" 
        anothervoice "아, 걱정하지 마. 지금 몸 속 어딘가에서 그 동안 취하지 못했던 휴식을 취하고 있을 뿐이야."
        guard "왜... 이제 와서야 나타난 거야?"
        anothervoice "나라고 좋아해서 네게 협력을 요구하는게 아니야.{p=.5}그날 죽어버린 동료들을 생각한다면... 아직도 피가 끓지만..."
        guard "안톤이 내게 어떤 \'가능성\'에 대해서 말한 적 있어.{p=.5}그때는 그냥 웃어 넘겼지만..."
        anothervoice "안톤이 하는 말은 언제나 옳았지."
        guard "그때 너까지 죽였어야 했어."
        anothervoice "개탄해 봤자 바뀌지 않아."
        guard "제기랄."
        anothervoice "내가 원하는 건 간단해. 힘을 빌려줘."
        guard "원수에게 손을 내밀다니, 그 고귀하던 한은 어디로 갔지?"
        play sound "jab.mp3"
        extend "{p=.5}...뭐, 좋아. 한 번 들어볼까."
        anothervoice "재액의 회당으로 갈 거야."
        guard "흠. 아마 네가 파수일 거고, 나는 싸움꾼... 나머지 둘은?"
        anothervoice "[main]의 친구들을 데려갈 거야."
        guard "너답지 않게 훌륭한 선택인걸. 확실히 그 둘이라면 나보다 더 믿음직하겠지."
        anothervoice "어떻게 할래."
        guard "내가 무슨 말을 할 지 너도 알고 있잖아?"
        anothervoice ".......{w=.5}...뭘 원해?"
        guard "네 컴퓨터의 암호."
        $firstcurious = "이스프킨이 내 컴퓨터 암호를 원하는 이유가 뭐지?"
        anothervoice "뭐야, 그걸 아직도 들고 있었어?"
        guard "뭘 어떻게 해도 열리지 않아서 말이야."
        anothervoice "네가 나한테 진 빚을 잊진 않았겠지."
        guard "잊었어."
        play sound "jab.mp3"
        "어떤 말을 입에 담아도, 어떤 말을 들어도. 어떤 행동을 취해도. 어떤 행동을 당해도. 그리고 그 끝에서도.{w=.5} 이스프킨의 표정이 바뀌는 일은 없었다."
        "안타슈프라인. 썩은 불꽃의 잔재. {w=.5}안톤에게 \'구조\'되기 전의 그녀는 피찬{rt}린{/rt}왕. 인간이 아닌 그 언저리의 무엇인가였다.{p=.5}살아가는 것이 아닌 생존하고 있었던, 오히려 스스로의 죽음조차 바랬던 무언가."
        "나는 그녀를 좋게 볼 수 없었다. {p=.5}0에서 부터 모든 것을 타의로 수행한, 그리고 그 결과 죽음을 두 번 넘어선 자의 이야기를.{p=.5}내 동료들을 학살했기 때문만이 아닌, 한때 숨쉬던 생명이 다른 생명에게 가진 경멸감으로써."
        "멸{rt}분{/rt}시{rt}노{/rt} 했고, 죽{rt}구{/rt}이{rt}하{/rt}려 했다. 그리고 실제로 성공했었다. {w=.5}성공했어야만 했다."
        guard "암호만 넘겨준다면 나는 일이 끝날 때까지는 네 말에 따르겠어.{w=.5} 물론 암호 먼저."
        anothervoice "...{w=.5}자랑스런 우리의 꿈."
        guard ".......{p=.5}.......{p=.5}.......{p=.5}...{w=.5}멍청이."
        "어께를 으쓱였다."
        nvl clear
        window show
        nvlnarr "\'꿈\': 사람의 기저에 서식하며 사고와 행동을 제어하는 천성."
        nvl clear
        window hide
        guard "꼭... 그렇게까지..."
        anothervoice "네가 지은 죄의 무게를 조금은 알게 되었길 빌겠어."
        guard "고작 이런 걸로 마음을 바꾸진 않아."
        anothervoice "두고 보면 알게 되겠지."
        show continued2 with dissolve
        scene bg_black with dissolve
        nvl clear
        window show
        nvlnarr "먼 옛날. 이 세상에 아직 \'신님\'이 남아있던 시절에. 별들은 손을 뻗으면 닿을 곳에 있었습니다.{p=.5}낮 동안 햇빛에 삶아지고 밤 동안 달빛에 얼려지는 것을 참다 못한 사람들은 가장 높은 산 꼭대기의 신님을 찾아갔답니다.\n\n\n\n돌맹이 왕자님 이야기 - 작자 미상"
        window hide
        scene bg_hallway
        show seng_nom at left
        show rine_nom at right
        with dissolve
        anothervoice "그래서..."
        rine "나는 상관 없을 것 같은데."
        seng "나도 상관 없어."
        anothervoice "고마워."
        seng "...{w=.5}괜찮아. \'우리\' 사이니까."
        "성과 리네를 설득하는데 성공했다.{w=.5}여장을 꾸려 길을 떠날 채비만 마치면 된다."
        rine "이스프킨이랑 어디서 합류할 거야?"
        anothervoice "제2 정거장 앞에서."
        seng "정거장까지 나가는 건... 학교에 도착하기 전 잠깐 떠돌이 생활을 했을 때 이후로 처음인걸."
        "[main]의 기억을 뒤졌다.{w=.5}생존자 구조를 위한 3차 구조대에 의해 발견되어 거두어지기 전까지, 성은 황폐화 된 도시들을 전전하며 살아왔다."
        anothervoice "교장과 안톤에게도 허락을 구해 놨어. 준비가 끝나는 대로 바로 출발하자."
        "{color=#DF0101}리네{/color}{color=#FFFFFF},{/color} {color=#91ff6d}성{/color}" "그래."
        scene bg_black with dissolve
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        stop sound
        scene bg_schooldoor with dissolve
        "공무를 위한 외출이 아닌 학생 개인의 현장 답사.{p=.5}당연하게도 버스 대절 허가가 나올 리 없었다."
        rine "나가면 두세달은 못 돌아오겠네."
        anothervoice "짐은 확실히 챙겼어?"
        seng "...챙겼어. 가자. 지체해서 좋을 일은 없어."
        "교문 밖으로 나서기 전, 학교의 영역을 알리는 돌을 세번 건드리고 가볍게 기도했다."
        anothervoice "...우리들을 품어주시는 주, 하늘에 계신 아버지. 모든 힘과, 모든 영광과, 국가를 당신께.{p=.5}저희 모두를 진심으로 가호해 주소서."
        scene bg_black with dissolve
        $renpy.transition(Dissolve(3.0))
        show screen muzlet(temp="3주 후")
        $renpy.pause(6.0)
        $renpy.transition(Dissolve(3.0))
        hide screen muzlet        
        $renpy.pause(3.0)
        hide curious_button
        scene bg_black
        with dissolve
        nameless "....... {w=.5}....... {w=.5}...성부와 성좌와 성령의 이름으로, 아멘. 성 요셉, 존체의 정배 성 마리아와 함께 저희를 위해 기도하시고, 저희들로 하여금 천주님 자비 속에 있다는 것을 알게 하소서."
        play first "shotgun.mp3"
        show cg_blood_2 at sizeing1 with vpunch
        "얼굴에 피가 튀었다."
        $renpy.pause(2.0)
        scene bg_black with dissolve
        "문질러 닦았다."
        "어째서 이렇게 되었을까."
        nameless "구세주 예수 그리스도, 우리들은 주를 믿으며, 소원하니. 영원히 두려워 할 것 없으라."
        "눈을 감겨주었다."
        nameless "깨지 않는 영원한 안식을,\'어{rt}환{/rt}긋{rt}상{/rt}난{rt}기{/rt} 꿈{rt}행{/rt}\'이여."
        "한 여인이 잠들었다. {w=.5}나의 인간성이 잘려나간다."
        nameless "큭..."
        show daruma_kickimage        
        $renpy.pause(3.0)
        "심장이 움츠러든다."
        nameless "[main]..."
        "[main]. 소라빛 소녀... {w=.5}나는 그 녀석을 위해 되돌아왔다.{p=.5}내 심장을 터뜨린 구슬들과, 내 양 눈을 꿰어버린 검을 넘어서."
        $renpy.music.play('heartbeat.mp3', 'second')    
        $renpy.music.set_volume(3.0, channel='second')
        $renpy.pause(4.0)
    #  $renpy.music.stop('heart', None)
        $renpy.music.stop('second')
        nameless "...후..."
        scene bg_black with dissolve
        "가라앉았다. {w=.5}기적과도 같이.{p=.5}이 몸도 얼마 가지 않아 붕괴될 것이다. {w=.5}그렇게 되면... {p=.5}의장의 말은 정확하다. {w=.5}그 녀석은 이리로, 반드시 올 것이다."
        play sound "walk_slow.mp3"
        "누군가 다가오고 있다."
        $renpy.pause(2.0)
        stop sound
        "[main]의 것은 아니다."
        "심호흡과 함께 임전 태세를 갖추었다."
        er "쏘지 마십시오. 접니다."
        nameless "...어떻게 됐어?"
        er "그 늬들의 모습을 확인했습니다. 빨간 머리 하나, 검은 머리 하나."
        nameless "수고했어."
        er "그럼 가 봐도 됩니까?"
        nameless "아니, 너는 여기서 나와 함꼐 녀석들을 기다려야지. 이들은?"
        er "먼저 돌아갔습니다."
        "대기했다."
        play sound "walk_slow.mp3"
        scene bg_vally 
        show seng_nom at right
        with dissolve
        $renpy.pause(2.0)
        stop sound
        "\'성\'이었다."
        nameless "여, 성."
        hide seng_nom
        show seng_ang at right
        seng "...너는..."
        nameless "뭐야, 그 귀신을 보기라도 한 것 같은 표정은."
        seng "말도 안 돼... 너는 죽었잖아... 분명... 죽였을 텐데..."
        nameless "죽었었어. 지금은 아니지만."
        play sound "drawning.wav"
        $renpy.pause(1.3)
        stop sound
        nameless "고작 검으로 상대가 되겠어?"
        seng "...길고... 짦은 건... 대 봐야 하는 법이야."
        nameless "그거야 기량이 비슷할 때 이야기지."
        play sound "shotgun.mp3"
        seng "큭..."
        stop sound
        play sound "blooding.mp3"
        show seng_supred at right with Dissolve(3.0)
        stop sound
        hide seng_ang
        play sound "collapse.ogg"
        hide seng_supred with wipedown
        seng "이봐... 마지막으로 할 말...이 있어..."
        nameless "해 봐. 네 묏자리에 새겨주지."
        seng "...지금... [main]... 신편한...테..."
        nameless "신편이라고?"
        seng "신...편의 이름은... \'한\'..."
        nameless "......."
        play sound "bone_break.mp3"
        $renpy.pause(7.0)
        "짓밟아 뼈를 부러뜨렸다."
        stop sound
        er "불쌍한 녀석. {w=.5}죽인 건가요?"
        nameless "아니, 계획 변경이야. 자리를 바꾼다. 한...이라면 분명 정상까지 오겠지."
        er "한이 누군가요?"
        nameless "...너희들은 모르는 사람의 이름.."
        er "사람이라니요? 분명 신-"
        nameless "시간이 흐르면 알게 될 일이야. 기다려. 알아봤자 좋은 건 아니니까."
        er "분부대로."
        play sound "walk_slow.mp3"
        $renpy.pause(2.0)
        scene bg_black with dissolve
        play sound "walk_slow.mp3"
        nvl clear
        nvlnarr "무. 시간은 공간을 창조했고, 공간은 별을 낳았으며, 별은 갖은 추악함을 잉태했다."
        nvl clear
        hide window
        scene bg_mountop
        show rine_ang
        show bad_nom at right
        with dissolve
        anothervoice "......." 
        er "오랜만이군요."
        "....... {w=.5}지난 번 습격 때 무리 속에 끼어 있던 이."
        rine "너는... 누구야?"
        er "묻는다는게 그건가요... 뭐, 상관없겠죠.{w=.5} 제 이름은 에르. 사정이 있어 이곳에서 당신들을 기다리고 있었습니다."
        anothervoice "우리를?"
        er "저와 함께 가시겠습니까? 제 주인께서 당신들과 만나고 싶어 합니다."
        menu :
            "순순히 따른다.":
                "별 다른 의도는 없을 듯 했다. 또한, 이 몸의 주인이 나인 이상 상처입힐 수 있는 이는 극히 한정된다."
                anothervoice "가자."
                rine ".......{w=.5} ...그래."
            "저항한다":
                anothervoice "거절하겠어."
                er ".......{w=.5}정말로요?"
                rine "에르...라고 했지?"
                er "그렇습니다만?"
                rine "성은 어디에 있지?"
                er "무슨 뜻으로 하신 말씀인지 모르겠습니다만."
                rine "쓸데없이 빙빙 돌려 말하려고 하지 마. 산등성이에 있던 핏자국... 그 피는 분명 성의 거야. 그것을 쫒아 올라왔을 때 나온 것이 너라면. 달리 범인이 있을까?"
                er "하하... 설마 그 피를 맛보기라도 한 건가요?"
                rine "굳이 그럴 것까지도 없어. 지금 네 몸에서 성의 냄새가 진동을 하니까."
                er "...이래서 눈치빠른 꼬맹이는 싫다니까...려나요. 뭐, 그렇습니다. 성은 제가 섬기고 있는 분의 공격을 받아 기절한 후 끌려갔습니다.{p=.5}되찾고 싶다면 따라 오시죠."
        play sound "walk_slow.mp3"    
        $renpy.pause(2.0)
        stop sound
        scene bg_nameless
        show rine_nom at right
        show bad_nom at left
        with dissolve
        nameless "아주 잘 해 줬어, 에르."
        er "감사합니다."
        "이 목소리는..."
        play sound "walk_slow.mp3"
        show nameless_nom at center with dissolve
        nameless "오랜만이야, [main]."
        play sound "heartbeat.mp3"
        "......."
        "몸을 되찾으려 날뛰었다."
        $renpy.pause(2.0)
        "짓누르는 것은 어렵지 않았다."
        rine "....... {w=.5}죽지 않았던 건가요..."
        nameless "글쎄. {w=.5} [main]. 나와 단 둘이 할 이야기가 있지 않아?"
        anothervoice "......."
        "저 녀석... 알고 있는 건가?"
        anothervoice "그럴지도 모르겠군요. 리네, 잠깐만 자리를 피해줄 수 있을까?" 
        rine ".......{w=.5} 알았어. 에르...라고 했던가요. 당신도 따라오시죠."
        er "좋을대로."
        play sound "walk_slow.mp3"
        hide rine_nom 
        hide bad_nom
        $renpy.pause(2.0)
        stop sound
        nameless "이게 몇 년 만이야."
        anothervoice "만나고 싶지 않았어요."
        nameless "그래... 나도 만나고 싶지 않았어."
        anothervoice "그렇다면 저를 왜 불러낸 거죠?"
        nameless "\'너\'랑은 말이지."
        anothervoice "예?"
        nameless "바른대로 말해. [main], 어디갔어?"
        anothervoice "......."
        nameless "이 총, 익숙하지?"
        anothervoice "그 녀석은 지금 제 안에 있어요."
        nameless "몸을 빼앗기다니, 답지 않은걸."
        anothervoice "붕괴된 건 아니에요. 그 인격은 아직 살아남은 채 지금도 당신과 이야기 하기 위해 발버둥 치고 있으니까요."
        nameless "강제로 뺏었다는 뜻이야?"
        anothervoice "녀석의 붕괴도가 위험수치를 넘었어요. 저는 그 녀석을 보호하기 위해 어쩔 수 없는 선택을 한 거라고요."
        nameless "좋아. 그럼 지금 당장 녀석을 해방해."
        anothervoice "제 말, 안 듣고 계신 건가요?"
        nameless "그런게 아냐. 죽음조차 거슬렀는데, 고작 신의 은총 하나 못 거스를까 봐?"
        anothervoice "...붕괴도를 줄일 확실한 방법이라도 있나요?"
        nameless "있어. 나와 [main]. 그 둘이기에 가능한게."
        anothervoice "......."
        "심호흡을 했다."
        anothervoice "....... {w=.5}....... {w=.5}......."
        main "....... {w=.5}....... {w=.5}......."
        nameless "[main]."
        main "나...는... [anothervoice]? [main]? {color=#FF0000}{b}나는...{/b}{/color}"
        play sound "slap.ogg"
        "따귀를 맏았다."
        $renpy.pause(1.0)
        main ".......{w=.5} [nameless]...?"
        nameless "그래, 나야."
        main "여긴... 큭..."
        scene bg_nameless
        show nameless_nom
        with pixellate
        nameless "정신 차려, [main]."
        main "[nameless]... {w=.5}[nameless]...?"
        nameless "여러가지 사정이 좀 있어서 말이야."
        "그리운... 목소리..."
        play sound "walk.mp3"
        show guard_nom at left with dissolve
        $renpy.pause(2.0)
        stop sound
        guard "젠장! 한 발 늦었나... [main]! [main]! 들려? [main!]"
        main "이스...프킨..."
        nameless "닥쳐 안타슈프라인."
        guard "물러서! 저 녀석의 말을 들어선 안 돼!" 
        play sound "shotgun.mp3"
        $renpy.music.play('heartbeat.mp3', 'second')    
        hide guard_nom 
        show guard_nomred at left with dissolve
        $renpy.pause(2.0)
        stop sound
        $renpy.music.stop('second')
        hide guard_nomred with wipedown
        "이스...프킨."
        nameless "아아, 의장님. 당신을 사랑합니다."
        play sound "shotgun.mp3"
        main "......."
        $renpy.pause(2.0)
        "손을 복부로 뻗었다.{p=.5}묻어나오는 진홍빛 액체. 틀림없는 피였다."
        "무슨 일이 일어난 것인가 이해할 수 없었다."
        rine "{color=#FF0000}{b}[main]──────────!{/b}{/color}"
        scene bg_black with Dissolve(4.0)
        $renpy.pause(4.0)
        play sound "collapse.ogg"
        $renpy.pause(1.0)
        stop sound
        play sound "shotgun.mp3"
        rine "큭..."
        play sound "walk.mp3"
        er "리네를 제압했습니다."
        nameless "월척이군. 돌아가자. 의장께서 아주 좋아하실 거야."
        main "...어째서..."
        anothervoice "......."
        scene bg_namelessG 
        show nameless_gray
        with Dissolve(4.0)
        play sound "drawning.wav"
        $renpy.pause(1.3)
        stop sound
        play sound "stab.ogg"
        $renpy.pause(1.0)
        "검이 [nameless]의 등허리를 뀄다."
        "피는 흐르지 않는다."
        nameless "......."
        anothervoice "....... {w=.5}...?"
        nameless "죽지 않은 이에게 혈액 따위... 남아있을 리 없잖아?"
        play sound "punch.wav"
        "정권."
        stop sound
        "버텨냈다."
        play sound "mamiru.mp3"
        $renpy.pause(.5)
        stop sound
        "휘둘렀다."
        show nameless_mamiru 
        hide nameless_gray
        nameless "......."
        "그녀는 아무 말 없이 바닥에 떨어진 목을 주워들었다."
        hide nameless_mamiru    
        show nameless_gray
        nameless "[anothervoice]."
        anothervoice "...젠장."
        nameless "한 번. 봐주겠어."
        anothervoice "......."
        nameless "내가 있는 곳은 중앙의회. 어디에 있는 것인가, 너라면 알 수 있겠지."
        play sound "blooding.mp3"
        "가시가 나를 옭아맸다."
        stop sound
        nameless "네 친구들은 내가 데려가겠어."
        anothervoice "그건!"
        play sound "blooding.mp3"
        anothervoice "아아아아아악!!!!"
        nameless "가만히 기다리는 것은 지루하지. {w=.5}시간 제한이라도 한 번 걸어볼까. {w=5}50시간을 주겠어. 네 숙주의 친구들을 구하고 싶다면... 그 안에 찾아오라고."
        anothervoice "잠깐! 마지막으로 하나만 알려주세요!"
        nameless "뭐야?"
        anothervoice "당신은 어째서... [main], 당신에게 가장 소중할 사람을 죽이려 하는 거죠?"
        nameless "죽이려 하는게 아니야. 나는... {w=.5}흠. 이것 또한 시간이 지나면 알 수 있겠지. 나중에 보자고."
        play sound "unsummon.mp3"
        scene bg_black with dissolve
        "인격을 점검했다."
        stop sound
        anothervoice "......."
        "맥동이 끊겨있다."
        "미세한 호흡, 눈을 감은 채 심층의식 한 켠 자신의 전당에 수감된 채 잠든 [main]."
        "저 총, 프레{rt}먹{/rt}데{rt}는 자{/rt}토레라면 [main] 같은 복합 인격체의 생명을 끊는 것 정도는 일도 아닐 것이다.{p=.5}죽이지 않고 굳이 치명상을 입혀 인격을 봉인했다는 것은... 어쩌면 저 말이 사실일지도 모르겠다."
        anothervoice "으으..."
        play sound "blooding.mp3"
        "가슴을 꿰뚫은 가시들을 억지로 뽑아냈다."
        stop sound
        er "가만히 계세요. 지금 치료해 드릴테니까."
        $firstcurious = "[nameless]의 저의는 뭘까?"
        $renpy.pause(3.0)
        prin "계약도 어기고 멋대로 바깥으로 나서더니 꼴 좋군."
        teacher "제 잘못입니다. 이스프킨과 함께라면 괜찮을 거라 생각했던 제 안일함 때문에..."
        prin "넌 옛날에도 지금도 사람이 너무 좋아. 네 잘못이 아닌 것까지 뒤집어 쓰려 하면 나는 미뤄두었던 판결을 지금 선고할 수 밖에 없어."
        "목소리."
        anothervoice "으음..."
        scene bg_prin
        show prin_nom at left
        show read_nom at center
        with irisout
        teacher "[main]! 정신이 들었습니까?"
        "안톤. 교장실. 기절해 있는 사이 학교로 옮겨진 모양이었다."
        anothervoice "성과 리네가... 그리고... 이스프킨..."
        prin "넌 지금 네 몸 상태가 어떤 지도 모르지?"
        "일어서려 했다."
        anothervoice "...욱!"
        "온 몸의 혈류가 멈췄다."
        "뻣뻣해지며, 차가워졌다."
        prin "이제 알겠지?"
        "교장이 나를 눕혔다."
        prin "3주. 가만히 쉬고 있어."
        anothervoice "...-"
        prin "네 친구들은 걱정하지 마. 너와 계약에 따라 탐사대를 꾸려 반드시 되찾아 줄 테니까. 은혜 모르는 네녀석들도 이걸로 나한테 복종할 수 밖에 없겠지."
        anothervoice "......."
        "[main], 성. 두 명의 소녀. {w=.5}관리자를 거둔다는 것은 그 힘을 노리는 세아릴 수 없을 습격을 받아내야 한다는 것이다. 그렇기에 그는 자신의 특기인 환술을 통해 두 사람의 몸에 각인을 박아 넣어 몇 예외를 제외하고 둘을 자유롭게 부릴 수 있도록 \'계약\'을 나누었다."
        "그것은 둘을 얽메는 족쇄인 동시에, 모든 악몽과 아픔의 종주가 꾸민 간계로부터 암흑을 걷어내는 보루의 열쇠."
        anothervoice "제 스승...이자 납치범인 [nameless]는 중앙의회에 있을 테니 찾아오라 말했어요."
        prin "중앙의회?"
        teacher "그건 이미 오래 전에 해체되었을 텐데요."
        anothervoice "예. \'첫 조커\'가 그곳을 탈출할 때, 의장을 비롯한 열 다섯 명의 간부가 몰살당해 와해되었죠. {w=1.0}그저 이름만 빌려온 것인지, 아니면 옛 영광의 재건을 위해 누군가 의장을 자처했는지는 잘 모르겠습니다만 [nameless]는 분명히 의회라 하였습니다."
        prin "...산문답인가."
        anothervoice "아뇨, 진실은 가까운 곳에 있을 겁니다."
        prin "뭐?"
        anothervoice "류스의 성형 요새 \'왕의 무덤\'. {w=1.0}저는 알 수 있습니다. 그녀가 있을 곳은 거기 뿐이라는 것을."
        prin "비약도 정도가 있다고 생각하지 않아?"
        anothervoice "비약일지도 모르죠.{w=1.0} 하지만 저는 꿰뚫어 볼 수 있습니다. 그곳은 저와 [nameless]가 처음으로 만났던 장소이자 그녀와 작별을 고했던 장소이자, 목이 떨어지고, 피가 흩뿌려짐으로써 저희 둘의 인연이 멈추고, 닫겨 끊긴 장소."
        anothervoice "개선장군으로써의 축배와 만리의 배신자로써의 저주. 들어맞는 곳은 거기 뿐이군요."
        prin "허. 뭐, 상관없어. 조사해야할 구역은 많으니까. 그러나 교장과 관리자 그 둘의 제안과 수긍은 모두 계약. 예측이 빗나갔을 떄의 대가. 확실히 징수하겠어."
        anothervoice "그때가 된다면, 얼마든지."
        "떠든 대가일까. 팔이 저렸다."
        prin "안톤. 저 녀석을 의무실로 치워버려."
        teacher "예. 옮긴 후에 돌아오면 되겠습니까?"
        prin "알아서 해."
        teacher "예. 자, 부축해 드릴테니 아파도 의무실까지만 참아 주십시오."
        "발을 딛었다."
        scene bg_prin 
        show prin_nom at left
        show read_nom at center
        with pixellate
        anothervoice "큭..."
        scene bg_black with Dissolve(6.0)
        "???" "나날 사힌 눗믈의 긑이 왔누나."
        guard "......."
        "???" "꾸믈 헤욤치는 그듸. 므서슬 바라는가."
        scene bg_club_morning 
        show someone_sil 
        with irisout
        seng "스승님?!"  
    # hide someone_sil at center
        if renpy.get_renderer_info()["additive"]:
            show showT at center 
        else:
            show showT2 at center
        with Dissolve(3.0)
        nameless "휘유. 이런 간단한 속임수에 넘어가다니."
        guard "[nameless]...!"
        nameless "진정해. 싸우고 싶지 않으니까."
        guard "닥쳐!"
        play sound "punch.wav"
        "복부에 명중. {w=.5}아파하는 기색조차 없다."
        stop sound
        nameless "네 머릿속에 심리 폭탄을 설치해 놨어. {w=.5}국지적 폭발과 함께 세상을 뜨고 싶지 않으면 가만히 있어."
        play sound "chain.mp3"
        "쇠사슬이 채워졌다."
        stop sound 
        nameless "50시간... 아니, 이제는 40시간이구나. {w=.5}전부 지나가면 네 방 안에 산성 가스가 살포될 거야.{p=.5}빠져나가려고 해도 바깥에는 내 부하들이 가득 깔려있지. 얌전히 구조를 기다리고 있으라고."
        guard "아이들... 리네와 성에게도 똑같은 짓을 한 거야?"
        nameless "당연하지. 나는 공평하니까."
        "반항할 수 없었다. 마법 처리가 완료된 쇠사슬은 물리력으로 끊을 수 없다."
        guard "아이들은 빼!"
        nameless "나한테 무엇인가 요구할 수 있는 상황이 아닐텐데?"
        guard "\'학교\'와 거래하기 위해서라면 나 하나만으로도 충분하잖아!"
        nameless "\'학교\'와 거래하기 위해서가 아니야, 이스프킨.{w=.5} 잘못 짚어도 한참 잘못 짚었어."
        play sound "punch.wav"
        guard "욱!"
        stop sound
        nameless "\'의장\'께서 될 수 있으면 손 대지 말라고 했지만... {w=.5}자비로우신 그분이라면 이 정도 분풀이는 봐 주시겠지."
        play sound "jab.mp3"
        $renpy.pause(1.0)
        stop sound
        play sound "jab.mp3"
        $renpy.pause(1.0)
        stop sound
        play sound "jab.mp3"
        $renpy.pause(1.0)
        stop sound
        scene bg_club_morningB
        show nameless_gray
        with Dissolve(3.0)
        guard "안톤... {w=.5}미안..."
        scene bg_black with dissolve
        play sound "chain.mp3"
        $renpy.pause(2.0)
        stop sound
        $renpy.pause(5.0)
        scene bg_room with irisout
        "잠에서 깨어났다."
        "고요한 방. 선생들과 대부분의 학생들은 [nameless]에게 붙잡힌{p=.5} [main]의 동료들을 구하러 갔으니 당연했다."
        "몸에 문제는 없다."
        teacher "[main]. 지금 즉시 교장실로 와 주십시오. 다시 한 번 말하겠습니다. [main], 지금 즉시 교장실로 와 주세요."
        "안톤의 목소리. 내가 자고 있는 동안 탐사대가 돌아온 것일까?"
        ".......{w=.5} ...교장의 성격 상 그럴 리 없었다."
        play sound "blanket.wav"
        "옷을 입었다."
        $renpy.pause(2.0)
        stop sound
        play sound "door.mp3"
        scene bg_black with dissolve
        $renpy.pause(1.5)
        stop sound
        play sound "walk.mp3"
        $renpy.pause(5.0)
        stop sound
        play sound "walk.mp3"
        scene bg_prin
        show read_nom at right 
        with dissolve
        $renpy.pause(1.5)
        stop sound
        anothervoice "무슨 일인가요, 안톤?"
        read ".......{w=.5} ...당신..."
        anothervoice "안톤...?"
        hide read_nom
        show read_ang at right
        read "역겹군요. 당신에게 그 이름으로 절 부를 자격이 있다고 생각하는겁니까?!"
        ".......{p=.5}눈치 챈 것이 틀림없었다."
        anothervoice "어디까지 알고 있어?"
        hide read_ang
        show read_nom at right.
        read "다 끝났잖습니까... 저희의 이야기는...{p=.5}왜... {w=.5}이제와서 다시 나타난 겁니까, 한?"

    else:
        centered "다시 왔구나?"
        extend "\n음... 너무 강압적이었던 거려나?"
        extend "\n한 번 정도는 괜찮겠지."
        extend "\n이어해도 좋아."
        extend "\n{color=#DF0101}네 이야기를{/color}."
        $emotion="ang"
        $destroy = persistent.destroy
        $equal = persistent.equal
        show screen dest
        "의문의 목소리" "너는 생각했을 것이다."
        main "......."
        "의문의 목소리" "\'내가 도망치는것은 그네들과의 약속을 지키기 위해서\'라고."
        main "......."
        "의문의 목소리" "네 옆에서 죽었다."
        main "......."
        "의문의 목소리" "제일 먼저 네 어머니가."
        play sound "scream.mp3"
        show cg_blood at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        "의문의 목소리" "그 다음으로 네 동생들."
        play sound "scream.mp3"
        show cg_blood2 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        play sound "scream.mp3"
        show cg_blood3 at Position(xpos=renpy.random.randint(100, 600), ypos=renpy.random.randint(0, 1000)) with vpunch
        $renpy.pause(2.0)
        hide window
        show movie
        $renpy.pause(2.0)
        hide movie
        call screen nonreal with dissolve
        return
