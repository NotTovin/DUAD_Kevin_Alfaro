import PySimpleGUI as sg
import json

def load_data():
    try:
        with open('week_17/financials.json', 'r') as file:
            financials = json.load(file)
    except FileNotFoundError:
        financials = {'categories': [], 'movements': []}
    return financials


def save_data(financials):
    with open('week_17/financials.json', 'w') as file:
        json.dump(financials, file, indent = 4)
        


def financial_window():
    
    layout = [[sg.Push(), sg.Text('Mis Finanzas', font='Default 16', text_color='white', background_color='black', key='-TITLE-'), sg.Push()],
                [sg.Table(values=[["", "", "", ""]],  
                    headings=["Descripcion", "Categoria", "Ingreso / Gasto", "Total"],
                    auto_size_columns=True,
                    justification='center',
                    key='-TABLE-')],
                [sg.Button('Agregar Categoría'), sg.Button('Agregar Ingreso'), sg.Button('Agregar Gasto'), sg.Button('Salir')]]
    
    return layout

def add_category():
    layout = [[sg.Text('Nombre de la categoria:'), sg.InputText(key='-CATEGORY-')],
                [sg.Button('Agregar'), sg.Button('Cancelar')]]
    return sg.Window('Agregar Categoría', layout)
    
def add_movement():
    layout = [[sg.Text('Descripcion: '), sg.InputText(key='-DESCRIPTION-')],
                [sg.Text('Categoria: '), sg.InputText(key='-CATEGORY-')],
                [sg.Text('Tipo: '), sg.InputText(key='-TYPE-')],
                [sg.Text('Monto: '), sg.InputText(key='-MONTO-')],
                [sg.Button('Agregar'), sg.Button('Cancelar')]]
    return sg.Window('Agregar Movimiento', layout)

def update_data(window):
    financials = load_data()
    data = [[mov['description'], mov['category'], mov['type'], mov['amount']] for mov in financials.get('movements', [])]
    window['-TABLE-'].update(values=data)
            

if __name__ == '__main__':
    
    financials = load_data()
    layout = financial_window()
    window = sg.Window('Mis Finanzas', layout, finalize=True)
    update_data(window)
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Agregar Categoría':
            category_window = add_category()
            while True:
                event_cat, values_cat = category_window.read()
                if event_cat == 'Agregar':
                    category = values_cat['-CATEGORY-']
                    financials = load_data()
                    financials['categories'].append(category)
                    save_data(financials)
                    update_data(window)
                    sg.popup('Categoría agregada')
                    category_window.close()
                    break
                elif event_cat == 'Cancelar' or event_cat == sg.WIN_CLOSED:
                    category_window.close()
                    break
            
        elif event == 'Agregar Ingreso' or event == 'Agregar Gasto':
            movement_window = add_movement()
            while True:
                event_mov, values_mov = movement_window.read()
                if event_mov == 'Agregar':
                    movement = {
                        'description': values_mov['-DESCRIPTION-'],
                        'category': values_mov['-CATEGORY-'],
                        'type': values_mov['-TYPE-'],
                        'amount': float(values_mov['-MONTO-'])
                    }
                    financials['movements'].append(movement)
                    save_data(financials)
                    update_data(window)
                    sg.popup('Movimiento agregado')
                    movement_window.close()
                    break
                elif event_mov == 'Cancelar' or event_mov == sg.WIN_CLOSED:
                    movement_window.close()
                    break
            
    
    window.close()
        
# def add_ingreso():
#     layout = [[sg.Text('Descripcion: '), sg.InputText(key='-DESCRIPTION-')],
#                 [sg.Text('Categoria: '), sg.InputText(key='-CATEGORY-')],
#                 [sg.Text('Ingreso: '), sg.InputText(key='-INGRESO-')],
#                 [sg.Text('Monto: '), sg.InputText(key='-MONTO-')],
#                 [sg.Button('Agregar')]]

# def add_gasto():
#     layout = [[sg.Text('Descripcion: '), sg.InputText(key='-DESCRIPTION-')],
#                 [sg.Text('Categoria: '), sg.InputText(key='-CATEGORY-')],
#                 [sg.Text('Gasto: '), sg.InputText(key='-GASTO-')],
#                 [sg.Text('Monto: '), sg.InputText(key='-MONTO-')],
#                 [sg.Button('Agregar')]]