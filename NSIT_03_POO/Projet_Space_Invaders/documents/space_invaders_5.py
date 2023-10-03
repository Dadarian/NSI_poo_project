import pygame
import space
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
fond = pygame.image.load('background2.png')

player = space.Joueur()
tir = space.Balle(player)
tir.etat = "attente"

listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

running = True
while running:
    screen.blit(fond, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.sens = "gauche"
            if event.key == pygame.K_RIGHT:
                player.sens = "droite"
            if event.key == pygame.K_SPACE:
                player.tirer()
                tir.etat = "tiree"

    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
        if (
    player.position < ennemi.depart + 40
    and player.position + 40 > ennemi.depart
    and player.vie > 0
    and player.position + 40 > ennemi.hauteur
    and player.position < ennemi.hauteur + 40
):
            player.perdre_vie()  # Le joueur perd une vie lorsqu'il entre en collision avec un ennemi

    font = pygame.font.Font(None, 36)
    text = font.render(f"Vies : {player.vie}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if player.vie <= 0:
        running = False

    player.deplacer()
    screen.blit(tir.image, [tir.depart, tir.hauteur])
    tir.bouger()
    screen.blit(player.image, [player.position, 500])

    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image, [ennemi.depart, ennemi.hauteur])

    pygame.display.update()
