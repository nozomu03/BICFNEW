label antoncurous:
    seng "[main]."
    main "그래. 쫒을거야."
    scene bg_black with wiperight
    "우리는 조심스럽게 안톤의 뒤를 밟았다."
    play sound "walk_slow.mp3"
    $renpy.pause(2.0)
    "작은 컨테이너 화장실 안으로 들어간 그.{p=.5}창문으로 조심스럽게 엿보았다."
    scene bg_bathroom 
    show read_nom at right
    with wipeleft
    teacher "좋아... 이제 이것만 넣으면..."
    "그가 무엇인가 만들고 있다."
    main "(저... 저건!)"
    "약학에 자신이 없는 나라 해도 저것이 무엇인지는 분명하게 알 수 있었다."
    seng "달의 잠...? 저게 왜...?"
    main "...분명 달의 잠은..."
    seng "맞아. 죽은 사람을 다시 되살릴 때 쓰는 거지."
    if thirditem!=None:
        main "....왜? 어째서...? {w=.5}아!"
        "뇌를 스치는 충격."
        seng "...?"
        main "나는 가방에서 \'그것\'을 꺼냈다."
        seng "...!!!!"
        main "이스프킨..."
    else:
        "숨을 죽인채 관찰했다."
        teacher "이 일과 관계없는 모든 분들께... {w=.5}미안...합니다... "
        "그는 무언가를 부었다."
        play sound "explosion.mp3"
        scene bg_bathroom at explosion 
        main "큭!"
        seng "지진?"
        "나는 다시 보았다."
        "그는 시체를 끌고 왔다."
        "그... 시체는..."
        show read_nom 
        show guard_nomred 
        with dissolve
        "[main], 성" "이스프킨?"
    seng "이스프킨은... 죽은거야?"
    "이스프킨이... \'죽었다\'?"            
    teacher "이스프킨..."
    main "죽...음...?"
    seng "[main]?"
    main "아... 아..."
    seng "젠장... 이 와중에 스위치가..."
    $destroy+=10
    seng "[main], [main]!"
    $destroy+=10
    seng "하... 이걸 어떻게 해야..."
    "몸이 식어온다."
    "지인의 죽음."
    "목도."
    "잊어야 하는.{p=.5}잊으려 했던.{p=.5}잊었다고 생각한 기억들이 솟는다."
    main "아... 아... 아..."
    $destroy+=10
    seng "[main]. 조금만 참아...!"
    $destroy+=10
    main "아...아..."
    $destroy+=10
    seng "제기랄...!"
    $renpy.transition(vpunch)
    show screen aaaaa
    scene bg_black 
    with vpunch
    seng "[main]!"
    "Black, {w=1.0}Out."
    $renpy.pause(4.0)
    hide screen aaaaa
    call psycopuzzle from _call_psycopuzzle
    $persistent.ok = True
    $persistent.trueR = True
    return

label antonnocurious:
    "안톤은 떠났다."
    seng "후아... 긴장이 풀려서 그런가 어지럽네..."
    play sound "walk_slow.mp3" 
    scene bg_school with dissolve
    "건물 밖."
    stop sound
    main "그러고보니 이스프킨이 안 보이네."
    seng "안톤이랑 같이 가지 않았을까?"
    main "그런가..."
    scene bg_black with dissolve
    "살은 에는 듯한 찬바람."
    "객귀를 정화하기 위한 무기는 시제품 제작 단계에 들어섰다."
    "테스트를 마치고, 개량이 끝난 다음은 양산.{p=.5} 저것이 양산 될 수만 있다면 객귀들을 몰아내고, 인간들은 다시 한 번 학교라는 허울 좋은 감금병동을 벗어나 양지로 나갈 수 있을 것이다."
    $persistent.ok = True
    $persistent.trueR = False
    return