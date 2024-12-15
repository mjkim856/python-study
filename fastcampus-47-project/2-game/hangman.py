import pygame, math

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

# 소숫점을 정수로 변경해주는 함수
def tup_r(tup):
    temp_list = []
    
    for a in tup: 
        temp_list.append(round(a))
        
    return tuple(temp_list)

drop = False
exit = False
k = 0

# 4. 메인 이벤트
while not exit:
    # 4-1. FPS 설정
    clock.tick(60)
    
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():  # 리스트로 반환됨 << 예시로 마우스 키보드 입력이 동시에 일어날 수도 있음
        if event.type == pygame.QUIT:
            exit = True
            
    # 4-3. 입력, 시간에 따른 변화
    k += 1
    
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
    pygame.draw.circle(screen, white, G, r_head, 3)
    
    # 목 그리기 
    H = (G[0], G[1]+r_head)
    I = (H[0], H[1]+r_head)
    pygame.draw.line(screen, white, H, I, 3)
        
    # 사선 그리기
    l_arm = r_head*2
    
    J = (I[0]-l_arm*math.cos(30*math.pi/180),
         I[1]+l_arm*math.sin(30*math.pi/180))
    K = (I[0]+l_arm*math.cos(30*math.pi/180),
         I[1]+l_arm*math.sin(30*math.pi/180))
    J = tup_r(J)
    K = tup_r(K)
    pygame.draw.line(screen, white, I, J, 3)
    pygame.draw.line(screen, white, I, K, 3)
    
    L = (I[0], I[1]+l_arm)
    pygame.draw.line(screen, white, I, L, 3)
    
    l_leg = round(l_arm * 1.5)
    M = (L[0]-l_leg*math.cos(60*math.pi/180),
         L[1]+l_leg*math.sin(60*math.pi/180))
    N = (L[0]+l_leg*math.cos(60*math.pi/180),
         L[1]+l_leg*math.sin(60*math.pi/180))  
    M = tup_r(M)
    N = tup_r(N)  
    pygame.draw.line(screen, white, L, M, 3)
    pygame.draw.line(screen, white, L, N, 3)      
    
    # 줄 자르기 위한 빨간 줄 애니메이션 코드
    if drop == False:
        O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2))
        P = (O[0]+k*2, O[1])
        if P[0] > size[0]/2+size[0]/6 :
            P = tup_r((size[0]/2+size[0]/6, O[1]))
            drop = True
            k = 0
        pygame.draw.line(screen, red, O, P, 3)
    
    # 4-5. 업데이트
    pygame.display.flip()
    
pygame.quit()