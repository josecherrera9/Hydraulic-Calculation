# Objects

class Artefact():
    def __init__(self, flow, diameter, schedule, length, system,
                 material, material_coefficient, real_diameter, multiplier,
                 initial_height, final_height, density, gravity, conversor_1,
                 conversor_2, conversor_3, type_of_artefact):
        
        self.flow = flow
        self.diameter = diameter
        self.cedule = schedule
        self.length = float(length)
        self.initial_height = float(initial_height)
        self.final_height = float(final_height)
        self.system = system
        self.material = material
        self.material_coefficient = float(material_coefficient)
        self.real_diameter = float(real_diameter)
        self.multiplier = multiplier
        self.density = float(density)
        self.gravity = float(gravity)
        self.conversor_1 = float(conversor_1)
        self.conversor_2 = float(conversor_2)
        self.conversor_3 = float(conversor_3)

    def pressure_drop(self):
        
        #Pressure Drop by Friction
        drop_per_length_unit_up = self.multiplier*((self.flow*self.conversor_3)**1.852)
        drop_per_length_unit_bottom = (self.material_coefficient**1.852)*((self.real_diameter/self.conversor_2)**4.871)
        drop_per_length_unit = -1*drop_per_length_unit_up / drop_per_length_unit_bottom
        friction_pressure_drop = drop_per_length_unit * self.length

        # Pressure Drop by Height
        drop_by_height = (self.density*-self.gravity*(self.final_height - self.initial_height)) / self.conversor_1

        Total_drop = friction_pressure_drop + drop_by_height

        pipe_object = {'Internal Diameter':self.real_diameter, 'Material':self.material, 'Material Coefficient':self.material_coefficient,
                       'Cedule':self.cedule, 'Length':self.length, 'Height change':self.final_height - self.initial_height,
                       'Flow through pipe':self.flow, 'Pressure drop by friction':friction_pressure_drop, 'Pressure drop by height':drop_by_height,
                       'Total pressure drop':Total_drop}
        
        return pipe_object