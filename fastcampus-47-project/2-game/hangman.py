import pygame, math, random

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [500, 900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
hint_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 80)
entry_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 60)

# 소숫점을 정수로 변경해주는 함수
def tup_r(tup):
    temp_list = []
    
    for a in tup: 
        temp_list.append(round(a))
        
    return tuple(temp_list)

entry_text = ""
try_num = 0
enter_go = False
drop = False
exit = False

#  A가 영어 단어를 1개 생각한다.
f = open("voca.txt","r",encoding='UTF-8')
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
data_list = data_list[:-1]
while True:
    r_index = random.randrange(0,len(data_list))
    word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
    if len(word) <= 6 :break
word = word.upper()

#  단어의 글자 수만큼 밑줄을 긋는다.
word_show = "_ "*len(word)
try_num = 0
ok_list = []        # 정답 알파벳을 넣는 리스트
no_list = []        # 오답 알파벳을 넣는 리스트

k = 0

# 4. 메인 이벤트
# 반복되는 것들은 여기 안에서 실행됨
while not exit:
    # 4-1. FPS 설정
    clock.tick(60)
    
    # 4-2. 각종 입력 감지
    for event in pygame.event.get(): # 리스트로 반환됨 << 예시로 마우스 키보드 입력이 동시에 일어날 수도 있음
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)   # 키 누른 거 알아내고
            if (key_name == "return" or key_name == "enter") and entry_text != "":
                enter_go = True   
            if len(key_name) == 1:                  # 알파벳 한 글자만 눌렸을 때를 가정
                if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                    entry_text = key_name.upper()   # 아스키코드를 사용하여 영문 대소문자일때 입력을 받되, 출력은 대문자(.upper())로 한다.
                else : entry_text = ""              # 이외의 경우는 빈칸을 넣는다.
            else : entry_text = ""
            
    # 4-3. 입력, 시간에 따른 변화
    k += 1
    
    # 알파벳을 입력하고 엔터를 누를 경우, 알파벳이 문제단어에 있는지 찾는다.
    # 없다면 no_list에 추가하고, 있다면 ok_list에 알파벳을 추가한다.
    # 알파벳이 포함되는 경우, 알파벳을 다음과 같이 보여준다 sc + r + een
    if enter_go == True:
        ans = entry_text
        result = word.find(ans)
        if result == -1 : #없음
            try_num += 1
            no_list.append(ans)
        else : #있음
            ok_list.append(ans)
            for i in range(len(word)):
                if word[i] == ans:
                    word_show = word_show[:i] + ans + word_show[i+1:]
        enter_go = False
        entry_text = ""
    
    # 4-4. 그리기
    screen.fill(black)
    
    # 처형대 그리기
    A = tup_r((0, size[1]*2/3))
    B = (size[0], A[1])
    C = tup_r((size[0]/6, A[1]))
    D = (C[0], C[0])
    E = tup_r((size[0]/2, D[1]))
    
    pygame.draw.line(screen, white, A, B, 3)
    pygame.draw.line(screen, white, C, D, 3)
    pygame.draw.line(screen, white, D, E, 3)
    
    F = tup_r((E[0], E[1]+size[0]/6))
    pygame.draw.line(screen, white, E, F, 3)
    
    # 얼굴 (동그라미) 그리기
    # G는 사람의 모든 좌표와 연결되어 있어서, 사럄이 떨어질 때 이 좌표만 움직이면 된다. 
    if drop == False:
        pygame.draw.line(screen, white, E, F, 3)
    r_head = round(size[0]/12)
    
    # 만약 drop이 True라면, 좌표상으로 떨어질 수 있도록 (+가 내려가는 거임) k를 더해준다
    # k는 while문이 반복될 때마다 (철자를 틀릴 때마다) 1씩 늘어남.
    # k가 점점 커져 P에 영향을 주고, P가 특정 숫자가 되는 순간 drop이 True가 되며 줄이 잘리고 사람이 떨어지는 애니메이션이 발생함.
    if drop == True : G = (F[0],F[1]+r_head+k*10)
    else : G = (F[0],F[1]+r_head)

    # 하나 틀릴 때마다 얼굴 목 팔 다리 ... 이렇게 그리기 위한 코드
    if try_num >= 1 : pygame.draw.circle(screen, white, G, r_head, 3)
    
    # 목 그리기 
    H = (G[0], G[1]+r_head)
    I = (H[0], H[1]+r_head)
    if try_num >= 2 :pygame.draw.line(screen, white, H, I, 3)

        
    # 사선 그리기
    l_arm = r_head*2
    
    J = (I[0]-l_arm*math.cos(30*math.pi/180),
         I[1]+l_arm*math.sin(30*math.pi/180))
    K = (I[0]+l_arm*math.cos(30*math.pi/180),
         I[1]+l_arm*math.sin(30*math.pi/180))
    J = tup_r(J)
    K = tup_r(K)
    if try_num >= 3 :pygame.draw.line(screen, white, I, J, 3)
    if try_num >= 4 :pygame.draw.line(screen, white, I, K, 3)
    
    L = (I[0], I[1]+l_arm)
    if try_num >= 5 :pygame.draw.line(screen, white, I, L, 3)

    l_leg = round(l_arm * 1.5)
    M = (L[0]-l_leg*math.cos(60*math.pi/180),
         L[1]+l_leg*math.sin(60*math.pi/180))
    N = (L[0]+l_leg*math.cos(60*math.pi/180),
         L[1]+l_leg*math.sin(60*math.pi/180))  
    M = tup_r(M)
    N = tup_r(N)  
    if try_num >= 6 :pygame.draw.line(screen, white, L, M, 3)
    if try_num >= 7 :pygame.draw.line(screen, white, L, N, 3)      
    
    # 줄 자르기 위한 빨간 줄 애니메이션 코드
    if drop == False and try_num == 8:
        O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2))
        P = (O[0]+k*2, O[1])
        if P[0] > size[0]/2+size[0]/6 :
            P = tup_r((size[0]/2+size[0]/6, O[1]))
            drop = True
            k = 0
        pygame.draw.line(screen, red, O, P, 3)
    
    # 힌트 표시하기
    # hint_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 80)
    # while문 내에서 외부파일을 계속 불러오면 시스템에 부하를 줄 수 있기에 while문 밖으로 빼 줌
    hint = hint_font.render(word_show, True, white)
    hint_size = hint.get_size()
    hint_pos = tup_r((size[0]/2-hint_size[0]/2, size[1]*5/6-hint_size[1]/2))
    screen.blit(hint, hint_pos)
    
    # 입력창 표시하기
    entry = entry_font.render(entry_text, True, black)
    entry_size = entry.get_size()
    entry_pos = tup_r((size[0]/2-entry_size[0]/2, size[1]*17/18-entry_size[1]/2))
    entry_bg_size = 80
    
    # 입력 텍스트 뒤의 하얀 네모창 만들기 (.rect)
    # 도형은 왼쪽 위 좌표가 필요함 >> 왼쪽위x, 왼쪽위y
    pygame.draw.rect(screen, white, (size[0]/2-entry_bg_size/2, size[1]*17.5/18-entry_bg_size/2
                                     ,entry_bg_size ,entry_bg_size))
    screen.blit(entry, entry_pos)
    
    # 4-5. 업데이트
    pygame.display.flip()
    
pygame.quit()