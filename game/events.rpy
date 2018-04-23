# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.

# First up, we define some simple events for the various actions, that
# are run only if no higher-priority event is about to occur.

init:
    $ event("cut", "rine_dia >= 80", event.only(), priority=200)
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
