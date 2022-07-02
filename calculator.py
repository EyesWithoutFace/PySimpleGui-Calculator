#calculator.py
import PySimpleGUI as sg
layout = [
        [sg.Text("", key = 'input')],
        [sg.Button('C'), sg.Button('Del')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('/')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('-')],
        [sg.Button('.'), sg.Button('0'), sg.Button('='), sg.Button('+')]
        ]
window = sg.Window('Calculator', layout, default_button_element_size = (6, 3))

Result = ''

while True:
    button, value = window.Read()
    if button == 'C':
        Result = ''
        window.find_element('input').Update(Result)
    elif button =='Del':
        Result = Result[:-1]
        window.find_element('input').Update(Result)
    elif len(Result) == 16:
        pass

    elif button == '=':
        Answer = eval(Result)
        Answer = str(round(float(Answer),3))
        window.find_element('input').Update(Answer)
        Result = Answer
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        Result += button
        window.find_element('input').Update(Result)
window.close()
