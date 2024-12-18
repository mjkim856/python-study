import pygame, math, random

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [500, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HANGMAN")

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)

hint_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
entry_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 60)
no_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
title_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 80)
guide_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
finish_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 30)

sound_bad = pygame.mixer.Sound("bad.ogg")
sound_good = pygame.mixer.Sound("good.ogg")
sound_clock = pygame.mixer.Sound("clock.ogg")
sound_save = pygame.mixer.Sound("save.ogg")
sound_fail = pygame.mixer.Sound("fail.ogg")

sound_bad.set_volume(0.2)
sound_good.set_volume(0.2)
sound_clock.set_volume(0.2)
sound_save.set_volume(0.2)
sound_fail.set_volume(0.2)

# 소숫점을 정수로 변경해주는 함수
def tup_r(tup):
    temp_list = []
    for a in tup: 
        temp_list.append(round(a))
    return tuple(temp_list)

exit = False

while not exit:
    entry_text = ""
    drop = False
    enter_go = False
    ready = False
    game_over = False
    save = False
    play_again = False
    is_cloud = False
    
    k = 0

    # 시작 화면
    sound_save.stop()
    sound_fail.stop()
    
    while not exit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True   
            if event.type == pygame.KEYDOWN:
                ready = True
                key_name = pygame.key.name(event.key)     # 키 누른 거 알아내고
                if (key_name == "return" or key_name == "enter"): 
                    is_cloud = True
        if ready == True: break   
        
        screen.fill(black)
        
        title = title_font.render("HANGMAN", True, white)
        title_size = title.get_size()
        title_pos = tup_r((size[0]/2-title_size[0]/2, size[1]/2-title_size[1]/2))
        screen.blit(title, title_pos)
        
        guide_space = guide_font.render("SPACE to VOCA  ", True, white)
        guide_enter = guide_font.render("ENTER to CLOUD", True, white)
        guide_space_size = guide_space.get_size()
        guide_enter_size = guide_enter.get_size()
        guide_space_pos = tup_r((size[0]/2-guide_space_size[0]/2, size[1]*4/5-guide_space_size[1]/2 - 20))
        guide_enter_pos = tup_r((size[0]/2-guide_enter_size[0]/2, size[1]*4/5-guide_enter_size[1]/2 + 20))
        
        # if pygame.time.get_ticks() % 2000 > 500 :
        # 원래 반짝거렸는데 끔
        screen.blit(guide_space, guide_space_pos)    
        screen.blit(guide_enter, guide_enter_pos)  
             
        pygame.display.flip()
       
    #  영어단어 코드 (스페이스)
    if is_cloud == False:
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
    #  클라우드 단어 (엔터)
    else:
        f = open("cloud.txt","r",encoding='UTF-8')
        raw_data = f.read()
        f.close()
        data_list = raw_data.split("\n")
        data_list = data_list[:-1]

        r_index = random.randrange(0, len(data_list))
        word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[0].upper()
        text = " ".join(data_list[r_index].split()[1:])

    #  단어의 글자 수만큼 밑줄을 긋는다.
    word_show = "?"*len(word)
    text_show = text
    print(text)
    try_num = 0
    ok_list = []        # 정답 알파벳을 넣는 리스트
    no_list = []        # 오답 알파벳을 넣는 리스트
     
    # 4. 메인 이벤트
    sound_clock.play(-1)
    
    # 반복되는 것들은 여기 안에서 실행됨
    while not exit:
        # 4-1. FPS 설정
        clock.tick(60)
        
        # 4-2. 각종 입력 감지
        for event in pygame.event.get(): # 리스트로 반환됨 << 예시로 마우스 키보드 입력이 동시에 일어날 수도 있음
            if event.type == pygame.QUIT:  
                exit = True
            if event.type == pygame.KEYDOWN:
                if drop == False and try_num == 8:        # 실패시 빨간 줄이 그어지는 동안 키 입력 불가하게 함
                    continue
                if game_over == True: play_again = True
                key_name = pygame.key.name(event.key)     # 키 누른 거 알아내고
                if (key_name == "return" or key_name == "enter"):       # 두 리스트를 합치고, 입력한 알파벳이 두 리스트에 없을 때만 enter_go를 True로 한다. 
                    if entry_text != "" and (ok_list+no_list).count(entry_text) == 0 :
                        enter_go = True   
                elif len(key_name) == 1:                  # 알파벳 한 글자만 눌렸을 때를 가정
                    if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                        entry_text = key_name.upper()   # 아스키코드를 사용하여 영문 대소문자일때 입력을 받되, 출력은 대문자(.upper())로 한다.
                    else : entry_text = ""              # 이외의 경우는 빈칸을 넣는다.
                else : entry_text = ""
                
        # 4-3. 입력, 시간에 따른 변화
        
        # 알파벳을 입력하고 엔터를 누를 경우, 알파벳이 문제단어에 있는지 찾는다.
        # 없다면 no_list에 추가하고, 있다면 ok_list에 알파벳을 추가한다.
        # 알파벳이 포함되는 경우, 알파벳을 다음과 같이 보여준다 sc + r + een
        if play_again == True : break
        if try_num == 8 : k += 1
        if enter_go == True:
            ans = entry_text
            result = word.find(ans)
            if result == -1 : #없음
                try_num += 1
                no_list.append(ans)
                sound_bad.play()
            else : #있음
                ok_list.append(ans)
                for i in range(len(word)):
                    if word[i] == ans:
                        word_show = word_show[:i] + ans + word_show[i+1:]
                sound_good.play()
            enter_go = False  
            entry_text = ""
          
        # 실패로 종료    
        if drop == True: 
            game_over = True
            word_show = word
            sound_clock.stop()
    
        # 성공으로 종료
        if word_show.find("?") == -1 and game_over == False : 
            game_over = True
            save = True
            sound_clock.stop()
            sound_save.play()
        
        # 4-4. 그리기
        screen.fill(black)
        
        # 처형대 그리기
        A = tup_r((0, size[1]*2/3))
        B = (size[0], A[1])
        C = tup_r((size[0]/6, A[1]))
        D = (C[0], C[0])
        E = tup_r((size[0]/2, D[1]))
        
        if save != True:
            pygame.draw.line(screen, white, A, B, 3)
            pygame.draw.line(screen, white, C, D, 3)
            pygame.draw.line(screen, white, D, E, 3)
        
        F = tup_r((E[0], E[1]+size[0]/6))
        if drop == False and save != True:
            pygame.draw.line(screen, white, E, F, 3)
        
        # 얼굴 (동그라미) 그리기
        # G는 사람의 모든 좌표와 연결되어 있어서, 사럄이 떨어질 때 이 좌표만 움직이면 된다. 
        r_head = round(size[0]/12)
        
        # 만약 drop이 True라면, 좌표상으로 떨어질 수 있도록 (+가 내려가는 거임) k를 더해준다
        # k는 while문이 반복될 때마다 (철자를 틀릴 때마다) 1씩 늘어남.
        # k가 점점 커져 P에 영향을 주고, P가 특정 숫자가 되는 순간 drop이 True가 되며 줄이 잘리고 사람이 떨어지는 애니메이션이 발생함.
        if drop == True : G = (F[0],F[1]+r_head+k*10)
        else : G = (F[0],F[1]+r_head)

        # 하나 틀릴 때마다 얼굴 목 팔 다리 ... 이렇게 그리기 위한 코드
        if try_num >= 1 or save == True: pygame.draw.circle(screen, white, G, r_head, 3)
        
        # 목 그리기 
        H = (G[0], G[1]+r_head)
        I = (H[0], H[1]+r_head)
        if try_num >= 2 or save == True:pygame.draw.line(screen, white, H, I, 3)

        # 사선 그리기
        l_arm = r_head*2
        
        J = (I[0]-l_arm*math.cos(30*math.pi/180),
            I[1]+l_arm*math.sin(30*math.pi/180))
        K = (I[0]+l_arm*math.cos(30*math.pi/180),
            I[1]+l_arm*math.sin(30*math.pi/180))
        J = tup_r(J)
        K = tup_r(K)
        if try_num >= 3 or save == True:pygame.draw.line(screen, white, I, J, 3)
        if try_num >= 4 or save == True:pygame.draw.line(screen, white, I, K, 3)
        
        L = (I[0], I[1]+l_arm)
        if try_num >= 5 :pygame.draw.line(screen, white, I, L, 3)

        l_leg = round(l_arm * 1.5)
        M = (L[0]-l_leg*math.cos(60*math.pi/180),
            L[1]+l_leg*math.sin(60*math.pi/180))
        N = (L[0]+l_leg*math.cos(60*math.pi/180),
            L[1]+l_leg*math.sin(60*math.pi/180))  
        M = tup_r(M)
        N = tup_r(N)  
        if try_num >= 6 or save == True:pygame.draw.line(screen, white, L, M, 3)
        if try_num >= 7 or save == True:pygame.draw.line(screen, white, L, N, 3)      
        
        # 줄 자르기 위한 빨간 줄 애니메이션 코드
        if drop == False and try_num == 8:
            O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2))
            P = (O[0]+k*2, O[1])
            if P[0] > size[0]/2+size[0]/6 :
                P = tup_r((size[0]/2+size[0]/6, O[1]))
                drop = True
                k = 0
                sound_fail.play()
            pygame.draw.line(screen, red, O, P, 3)
        
        # 힌트 표시하기 (정답 표시하기?)
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
        pygame.draw.rect(screen, white, tup_r((size[0]/2-entry_bg_size/2, size[1]*17/18-entry_bg_size/2
                                        ,entry_bg_size ,entry_bg_size)))
        screen.blit(entry, entry_pos)
        
        # 오답 표시하기
        no_text = " ".join(no_list)
        no = no_font.render(no_text, True, red)
        no_pos = tup_r((20, size[1]*2/3+20))
        screen.blit(no, no_pos)
        
        # 종료 화면
        if game_over == True:
            finish_bg = pygame.Surface(size)
            finish_bg.fill(black)
            finish_bg.set_alpha(200)
            screen.blit(finish_bg, (0,0))
            
            if save == True: finish_text = "You saved the man"
            else : finish_text = "You killed the man"
            finish = finish_font.render(finish_text, True, white)
            finish_size = finish.get_size()
            finish_pos = tup_r((size[0]/2-finish_size[0]/2, size[1]*3/4-finish_size[1]/2))
            screen.blit(finish, finish_pos)
            
            explain = finish_font.render(text, True, white)
            ex_size = explain.get_size()
            ex_pos = tup_r((size[0]/2-ex_size[0]/2, size[1]*5/6-ex_size[1]/2 + 20))
            screen.blit(explain, ex_pos)
            
            guide = guide_font.render("PRESS ANY KEY TO PLAY AGAIN", True, white)
            guide_size = guide.get_size()
            guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2))
            screen.blit(guide, guide_pos) 
        
        # 4-5. 업데이트
        pygame.display.flip()
    
pygame.quit()