import sys, pygame
from sys import exit
pygame.init()

class prueba1:
    def __init__(self):
        self.tamaño_de_pantalla()

    def tamaño_de_pantalla (self):

        size = width, height = 1000, 700
        speed = [0,0]
        black = 112, 10, 139

        screen = pygame.display.set_mode(size)
        

        ball = pygame.image.load("intro_ball.gif")
        ballrect = ball.get_rect()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            ballrect = ballrect.move(speed)

            if ballrect.left < 0 or ballrect.right > width:
                speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                speed[1] = -speed[1]

            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()



class prueba2():
    def __init__(self) -> None:
        self.tuto()

    def tuto(self):
        #!siempre comenzar con esto
        pygame.init()
        #! NOMBRE DE LA VENTANA
        pygame.display.set_caption("PONG ULTIMATE GAME POG CHAMP")
        speed = [5,5]
        score_1=0
        score_2=0
        print("veces")
        #! Control de fps (IMPORTANTE)
        clock = pygame.time.Clock()
        #! Pantalla (DISPLAY SURFACES SOLO ES UNA)
        screen = pygame.display.set_mode((1000,500))
        #! REGULAR SURFACE (TEXTO)
        text_font = pygame.font.Font(None,50)
        

        
       
        #! Pantalla (REGULAR SURFACES multiples surfaces dentro del display surfaces) Y RECTANGULOS
        rectangulo1_surface= pygame.image.load("imagenes/rectangulo_1.png").convert_alpha()
        rectangulo1_rect= rectangulo1_surface.get_rect( center= (20,250))

        rectangulo2_surface = pygame.image.load("imagenes/rectangulo_2.png").convert_alpha()
        rectangulo2_rect= rectangulo2_surface.get_rect(center = (985,250))

        fondo_surface = pygame.image.load("imagenes/fondo.jpg").convert()

        pelota_surface = pygame.image.load("imagenes/pelota.png").convert_alpha()
        pelota_rect= pelota_surface.get_rect(center = (500,250))

        while True:
            #!scores
            score_surface_1 = text_font.render(str(score_1),False, "Black" )
            score_rect_1= score_surface_1.get_rect( center= (75,50))
            score_surface_2 = text_font.render(str(score_2),False, "Black" )
            score_rect_2= score_surface_2.get_rect( center= (925,50))


            pelota_rect = pelota_rect.move(speed) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        rectangulo2_rect.y -= 100
                    if event.key == pygame.K_DOWN:
                        rectangulo2_rect.y += 100
                    
                    if event.key == pygame.K_w:
                        rectangulo1_rect.y -= 100
                    if event.key == pygame.K_s:
                        rectangulo1_rect.y += 100

                if event.type == pygame.KEYUP:
                    pass
                
            #!AQUI SE HACE TODOS LOS ELEMENTOS
            #! TOMAR EN CUENTA LA JERARQUIA A LA HORA DE COLOCAR IMAGENES PARA NO SOBRE PONER
            screen.blit(fondo_surface,(0,0))

            screen.blit(rectangulo1_surface,rectangulo1_rect)
            screen.blit(rectangulo2_surface,rectangulo2_rect)

            screen.blit(score_surface_1,score_rect_1)
            screen.blit(score_surface_2,score_rect_2)
            
            

            screen.blit(pelota_surface,pelota_rect)
            
            

            #! COLICIONES
            if(rectangulo2_rect.colliderect(pelota_rect)):
                speed[0] = -speed[0]
                speed[0] *= 1.05
            if rectangulo1_rect.colliderect(pelota_rect):
                speed[0] = -speed[0]
                speed[0] *= 1.05
            if pelota_rect.top < 0 or pelota_rect.bottom > 500:
                speed[1] = -speed[1]

            if pelota_rect.right > 1000:
                pelota_rect.left = 500
                score_1+=1

            if pelota_rect.left < 0:
                pelota_rect.left = 500
                score_2+=1
            
            elif score_2 >= 5:
                score_surface_3 = text_font.render("GANO JUGADOR 1",False, "Black" )
                score_rect_3= score_surface_3.get_rect( center= (500,250))
                screen.blit(score_surface_3,score_rect_3)
                speed[0] *=0
                speed[1] *=0
                pelota_rect.left = 500
                pelota_rect.top = 250

            elif score_1 >=5:
                score_surface_4 = text_font.render("GANO JUGADOR 2",False, "Black" )
                score_rect_4= score_surface_4.get_rect(center= (500,250))
                screen.blit(score_surface_4,score_rect_4)
                speed[0] *=0
                speed[1] *=0
                pelota_rect.left = 500
                pelota_rect.top = 250

                


            
            
                
                



            
            #! AQUI SE ACTUALIZA PARA QUE SE ENCICLE Y NO SE CIERRE
            pygame.display.update()
            #! CUANTAS VECES POR SEGUNDOS (FPS)
            clock.tick(60)

            


prueba2()


"""
x, y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
"""