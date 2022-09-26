from motion_capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models.tickers import FixedTicker
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 250, width = 900, title = 'Motion Graph', title_location = "above", sizing_mode = "stretch_width")
p.title.text_font_size = '25px'
p.title.align = "center"
p.yaxis.ticker = FixedTicker(ticks=[0, 1])
p.ygrid.grid_line_color = None

hover = HoverTool(tooltips=[("Start: ","@Start_string"), ("End: ","@End_string")])
p.add_tools(hover)
q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = "green", source= cds)

output_file("Graph2.html")
show(p)