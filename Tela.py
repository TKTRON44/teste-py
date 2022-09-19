import PySimpleGUI as sg

sg.theme('Reddit')

layout = [  [sg.Text('Chute seu Numero'), sg.InputText()],
            [sg.Button('Ok')] ]

window = sg.Window('Bem vindo ao jogo de Adivinhação', layout)
