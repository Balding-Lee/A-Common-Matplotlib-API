import matplotlib.pyplot as plt
import numpy as np
import warnings


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw_texts(plt_instance, xs, ys, height_pos):
    """
    在每个 x 轴对应的位置绘制上 y 轴的数值
    :param plt_instance: Object
            matplotlib 的实例化对象
    :param xs: list or array
            横坐标
    :param ys: list or array
            纵坐标
    :param height_pos: double
            折线图中每个点的文本距离原本点的垂直距离
    """
    for x, y in zip(xs, ys):
        plt_instance.text(x, y + height_pos, y, ha='center', va='bottom')


def draw_pie(values, labels, explode_mode=None, explode_degree=0.01, autopct=None,
             title=None, save_path=None):
    """
    绘制饼状图
    :param values: list or ndarray
            饼状图中每一块的占比
            如果列表求和不为 100, 则会平均全部数据直至求和为 100
    :param labels: list or ndarray
            每一块值对应的标签
    :param explode_mode: str
            'highlight': 高亮扇形图最大的区域
            'all': 所有区域全部高亮
            default: None
    :param explode_degree: double
            高亮的程度, 仅在 explode_mode 不为 None 时有效
            default: 0.1
    :param autopct: str
            饼状图中的数据是否显示, 以及显示保留小数点后几位
            e.g. '%.2f'
            default: None
    :param title: str
            表头名
            default: None
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    if sum(values) != 100:
        warnings.warn('The sum of values is not 100', RuntimeWarning)

    if explode_mode == 'highlight':
        max_index = values.index(max(values))
        explode = []
        for i in range(len(values)):
            if i == max_index:
                explode.append(explode_degree)
            else:
                explode.append(0)
    elif explode_mode == 'all':
        explode = [explode_degree] * len(values)
    else:
        explode = None
    plt.pie(values, labels=labels, explode=explode, autopct=autopct)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()


def draw_single_line(xs, ys, xlabel=None, ylabel=None, title=None, is_text=False,
                     text_pos=0.0, xlim=None, ylim=None, save_path=None):
    """
    绘制单条折线图
    :param xs: list or ndarray
            横坐标
    :param ys: list or ndarray
            纵坐标
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param is_text: bool
            True: 在每个点上绘制上 y 轴的值
            False: 不绘制 y 轴值
            default: False
    :param text_pos: double
            折线图中每个点的文本距离原本点的垂直距离
            只有 is_text == True 时有效
            default: 0.0
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    plt.plot(xs, ys)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if is_text:
        draw_texts(plt, xs, ys, text_pos)

    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)
    plt.show()


def draw_bar_with_plot(xs, ys, xlabel=None, ylabel=None, title=None, is_text=False,
                       text_pos=0.0, plot_color='#ff85c0', bar_color='#69c0ff',
                       bar_transparency=0.5, xlim=None, ylim=None, line_style='--',
                       save_path=None):
    """
    绘制带有折线图的柱状图
    :param xs: list or ndarray
            横坐标
    :param ys: list or ndarray
            纵坐标
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param is_text: bool
            True: 在每个点上绘制上 y 轴的值
            False: 不绘制 y 轴值
            default: False
    :param text_pos: double
            折线图中每个点的文本距离原本点的垂直距离
            只有 is_text == True 时有效
            default: 0.0
    :param plot_color: str
            折线图的颜色, 16进制表示
            default: #ff85c0
    :param bar_color: str
            柱状图的颜色, 16进制表示
            default: #69c0ff
    :param bar_transparency: double
            [0, 1]之间的数, 用于表示柱状图的透明度
            default: 0.5
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param line_style: str
            折线图的样式
            '': 实线, '--': 虚线, '-': 点划线
            default: '--'
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    # 绘制折线图
    plt.plot(xs, ys, line_style, color=plot_color)

    # 绘制柱状图
    plt.bar(xs, ys, color=bar_color, alpha=bar_transparency)

    if is_text:
        draw_texts(plt, xs, ys, text_pos)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)
    plt.show()


def draw_single_bar(xs, ys, xlabel=None, ylabel=None, title=None, is_text=False,
                    text_pos=0.0, xlim=None, ylim=None, save_path=None):
    """
    绘制单一柱状图
    :param xs: list or ndarray
            横坐标
    :param ys: list or ndarray
            纵坐标
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param is_text: bool
            True: 在每个点上绘制上 y 轴的值
            False: 不绘制 y 轴值
            default: False
    :param text_pos: double
            折线图中每个点的文本距离原本点的垂直距离
            只有 is_text == True 时有效
            default: 0.0
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    plt.bar(xs, ys)

    if is_text:
        draw_texts(plt, xs, ys, text_pos)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def draw_hist(ys, bins, xlabel=None, ylabel=None, title=None, xlim=None, ylim=None,
              is_frequency=False, save_path=None):
    """
    绘制直方图
    :param ys: list or ndarray
            纵坐标
    :param bins: int
            直方图划分的区间数
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param is_frequency: bool
            True: 纵坐标变为频率
            False: 纵坐标为数目
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    plt.hist(ys, bins=bins, density=is_frequency)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def draw_hist_with_plot(ys, bins, xlabel=None, ylabel=None, title=None, xlim=None,
                        ylim=None, is_frequency=False, plot_color='#ff85c0',
                        hist_color='#69c0ff', hist_transparency=0.5,
                        line_style='--', save_path=None):
    """
    绘制直方图与折线图
    :param ys: list or ndarray
            纵坐标
    :param bins: int
            直方图划分的区间数
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param is_frequency: bool
            True: 纵坐标变为频率
            False: 纵坐标为数目
    :param plot_color: str
            折线图的颜色, 16进制表示
            default: #ff85c0
    :param hist_color: str
            柱状图的颜色, 16进制表示
            default: #69c0ff
    :param hist_transparency: double
            [0, 1]之间的数, 用于表示柱状图的透明度
            default: 0.5
    :param line_style: str
            折线图的样式
            '': 实线, '--': 虚线, '-': 点划线
            default: '--'
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    hist = plt.hist(ys, bins=bins, density=is_frequency, color=hist_color,
                    alpha=hist_transparency)

    # hist[0]: 每个柱的 y 轴坐标
    # hist[1]: 每个柱的最左边的 x 轴坐标
    # 这里用最笨的办法来计算每个柱子的宽度,
    # 由于我们需要的是每个柱子中间的坐标, 所以先求得每个柱子的横坐标需要加上多少
    # 然后每个横坐标加上这个计算后的值
    half_weight = (hist[1][1] - hist[1][0]) / 2
    # 这里只取 [: bins] 的大小是因为直方图的分隔数为 bins + 1
    xs = np.array(hist[1][: bins]) + half_weight

    plt.plot(xs, hist[0], line_style, color=plot_color)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def draw_multi_plot(xs, ys, xlabel=None, ylabel=None, title=None,
                    xlim=None, ylim=None, save_path=None):
    """
    绘制多个折线图
    :param xs: list or ndarray
            shape: [n], n 是数据规模
            横坐标
    :param ys: list or ndarray
            shape: [m, n], m 是需要绘制的条数, n 是数据规模
            纵坐标
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    """
    for i in range(len(ys)):
        plt.plot(xs, ys[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if save_path:
        plt.savefig(save_path)

    plt.show()


def draw_multi_bar(x_names, ys, labels, total_width=0.8, xlabel=None, ylabel=None,
                   title=None, xlim=None, ylim=None, is_text=False, text_pos=0.0,
                   save_path=None):
    """
    绘制多个柱状图
    :param x_names: list or ndarray
            shape: [n], n 是数据规模
            横坐标
    :param ys: list or ndarray
            shape: [m, n], m 是需要绘制的条数, n 是数据规模
            纵坐标
    :param labels: list
            shape: [m], m 是需要绘制的条数
            每个柱子代表的含义
    :param total_width: double
            (0, 1], 每个 x 的柱子对应的总宽度
    :param xlabel: str
            横坐标的表示
    :param ylabel: str
            纵坐标表示
    :param title: str
            表头名
            default: None
    :param xlim: list or tuple
            横坐标范围
            default: None
    :param ylim: list or tuple
            纵坐标范围
            default: None
    :param is_text: bool
            True: 在每个点上绘制上 y 轴的值
            False: 不绘制 y 轴值
            default: False
    :param text_pos: double
            折线图中每个点的文本距离原本点的垂直距离
            只有 is_text == True 时有效
            default: 0.0
    :param save_path: str
            保存路径, 如果设置了保存路径, 则保存文件, 否则不保存
            default: None
    total_width: 柱状图总宽度,
    """
    if total_width <= 0 or total_width > 1:
        raise IndexError('total_width must be in (0, 1], total_width is: %d' % total_width)

    x_indices = np.arange(len(x_names))  # 横坐标范围
    n = len(ys)  # n: 一共多少个柱子
    width = total_width / n  # 每个柱子的宽度

    x_start = x_indices - total_width / 2 + width / 2

    xs = []
    for i in range(n):
        if not xs:
            xs.append(x_start)
        else:
            xs.append(xs[-1] + width)

    for i in range(n):
        plt.bar(xs[i], ys[i], width=width, label=labels[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(xlim)
    plt.ylim(ylim)

    if is_text:
        for x, y in zip(xs, ys):
            draw_texts(plt, x, y, text_pos)

    plt.xticks(x_indices, x_names)
    plt.legend()

    if save_path:
        plt.savefig(save_path)

    plt.show()


