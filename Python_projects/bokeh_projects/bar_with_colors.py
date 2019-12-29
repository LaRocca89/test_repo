from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
import pandas as pd

"""
The objective here is to create a bokeh plot that pulls data from a CSV file and plots it.
"""

output_file("test_bar_colors.html")
data = pd.read_csv('test.csv')
fruits = data['Fruit']
counts = data['Value']

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
p = figure(x_range=fruits, y_range=(0, 9), plot_height=350, title="Fruit Counts",
           toolbar_location=None)
p.vbar(x='fruits', top='counts', width=0.9, color='color', source=source, legend="fruits")
p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
