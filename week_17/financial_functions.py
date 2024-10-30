import PySimpleGUI as sg
from financial_data import load_data, save_data 
from financial_windows import financial_window, category_window, movement_window

def update_data(window):
    financials = load_data()
    data = [[mov['description'], mov['category'], mov['amount']] for mov in financials.get('movements', [])]
    window['-TABLE-'].update(values=data)
    
def validate_category(category):
    financials = load_data()
    if category not in financials['categories']:
        sg.popup('Error: La categoría no existe. Por favor, ingresa una categoría válida o crea una nueva.')
        return False
    return True

def validate_amount(amount):
    try:
        return float(amount)
    except ValueError:
        sg.popup('Error: El monto debe ser un número.')
        return None