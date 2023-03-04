import random, pygame, sys
from pygame.locals import *
pygame.init()
white = (255,255,255)
grey = (211,211,211)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,102)
red = (255,25,0)

font = pygame.font.SysFont('arialblack', 30)

def check(times, word, guess, window):
    randlist = ['']*5
    space = 0
    guesscolor= [grey]*5
    
    for i in range(len(guess)):
        if guess[i] == word[i]:
            guesscolor[i] = green
        elif guess[i] in word:
            guesscolor[i] = yellow
        
    for x in range(5):
        randlist[x] = font.render(guess[x], True, black)
        pygame.draw.rect(window, guesscolor[x], pygame.Rect(60 +space, 50+ (times*70), 50, 50))
        window.blit(randlist[x], (70 + space, 53 + (times*70)))
        space += 80
    if guesscolor.count(green) == 5:
        return True
    
    
def main():
    file = open('list.txt', 'r')
    wordlist = file.readlines()
    word = wordlist[random.randint(0,len(wordlist)-1)].upper()
    print(word)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((500,500))
    window.fill(black)
    pygame.display.set_caption("Wordle!")

    
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(window, white, pygame.Rect(60+(j*80), 50+(i*70), 50, 50), 2 )
    win = False
    times = 0
    guess = ''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    guess += event.unicode.upper()
                
                if win or times == 6:
                    main()
                    
                if event.key == pygame.K_BACKSPACE or len(guess) >5:
                    guess = guess[:-1]
                if event.key == K_RETURN and len(guess) == 5:
                    win = check(times, word, guess, window)
                    times += 1
                    guess = ''
                    
        window.fill(black,(0, 450, 450, 200))
        rendguess = font.render(guess, True, grey)
        window.blit(rendguess, (180,450))
        
        titlefont = pygame.font.SysFont('arialblack', 80)
        againfont = pygame.font.SysFont('arialblack', 30)
        again = againfont.render('Press any to play again', True, red)
        
        if win:
            youwin = titlefont.render('Win!', True, red)
            window.fill(black)
            window.blit(youwin, (150,150))
            window.blit(again, (55, 325))
            
        elif not win and times == 6:
            youlose = titlefont.render('Lose!', True, red)
            window.fill(black)
            window.blit(youlose,(133,150))
            window.blit(again, (55, 325))
            
        pygame.display.update()
        clock.tick(30)

main()
    