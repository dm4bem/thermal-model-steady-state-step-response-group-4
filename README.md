[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Sysy6avs)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dm4bem/thermal-model-steady-state-step-response-group-4/HEAD)

Different codes are available in the main branch :
- WeatherData.py, that compile with the weather data of a specific place (in a .epw file) and allows you to obtain the direct radiation, diffuse radiation and solar radiation diffused by the ground. 
- Thermal model.py, the main code that combines the thermal mode, the steady-state and step response.
- Insulation out.ipynb, that study the influence of the position of the insulation (either on the inside or on the outside of the walls) on the time step.
- Conductivity_insulation.ipynb, that study the influence of the insulation's conductivity on the time step and settling time.
- Glass_capacity.ipynb, that study the influence of neglecting the capacity of the glass on the behavior of the thermal system. 

For these codes, it is required that the file dm4bem.py is in the same folder as those ones in order for them to compile without errors.
