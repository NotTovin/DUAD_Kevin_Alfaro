import PySimpleGUI as sg
from financial_functions import update_data, validate_category, validate_amount
from financial_data import load_data, save_data
from financial_windows import financial_window, category_window, movement_window

if __name__ == '__main__':
    financials = load_data()
    layout = financial_window()
    window = sg.Window('Mis Finanzas', layout, finalize=True, no_titlebar=True)
    update_data(window)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        
        elif event == 'Agregar Categoría':
            category = category_window()
            while True:

                event_cat, values_cat = category.read()
                
                if event_cat == 'Agregar':
                    category_value = values_cat['-CATEGORY-']
                    if category_value and category_value not in financials['categories']:
                        financials['categories'].append(category_value)
                        save_data(financials)
                        sg.popup('Categoría agregada')
                    elif category_value in financials['categories']:
                        sg.popup('La categoría ya existe')
                        
                elif event_cat in (sg.WIN_CLOSED, 'Cancelar'):
                    category.close()
                    break
                
        
        elif event == 'Agregar Movimiento':
            
            categories = financials['categories']
            movement = movement_window(categories)
            
            while True:
                event_mov, values_mov = movement.read()
                    
                if event_mov == 'Agregar':
                    description = values_mov['-DESCRIPTION-']
                    category = values_mov['-CATEGORY-']
                    amount = validate_amount(values_mov['-MONTO-'])
                    
                    if amount is not None and validate_category(category):
                        movement_data = {
                            'description': description,
                            'category': category,
                            'amount': amount
                        }
                        financials['movements'].append(movement_data)
                        save_data(financials)
                        sg.popup('Movimiento agregado')
                        update_data(window)  
                        
                    else:
                        sg.popup('Por favor, revisa los datos ingresados')
                        
                elif event_mov in (sg.WIN_CLOSED, 'Cancelar'):
                    movement.close()
                    break
                
            
    window.close()