# corona
Coronavirus (Covid-19) Scripts that I've been playing around with.

corona_bokeh.py is a simple Bokeh Python graph using the timeseries datasource from [https://github.com/pomber/covid19](https://github.com/pomber/covid19)

The json contains the number of Coronavirus confirmed cases, deaths, and recovered cases for every country and every day since 2020-1-22:

```
{
  "Australia": [
    {
      "date": "2020-4-16",
      "confirmed": 6462,
      "deaths": 63,
      "recovered": 2355
    },
    {
      "date": "2020-4-17",
      "confirmed": 6522,
      "deaths": 66,
      "recovered": 3808
    },
    ...
  ],
  ...
}
```
