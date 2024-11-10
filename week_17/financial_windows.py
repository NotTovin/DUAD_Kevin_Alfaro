import PySimpleGUI as sg

def financial_window():
    sg.theme('Dark')
    layout = [[sg.Push(), sg.Text('Mis Finanzas', font='Default 16', text_color='white'), sg.Push()],
                [sg.Push(),sg.Table(values=[["", "", "", ""]],  
                    headings=["Descripcion", "Categoria", "Total"],
                    auto_size_columns=True,
                    justification='center',
                    key='-TABLE-'), sg.Push()],
                [sg.Push(), sg.Button('Agregar Categoría'), sg.Button('Agregar Movimiento'), sg.Button('Salir'), sg.Push()]
            ]
    
    return layout

def category_window():
    layout = [
        [sg.Text('Nombre de la categoria:'), sg.InputText(key='-CATEGORY-')],
        [sg.Button('Agregar'), sg.Button('Cancelar')]
    ]
    return sg.Window('Agregar Categoría', layout, modal=True)
    
def movement_window(categories):
    layout = [
        [sg.Text('Descripcion: '), sg.InputText(key='-DESCRIPTION-')],
        [sg.Text('Categoria: '), sg.Combo(categories, key='-CATEGORY-', readonly=True)],
        [sg.Text('Monto: '), sg.InputText(key='-MONTO-')],
        [sg.Button('Agregar'),sg.Button('Cancelar')]]
    return sg.Window('Agregar Movimiento', layout, modal=True)