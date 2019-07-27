# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.

# First up, we define some simple events for the various actions, that
# are run only if no higher-priority event is about to occur.

init python:
    event("cut", "rine_dia >= 80", event.only(), priority=200)
    #event("check1", "persistent.USB==1")
   # $ event("cut_bad", "rine_dia == -20", priority=210)


label cut:
    rine "...정말이야?"
    main "당연하지.{p}거짓말은 0.1%도 안 섞었어."
    rine "으음..."
    "혼란스러워 보인다.{p}그럴만도 하겠지.{p}자신이 알고 있던 모든 사실들이 바뀌어 버렸으니까."
    "조용히 중얼거리는 그녀."
    rine "{size=4}대체 당신은 무엇을 위해서 절 만들고 이리로 보낸건가요...{/size}"
    main "뭐?"
    rine "아니, 아무것도 아니야."
    "리네는 가볍게 고개를 저었다."
    main "어때, 납득이 돼?"
    rine "납득하고 싶지 않지만... 납득 할 수 밖에 없어 보이네..."
    "그녀에게 상황을 설명하는데 성공한 듯 했다."
    "한숨 돌려도 되려나."

label anton_dia:
    #$renpy.fix_rollback()        
    menu:
        "넘긴다.":
            $renpy.fix_rollback()        
            return

        "계속한다.":
            $renpy.fix_rollback()        

            if anton_miss<=20:
                main "저... 그래도..."
                teacher "그 이야기에 관해서는 더 이상 말 하지 않을겁니다."
                $anton_miss+=1
                call anton_dia from _call_anton_dia_1
            else:
                teacher "당신. 예전보다 훨씬 끈질겨졌군요."
                teacher "제가 알던 사람은 이렇지 않았는데..."
                teacher "지금 당신은 당신이 아닌 것 아닌가요?"
                main "무슨 뜻인지 잘 모르겠는걸요?"
                teacher "노파심에서 하는 말이긴 합니다만... 당신은 관리자입니다. 언제든지 자신이 알지 못하는 사이에 신편에게 몸을 뺴앗길 수도 있어요."
                main "알고 있어요. 알고 있다고요. 하지만 지금은 아니에요."
                teacher "물론 저는 당신을 믿습니다. 당신이 신편에게 질 만큼 약하지 않다는 것을.{p=.5}하지만 만약이라는 것이 있는걸요."
                main "걱정해 주셔서 감사합니다. 하지만 저는 저에요."
                teacher "그러길 간절히 바라고 있습니다..."
    return
label check1:
    "..."
    show seng_nom at right
    "."
    return