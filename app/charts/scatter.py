import os

from pyecharts import Scatter, Page


def scatter_charts():
    page = Page()

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    chart = Scatter("散点图-双数值轴")
    chart.add("A", v1, v2)
    chart.add("B", v1[::-1], v2)
    page.add(chart)

    chart = Scatter("散点图-x轴类目轴")
    chart.add("A", ["a", "b", "c", "d", "e", "f"], v2)
    chart.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1],
              xaxis_type="category")
    page.add(chart)

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    chart = Scatter("散点图-VisualMap")
    chart.add("A", v1, v2)
    chart.add("B", v1[::-1], v2, is_visualmap=True)
    page.add(chart)

    chart = Scatter("散点图-VisualMap")
    chart.add("A", v1, v2)
    chart.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size',
              visual_range_size=[20, 80])
    page.add(chart)

    data = [
        [28604, 77, 17096869],
        [31163, 77.4, 27662440],
        [1516, 68, 1154605773],
        [13670, 74.7, 10582082],
        [28599, 75, 4986705],
        [29476, 77.1, 56943299],
        [31476, 75.4, 78958237],
        [28666, 78.1, 254830],
        [1777, 57.7, 870601776],
        [29550, 79.1, 122249285],
        [2076, 67.9, 20194354],
        [12087, 72, 42972254],
        [24021, 75.4, 3397534],
        [43296, 76.8, 4240375],
        [10088, 70.8, 38195258],
        [19349, 69.6, 147568552],
        [10670, 67.3, 53994605],
        [26424, 75.7, 57110117],
        [37062, 75.4, 252847810]
    ]

    x_lst = [v[0] for v in data]
    y_lst = [v[1] for v in data]
    extra_data = [v[2] for v in data]
    chart = Scatter("散点图-加入第三维度数据")
    chart.add("scatter", x_lst, y_lst, extra_data=extra_data, is_visualmap=True,
              visual_dimension=2, visual_orient='horizontal',
              visual_type='size', visual_range=[254830, 1154605773],
              visual_text_color='#000')
    page.add(chart)

    chart = Scatter("散点图-画pyecharts")
    v1, v2 = chart.draw(os.path.join(".", "data", "pyecharts.png"))
    chart.add("pyecharts", v1, v2, is_random=True)
    page.add(chart)

    chart = Scatter("散点图-画爱心", width=800, height=480)
    v1, v2 = chart.draw(os.path.join(".", "data", "love.png"))
    chart.add("Love", v1, v2)
    page.add(chart)

    chart = Scatter("散点图-画火辣Bra", width=1000, height=480)
    v1, v2 = chart.draw(os.path.join(".", "data", "cup.png"))
    chart.add("Cup", v1, v2)
    page.add(chart)

    chart = Scatter("散点图-画性感Bra", width=1000, height=480)
    v1, v2 = chart.draw(os.path.join(".", "data", "cup.png"))
    chart.add("Cup", v1, v2, label_color=["#000"])
    page.add(chart)

    return page