# Hydraulic-Calculation-Software

This is a tool designed for calculating pressure drops in hydraulic systems. This application, built with Python and the customtkinter library, allows users to compute pressure loss due to friction and elevation changes in a pipeline.

**Overview**

This software performs calculations to determine the pressure drop caused by both friction and changes in elevation within a hydraulic system. Users can input various parameters related to the pipe and system, and the software will calculate the resulting pressure drop.

**Project Structure**

main.py: The main script that initializes the user interface and handles user interactions. It includes the setup for the graphical interface, input fields, and buttons for user actions.

object_class.py: Defines the Artefact class, which represents a segment of the pipeline or a fitting. The class includes methods for calculating pressure drops based on friction and elevation changes.

data_management.py: Contains functions for managing data, performing calculations, and generating results. It includes methods for reading CSV data, performing calculations, and updating the user interface with results.

equivalent_lengths_notebook.ipynb: A Jupyter Notebook that calculates equivalent lengths for various pipe fittings and artefacts. This notebook is useful for determining the impact of fittings on pressure drops and can be used to supplement the main calculations performed by the software.

**Dependencies**

Python 3.x
customtkinter
matplotlib
Jupyter Notebook (for running the equivalent lengths notebook)

# Usage

1. Run main.py

2. Enter the parameters in the input fields:

Flow

Diameter

Schedule

Length

Initial Height

Final Height

Material

Type of Artefact

3. Select the measurement system (Metric or Imperial) and click the "Add Object" button to add the parameters to the calculation.

4. Click "Complete process" to compute the total pressure drop and display the results.
