import PySimpleGUI as sg

NUMERO_SECRETO = 42

sg.theme('DarkTeal2')
layout = [  [sg.Text('Chute um Número'), sg.InputText(),],
            [sg.Button('Ok'), sg.Button('Fechar')] ]

window = sg.Window('Bem Vindo Ao Jogo de Adivinhação!', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    if event == 'Ok':
        print('Você Digitou', values[0])



#sg.popup('Você Digitou', values[0])
#print("Parabéns você Acertou!!")
