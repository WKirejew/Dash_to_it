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
        # Conversion logic for flow unit conversion
        match new_unit:
            case "metric":
                match self.unit:
                    case "imperial":
                        return self.value / 35.3146, "metric"
                    case "liters":
                        return self.value / 60000, "metric"
                    case "standard":
                        return self.value / 60000000, "metric"
                    case _:
                        return self.value, self.unit
            case "imperial":
                match self.unit:
                    case "metric":
                        return self.value * 35.3146, "imperial"
                    case "liters":
                        return self.value / 1699.0107, "imperial"
                    case "standard":
                        return self.value / 471.9472, "imperial"
                    case _:
                        return self.value, self.unit
            case "liters":
                match self.unit:
                    case "metric":
                        return self.value * 60000, "liters"
                    case "imperial":
                        return self.value * 1699.0107, "liters"
                    case "standard":
                        return self.value / 1000, "liters"
                    case _:
                        return self.value, self.unit
            case "standard":
                match self.unit:
                    case "metric":
                        return self.value * 60000000, "standard"
                    case "imperial":
                        return self.value * 471.9472, "standard"
                    case "liters":
                        return self.value * 1000, "standard"
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