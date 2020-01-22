"""
This module is responsible for defining information we want to get from user.
"""


class UserInputServiceInverse:
    def __init__(self):
        self.number_parameters_to_get_from_user = [
            {"name": "Simulation step",
                "description": "How big steps to take when simulating. The larger, the quicker the simulation.",
                "input_name": "simulation_step_input_seconds",
                "variable_name": "dt",
                "default_value": 20,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "seconds",
                "unit_abbrev": "s"},
            {"name": "Object length",
                "description": "The length of the 1D object we are simulating.",
                "input_name": "object_length_input_centimetres",
                "variable_name": "object_length",
                "default_value": 1,
                "parse_function": float,
                "multiplicate_to_SI": 0.01,
                "unit": "centimetres",
                "unit_abbrev": "cm"},
            {"name": "Position of interest",
                "description": "The distance in which the temperatures were measured.",
                "input_name": "place_position_input_centimetres",
                "variable_name": "place_of_interest",
                "default_value": 0.445,
                "parse_function": float,
                "multiplicate_to_SI": 0.01,
                "unit": "centimetres",
                "unit_abbrev": "cm"},
            {"name": "Number of elements",
                "description": "How granular should be the simulation.",
                "input_name": "number_of_elements_input",
                "variable_name": "number_of_elements",
                "default_value": 15,
                "parse_function": int,
                "multiplicate_to_SI": 1,
                "unit": "",
                "unit_abbrev": "-"},
            {"name": "Plotting period",
                "description": "How frequently to update the plot (in simulation seconds).",
                "input_name": "plotting_period_input",
                "variable_name": "callback_period",
                "default_value": 1000,
                "parse_function": int,
                "multiplicate_to_SI": 1,
                "unit": "seconds",
                "unit_abbrev": "s"},
            {"name": "Theta",
                "description": "Determines explicitness (0) and implicitness (1) of the algorithm approach.",
                "input_name": "theta_input",
                "variable_name": "theta",
                "default_value": 0.5,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "",
                "unit_abbrev": "-"},
            {"name": "Robin Alpha",
                "description": "Defines the convection heat transfer coefficient.",
                "input_name": "robin_alpha_input",
                "variable_name": "robin_alpha",
                "default_value": 13.5,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "Watt/Kelvin",
                "unit_abbrev": "W/K"},
            {"name": "Window span",
                "description": "How far into the future to look when matching the temperatures.",
                "input_name": "window_span_input",
                "variable_name": "window_span",
                "default_value": 3,
                "parse_function": int,
                "multiplicate_to_SI": 1,
                "unit": "",
                "unit_abbrev": "-"},
            {"name": "Tolerance",
                "description": "How accurate should the temperature-matching be.",
                "input_name": "tolerance_input",
                "variable_name": "tolerance",
                "default_value": 1e-3,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "",
                "unit_abbrev": "-"},
            {"name": "Initial Heat Flux",
                "description": "What should we fill the initial Heat Flux array with.",
                "input_name": "q_init_input",
                "variable_name": "q_init",
                "default_value": 0,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "Watt",
                "unit_abbrev": "W"},
            {"name": "Initial Heat Flux Adjustment",
                "description": "How big should be the initial step when adjusting Heat Flux.",
                "input_name": "init_q_adjustment_input",
                "variable_name": "init_q_adjustment",
                "default_value": 20,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "Watt",
                "unit_abbrev": "W"},
            {"name": "Adjusting Value Coefficient",
                "description": "By which should the adjusting value being multiplied by.",
                "input_name": "adjusting_value_input",
                "variable_name": "adjusting_value",
                "default_value": -0.7,
                "parse_function": float,
                "multiplicate_to_SI": 1,
                "unit": "",
                "unit_abbrev": "-"}
        ]
