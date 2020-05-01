from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import DatetimeTickFormatter
import pandas
from datetime import datetime

df = pandas.read_json("https://pomber.github.io/covid19/timeseries.json")


df1 = pandas.DataFrame(columns=['Date', 'Confirmed', 'Deaths', 'Recovered'])


for i in list(df["Australia"]):
    df1 = df1.append({'Date': datetime.strptime(i["date"], '%Y-%m-%d'), 'Confirmed': i["confirmed"], 'Deaths': i["deaths"], 'Recovered': i["recovered"]}, ignore_index=True)


f=figure(plot_width=700,plot_height=500,tools='save',x_axis_type='datetime')

f.title.text="Covid-19 statistics for Australia"
f.title.text_font_style="bold"
f.xaxis.axis_label="Date"
#convert time to AU standard day/month rather than month/day
f.xaxis.formatter=DatetimeTickFormatter(days="%d/%m")
f.yaxis.axis_label="Cases"
f.yaxis.formatter.use_scientific = False

#create  plot
f.line(df1["Date"],df1["Confirmed"],color="Orange")
f.line(df1["Date"],df1["Deaths"],color="Red")
f.line(df1["Date"],df1["Recovered"],color="Green")

show(f)