from matplotlib.figure import Figure
from textwrap import wrap


def plot_graph(results, indicator):
    indicator = indicator[0]
    country_list = []
    dict_data = {}
    fig = Figure()
    ax = fig.subplots()
    for data in results:
        country = data['countryname']
        value = data['value']
        year = data['year']
        if country not in country_list:
            country_list.append(data['countryname'])
            dict_data[country] = []
        else:
            dict_data[country].append(
                [year, value])
    x = []
    y = []
    for key in dict_data:
        for datapoint in dict_data[key]:
            x.append(datapoint[0])
            y.append(datapoint[1])
        ax.plot(x, y, label=key)
        ax.set_xlabel('Year')
        ax.set_ylabel('\n'.join(wrap(indicator, 40)))
        x = []
        y = []
    ax.legend()
    ax.grid()
    fig.savefig('./world_bank_connect/plots/plot.png')
