import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Variables for the calculations with their units
class Variable:
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{self.name}: {self.value} {self.unit}"
    
    def convert_to(self, new_unit):
        # Conversion logic can be added here
        match new_unit:
            case "metric":
                match self.unit:
                    case "cm":
                        return self.value / 100, "m"
                    case "in":
                        return self.value * 0.0254, "m"
                    case "L":
                        return self.value / 1000, "m³"
                    case "SCCM":
                        return self.value / 1e6, "m³/s"
                    case _:
                        return self.value, self.unit
            case "imperial":
                match self.unit:
                    case "cm":
                        return self.value / 2.54, "in"
                    case "m":
                        return self.value / 0.0254, "in"
                    case "L":
                        return self.value * 61.0237, "in³"
                    case "SCCM":
                        return self.value / 28.3168, "ft³/min"
                    case _:
                        return self.value, self.unit
            case "liters":
                match self.unit:
                    case "cm³":
                        return self.value / 1000, "L"
                    case "m³":
                        return self.value * 1000, "L"
                    case "in³":
                        return self.value / 61.0237, "L"
                    case "ft³":
                        return self.value * 28.3168, "L"
                    case _:
                        return self.value, self.unit
            case "standard":
                match self.unit:
                    case "cm³":
                        return self.value, "SCCM"
                    case "m³/s":
                        return self.value * 1e6, "SCCM"
                    case "L":
                        return self.value * 1000, "SCCM"
                    case "ft³/min":
                        return self.value * 28316.8, "SCCM"
                    case _:
                        return self.value, self.unit
            case _:
            # If the unit is not recognized, return the original value and unit
                return self.value, self.unit

# Example usage
# var = Variable("Diameter", 10, "cm")
# print(var)

# --------------------------------------------
# App layout
app.layout = html.Div([
    html.H1("Pipe Diameter Calculator", style={'textAlign': 'center'}),
    dcc.Input(id='flow_rate', type='number', placeholder='Flow Rate'),
    dcc.Dropdown(
        id='flow_rate_unit',
        options=[
            {'label': 'm³/s', 'value': 'metric'},
            {'label': 'ft³/s', 'value': 'imperial'},
            {'label': 'l/min', 'value': 'liters'},
            {'label': 'SCCM', 'value': 'standard'},
        ],
        value='metric',
        style={'width': '30%'},
    ),
    dcc.Input(id='velocity', type='number', placeholder='Velocity (m/s)'),
    dcc.Input(id='roughness', type='number', placeholder='Roughness (m)'),
    dcc.Input(id='length', type='number', placeholder='Length (m)'),
    dcc.Input(id='viscosity', type='number', placeholder='Viscosity (Pa.s)'),
    dcc.Input(id='density', type='number', placeholder='Density (kg/m³)'),
    html.Button('Calculate', id='calculate-button'),
    html.Div(id='output-container')
])

# ----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)