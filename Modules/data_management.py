# Functions

import csv
import os
from Modules.object_class import Artefact
import customtkinter as Ctk

global objects_dict
global results_list

objects_dict = {}
results_list = []


def csv_to_dict():
    data_dict = {}
    
    object_class_path = os.path.abspath(__file__)

    modules_directory = os.path.dirname(object_class_path)

    materials_data = os.path.join(modules_directory, 'Materials_data')

    tables_list = os.listdir(materials_data)
    
    for table in tables_list:
        data_dict[table] = {}

        with open(os.path.join(materials_data, table), mode='r', encoding='utf-8') as data_csv:
            data_table = csv.reader(data_csv, delimiter=',')
            
            row_count = 0
            headers = []

            for row in data_table:
                if row_count == 0:
                    
                    headers = row
                    for col in headers:
                        data_dict[table][col] = []
                    row_count += 1
                else:
                    
                    for col, element in zip(headers, row):
                        data_dict[table][col].append(element)
                        
    return data_dict


def create_and_calculate(flow, diameter, schedule, length, system, initial_height, final_height, material, type_of_artefact, results_list):

    tables_info = csv_to_dict()
    if system == 'Metric':
        diameter_unit = 'mm'
        multiplier = 10.674
        density = 1000
        gravity = 9.81
        conversor_1 = 1
        conversor_2 = 1000
        conversor_3 = 1

    elif system == 'Imperial':
        diameter_unit = 'ft'
        multiplier = 4.53
        density = 1.94
        gravity = 32.2
        conversor_1 = 12**2
        conversor_2 = 1
        conversor_3 = 0.00223

    if schedule == 40:
        table = 'Tabla F1.csv'

    elif schedule == 80:
        table = 'Tabla F2.csv'

    else:
        pass

    if type_of_artefact != 'Pipe':
        
        for artefact in range(len(tables_info[f'fittings_{system.lower()}.csv'][''])):
            if tables_info[f'fittings_{system.lower()}.csv'][''][artefact] == type_of_artefact:

                length = tables_info[f'fittings_{system.lower()}.csv'][f'{diameter} '][artefact]

                break
            else:
                continue

    diameter_index = next((i for i, x in enumerate(tables_info[table]['Nominal NPS(in)']) if x == diameter), None)

    real_diameter = tables_info[table][f'D.I({diameter_unit})'][diameter_index]
            
    material_index = next((i for i, x in enumerate(tables_info['Tabla 8.3.csv']['Pipe Type']) if x == material), None)
    material_coefficient = tables_info['Tabla 8.3.csv']['Design Value'][material_index]

    this_pipe = Artefact(flow = flow, diameter = diameter, schedule = schedule, length = length, system = system,
                 material = material, material_coefficient = material_coefficient, real_diameter = real_diameter, 
                 multiplier = multiplier, initial_height = initial_height, final_height = final_height, 
                 density = density, gravity = gravity, conversor_1=conversor_1, conversor_2=conversor_2,
                 conversor_3=conversor_3, type_of_artefact = type_of_artefact)
    
    results_list.append(this_pipe.pressure_drop()['Total pressure drop'])

    return this_pipe.pressure_drop()['Total pressure drop']


def complete_process(results_list, app):

    total_pressure_drop = sum(results_list)

    result_label = Ctk.CTkLabel(app, text=f'Total pressure drop: {total_pressure_drop:.2f} ', fg_color='gray')
    result_label.place(relx = 0.5, rely = 0.6)

    return total_pressure_drop
