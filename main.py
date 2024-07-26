# Main

import customtkinter as Ctk
from Modules.data_management import create_and_calculate, complete_process
import Modules.object_class

Ctk.set_appearance_mode("System")
app = Ctk.CTk()

# Lists

materials = [
    'Ductile Iron Steel',
    'Cast Iron with Cement Lining',
    'Cast Iron with Bituminous Coating',
    'Plastic',
    'Copper',
    'Brass Glass',
    'Bare Cast Iron Steel',
    'Concrete',
    'Corrugated Steel'
]

artefacts = [
    'Pipe',
    '45°elbow',
    '90°elbow',
    '90°long-turn elbow',
    'Gate valve',
    'Butterfly valve',
    'Swing check'
]

schedules = [
    '40',
    '80'
]

nominal_diameters = [
    '1/8', '1/4', '3/8', '1/2', '3/4',
    '1', '1 1/4', '1 1/2', '2', '2 1/2',
    '3', '3 1/2', '4', '5', '6',
    '8', '10', '12', '14', '16',
    '18', '20', '24'
]

global results_list
results_list = []

# Functions

# Entries
flow_entry = Ctk.CTkEntry(app, placeholder_text='Flow')
flow_entry.place(relx=0.1, rely=0.5, anchor = 'w')

length_entry = Ctk.CTkEntry(app, placeholder_text='Length')
length_entry.place(relx=0.1, rely=0.6, anchor = 'w')

i_height_entry = Ctk.CTkEntry(app, placeholder_text='Initial height')
i_height_entry.place(relx=0.1, rely=0.7, anchor = 'w')

f_height_entry = Ctk.CTkEntry(app, placeholder_text='Final height')
f_height_entry.place(relx=0.3, rely=0.7, anchor = 'w')

# Menus
artefacts_combobox = Ctk.CTkComboBox(app, values=artefacts)
artefacts_combobox.place(relx=0.3, rely=0.475)

materials_combobox = Ctk.CTkComboBox(app, values=materials)
materials_combobox.place(relx=0.3, rely=0.575)

schedule_combobox = Ctk.CTkComboBox(app, values=schedules)
schedule_combobox.place(relx=0.5, rely=0.475)

diameters_combobox = Ctk.CTkComboBox(app, values=nominal_diameters)
diameters_combobox.place(relx=0.7, rely=0.475)

# Switch
system_switch = Ctk.CTkSwitch(app, onvalue='Metric', offvalue='Imperial', text='Metric')
system_switch.place(relx=0.3, rely=0.4)

# Labels
imperial_label = Ctk.CTkLabel(app, text='Imperial')
imperial_label.place(relx=0.23, rely=0.4)

# Buttons
complete_process_button = Ctk.CTkButton(app, text='Complete process', command=lambda: complete_process(results_list=results_list, app=app))
complete_process_button.place(relx=0.8, rely=0.9)

add_object_button = Ctk.CTkButton(app, text='+ Add', command=lambda: create_and_calculate(
    flow=float(flow_entry.get()),
    diameter=diameters_combobox.get(),
    schedule=int(schedule_combobox.get()),
    length=float(length_entry.get()),
    system=system_switch.get(),
    initial_height=float(i_height_entry.get()),
    final_height=float(f_height_entry.get()),
    material=materials_combobox.get(),
    type_of_artefact=artefacts_combobox.get(),
    results_list=results_list
))
add_object_button.place(relx=0.3, rely=0.8)

app.geometry("800x600")
app.mainloop()