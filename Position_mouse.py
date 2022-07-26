import pyautogui

pyautogui.sleep(4)
# Tempo de delay, ou seja, depois de rodar esse código, imediatamente posicione o mouse onde você quer obter a posição e espere 4 segundos para o resultado
# você pode trocar o tempo para o que deseja, só alterar o número 4 que está dentro do parenteses.

print(pyautogui.position())

# Esse script retorna a posição da setinha do mouse na tela do seu computador;
# A resposta é em formato de eixo X e Y;
# O ponto zero ou ponto de referência deste código é o canto/quina superior esquerdo da sua tela;