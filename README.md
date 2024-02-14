[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Sysy6avs)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dm4bem/thermal-model-steady-state-step-response-group-4/HEAD)

Different codes are available in the main branch :
- WeatherData.py, that compile with the weather data of a specific place (in a .epw file) and allows you to obtain the direct radiation, diffuse radiation and solar radiation diffused by the ground. 
- Thermal model.py, the main code that combines the thermal mode, the steady-state and step response.
- Insulation out.ipynb, that study the influence of the position of the insulation (either on the inside or on the outside of the walls) on the time step.
- Inputs.py, which calculate the total solar irradiance and then the solar radiation absorbed by the wall and the glass. It uses the weather data of a specific place (in a .epw file). The files walls_out.csv and input_data_set.csv are inputs for this code.

For these codes, it is required that the file dm4bem.py is in the same folder as those ones in order for them to compile without errors.
