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
    screen.fill(white)
    
    # 4-5. 업데이트
    pygame.display.flip()
    
pygame.quit()