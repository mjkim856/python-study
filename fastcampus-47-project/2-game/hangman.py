import pygame

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
exit = False

# 소숫점을 정수로 변경해주는 함수
def tup_r(tup):
    temp_list = []
    
    for a in tup: 
        temp_list.append(round(a))
        
    return tuple(temp_list)

# 4. 메인 이벤트
while not exit:
    # 4-1. FPS 설정
    clock.tick()
    
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():  # 리스트로 반환됨 << 예시로 마우스 키보드 입력이 동시에 일어날 수도 있음
        if event.type == pygame.QUIT:
            exit = True
            
    # 4-3. 입력, 시간에 따른 변화
    
    # 4-4. 그리기
    screen.fill(black)
    A = tup_r((0, size[1]*2/3))
    B = (size[0], A[1])
    C = tup_r((size[0]/6, A[1]))
    D = (C[0], C[0])
    E = tup_r((size[0]/2, D[1]))
    
    pygame.draw.line(screen, white, A, B, 3)
    pygame.draw.line(screen, white, C, D, 3)
    pygame.draw.line(screen, white, D, E, 3)
    

        
    # 4-5. 업데이트
    pygame.display.flip()
    
pygame.quit()