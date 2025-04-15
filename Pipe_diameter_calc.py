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