# A-Common-Matplotlib-API

# Requires

matplotlib = 3.1.1

numpy = 1.16.5

# 饼状图

样式图例：

![pie](https://user-images.githubusercontent.com/49380927/165210670-f8fbb3c1-d74e-4f97-9eb8-e223eaf16b30.png)

参数说明：

`values`: 输入为`列表`或者 `numpy` 对象。如果列表求和不为100，则会带权平均至100。

`labels`: 输入为`列表`或者 `numpy` 对象。每一块对应的标签。

`explode_mode`: 输入为 `字符串`。`highlight`: 高亮最大占比区域；`all`: 高亮所有区域；其他输入则不高亮。默认为 None。

`explode_degree`: 输入为`浮点数。指的是高亮程度。当且仅当 `explode_mode` 为 `highlight` 和 `all` 才有效。默认值为 0.1

`autopct`: 输入为`字符串`。是否显示每个饼里面的值，以及如果显示的话保留小数点后几位。比如 '%.2f'。默认为 None。

`title`: 输入为`字符串`。表头名字。默认为 None

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 折线图

样式图例：

![plot](https://user-images.githubusercontent.com/49380927/165210719-4edc3332-e404-4d5d-8e41-2098335b677e.png)

参数说明：

`xs`: 输入为 `列表` 或 `numpy 对象`。横坐标刻度。

`ys`: 输入为 `列表` 或 `numpy 对象`。横坐标的值。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`is_text`: 输入为 `boolean`。`True`: 在折线图中每个点写上具体值。`False`: 不写文字。默认为 False。

`text_pos`: 输入为 `浮点数`。折线图中每个点的字距离该点的垂直距离。当且仅当 `is_text == True` 时有效。默认为 0.0。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 柱状图

样式图例：

![bar](https://user-images.githubusercontent.com/49380927/165210784-06c565b1-6d2d-4237-aada-f669bd96e917.png)

参数说明：

`xs`: 输入为 `列表` 或 `numpy 对象`。横坐标刻度。

`ys`: 输入为 `列表` 或 `numpy 对象`。横坐标的值。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`is_text`: 输入为 `boolean`。`True`: 在折线图中每个点写上具体值。`False`: 不写文字。默认为 False。

`text_pos`: 输入为 `浮点数`。折线图中每个点的字距离该点的垂直距离。当且仅当 `is_text == True` 时有效。默认为 0.0。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 带折线图的柱状图

样式图例：

![bar_with_plot](https://user-images.githubusercontent.com/49380927/165210809-89b67640-5324-40c4-94a3-b2b1af6358fb.png)

参数说明：

`xs`: 输入为 `列表` 或 `numpy 对象`。横坐标刻度。

`ys`: 输入为 `列表` 或 `numpy 对象`。横坐标的值。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`is_text`: 输入为 `boolean`。`True`: 在折线图中每个点写上具体值。`False`: 不写文字。默认为 False。

`text_pos`: 输入为 `浮点数`。折线图中每个点的字距离该点的垂直距离。当且仅当 `is_text == True` 时有效。默认为 0.0。

`plot_color`: 输入为 `字符串`。折线图的颜色，16进制表示。默认为 `#ff85c0`。

`bar_color`: 输入为 `字符串`。柱状图的颜色，16进制表示。默认为 `#69c0ff`。

`bar_transparency`: 输入为 `浮点数`。数值区间为 [0, 1]，用于表示柱状图的透明程度。默认为 0.5。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`line_style`: 输入为 `字符串`。折线图的样式。'--': 虚线，'-': 点划线，'': 实线。默认为 '--'。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 直方图

样式图例：

![hist](https://user-images.githubusercontent.com/49380927/165210843-0c2f4994-8cee-4e19-a096-a0786f507901.png)


![hist frequency](https://user-images.githubusercontent.com/49380927/165210852-32f049b5-6441-4673-b56b-b323d2ae1eeb.png)


参数说明：

`ys`: 输入为 `列表` 或 `numpy 对象`。横坐标的值。

`bins`: 输入为 `int`。直方图划分的区间数。比如 `bins = 50` 就是有50个柱子。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`is_frequency`: 输入为 `boolean`。`True`: 纵坐标变为频率，`False`: 纵坐标为数目。上图1为 `is_frequency == False`，上图2为 `is_frequency == True`。 默认为 False。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 带折线图的直方图

样式图例：

![hist with plot](https://user-images.githubusercontent.com/49380927/165210876-f38d612f-f5b2-4548-af31-d09fd346a0a4.png)

参数说明：

`ys`: 输入为 `列表` 或 `numpy 对象`。横坐标的值。

`bins`: 输入为 `int`。直方图划分的区间数。比如 `bins = 50` 就是有50个柱子。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`is_frequency`: 输入为 `boolean`。`True`: 纵坐标变为频率，`False`: 纵坐标为数目。 默认为 False。

`plot_color`: 输入为 `字符串`。折线图的颜色，16进制表示。默认为 `#ff85c0`。

`hist_color`: 输入为 `字符串`。柱状图的颜色，16进制表示。默认为 `#69c0ff`。

`hist_transparency`: 输入为 `浮点数`。数值区间为 [0, 1]，用于表示柱状图的透明程度。默认为 0.5。

`line_style`: 输入为 `字符串`。折线图的样式。'--': 虚线，'-': 点划线，'': 实线。默认为 '--'。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 多折线图

样式图例：

![multi plot](https://user-images.githubusercontent.com/49380927/165210891-d9a462e5-6c3a-49d1-b3a8-5a9561601afc.png)

参数说明：

`xs`: 输入为 `列表` 或 `numpy 对象`。`shape`: [n]，其中 `n` 为有多少个 `x`。横坐标刻度。

`ys`: 输入为 `列表` 或 `numpy 对象`。`shape`: [m, n]，其中 `n` 为有多少个 `x`，`m` 为需要画多少个折线。纵坐标刻度。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。

# 多柱状图

样式图例：

![multi bar](https://user-images.githubusercontent.com/49380927/165210912-1773401c-8008-49ef-bd95-8bba45c6b84e.png)

参数说明：

`x_names`: 输入为 `列表` 或 `numpy 对象`。`shape`: [n]，其中 `n` 为有多少组柱子。横坐标刻度。

`ys`: 输入为 `列表` 或 `numpy 对象`。`shape`: [m, n]，其中 `n` 为有多少组柱子，`m` 为每组柱子有多少个柱子。纵坐标刻度。

`labels`: 输入为 `列表`。`shape`: [m]，其中 `m` 为每组柱子有多少个柱子。i.e. 每个柱子代表的含义。比如上图中的 `P`、`R`、`F1`。

`total_width`: 输入为 `浮点数`。取值范围为 (0, 1]。对应每组柱子的总宽度。当 `total_width == 1` 时，每两组柱子之间每个空白。默认为 0.8。

`xlabel`: 输入为 `字符串`。横坐标的名字。默认为 None。

`ylabel`: 输入为 `字符串`。纵坐标的名字。默认为 None。

`title`: 输入为 `字符串`。表头名。默认为 None。

`xlim`: 输入为 `列表` 或 `元组`。横坐标的刻度范围。比如 [0, 10]。默认为 None。

`ylim`: 输入为 `列表` 或 `元组`。纵坐标的刻度范围。比如 [0, 10]。默认为 None。

`is_text`: 输入为 `boolean`。`True`: 在折线图中每个点写上具体值。`False`: 不写文字。默认为 False。

`text_pos`: 输入为 `浮点数`。折线图中每个点的字距离该点的垂直距离。当且仅当 `is_text == True` 时有效。默认为 0.0。

`save_path`: 输入为`字符串`。需要保存的路径以及保存格式。比如 'test.pdf'。如果 save_path 为空则不保存文件。默认为 None。
