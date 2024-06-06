import turtle

# Configurações iniciais da tela
window = turtle.Screen()
window.title("Jogo de Damas")
window.bgcolor("white")
window.setup(width=600, height=600)

# Configurações do tabuleiro
tamanho_quadrado = 60
tamanho_tabuleiro = 8
cor1 = "black"
cor2 = "white"

# Configuração das peças
peças_brancas = []
peças_pretas = []

# Desenhando o tabuleiro
def desenhar_tabuleiro():
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    
    for i in range(tamanho_tabuleiro):
        for j in range(tamanho_tabuleiro):
            turtle.goto(-240 + j * tamanho_quadrado, 240 - i * tamanho_quadrado)
            if (i + j) % 2 == 0:
                turtle.color(cor1)
            else:
                turtle.color(cor2)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(tamanho_quadrado)
                turtle.right(90)
            turtle.end_fill()


# Desenhando a borda
def desenhar_borda():
    turtle.penup()
    turtle.goto(-240, 240)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color("black")
    for _ in range(4):
        turtle.forward(tamanho_tabuleiro * tamanho_quadrado)
        turtle.right(90)

    
# Desenhando uma peça
def desenhar_peça(x, y, cor):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(cor)
    turtle.begin_fill()
    turtle.circle(tamanho_quadrado // 2 - 5)
    turtle.end_fill()

# Posicionando as peças no tabuleiro
def posicionar_peças():
    for i in range(tamanho_tabuleiro):
        for j in range(tamanho_tabuleiro):
            x = -240 + j * tamanho_quadrado + tamanho_quadrado // 2
            y = 218 - i * tamanho_quadrado - tamanho_quadrado // 2
            
            if (i + j) % 2 != 0:
                if i < 3:
                    peças_pretas.append((x, y))
                    desenhar_peça(x, y, "black")
                elif i > 4:
                    peças_brancas.append((x, y))
                    desenhar_peça(x, y, "red")

# Função principal
def main():
    desenhar_tabuleiro()
    desenhar_borda()
    posicionar_peças()
    turtle.done()

if __name__ == "__main__":
    main()
