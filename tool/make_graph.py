# モジュール
import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# 定数群
GRAPH_SIZE_WIDTH = 15          # グラフの幅
GRAPH_SIZE_HEIGHT = 8          # グラフの高さ
FONT_SIZE = 15                 # 目盛りのフォントサイズ
MAIN_TITLE_NAME = "ECS使用量"  # グラフのタイトル名
X_TITLE_NAME = "経過時間(分)"  # x軸のタイトル
Y_TITLE_NAME = "起動台数(台)"  # y軸のタイトル
MAIN_TITLE_SIZE = 30         # グラフのタイトルのサイズ
X_TITLE_SIZE = 20            # x軸のタイトルのサイズ
Y_TITLE_SIZE = 20            # y軸のタイトルのサイズ
X_MIN = 0                      # x軸の最小値
X_MAX = 75                     # x軸の最大値
Y_MIN = 0                      # y軸の最小値
Y_MAX = 4080                   # y軸の最大値
X_INTERVAL = 5                 # x軸の目盛間隔
Y_INTERVAL = 240               # y軸の目盛間隔
ROTATION = 0                   # メモリの数値orテキストの回転
LOC = 0                        # グラフの凡例
LOC_SIZE = 15                  # グラフの凡例のサイズ
GRID = True                    # グリッド線を出力するか
GRID_BELOW = True              # グリッド線を背面にするか

# グラフ1
X1_LIST = [i for i in range(74)]
Y1_LIST = [
        0, 240, 560, 880, 880, 1040, 1200,
        1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
        2080, 2160, 2240, 2320, 2400, 2480, 2520, 2600, 2680, 2740,
        2820, 2900, 2980, 3060, 3140, 3220, 3300, 3380, 3460, 3540,
        3620, 3700, 3780, 3860, 3940, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 2000, 0
        ]
MARKER1 = "o"
COLOR1 = "blue"
LABEL1 = 'smpdgjd-sawara-workers-cluster'
GRAPH_TYPE1 = 'plot'
LINE_WIDTH1 = 3

# グラフ2
X2_LIST = [i for i in range(74)]
Y2_LIST = [0, 240, 560, 880, 880, 1040, 1200,
        1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
        2080, 2160, 2240, 2320, 2400, 2480, 2520, 2600, 2680, 2740,
        2820, 2900, 2980, 3060, 3140, 3220, 3300, 3380, 3460, 3540,
        3620, 3700, 3780, 3860, 3940, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
        4000, 4000, 4000, 4000, 4000, 2000, 0
        ]
MARKER2 = "^"
COLOR2 = "red"
LABEL2 = 'smpdgjd-sawara-workers-cluster2'
GRAPH_TYPE2 = 'plot'
LINE_WIDTH2 = 3

# グラフ3
X3_LIST = [i for i in range(74)]
Y3_LIST = [0, 240, 560, 880, 880, 1040, 1200,
        1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
        2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
        2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
        2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
        2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
        2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
        2000, 2000, 2000, 2000, 2000, 1000, 0
        ]
MARKER3 = "v"
COLOR3 = "green"
LABEL3 = '別リージョン'
GRAPH_TYPE3 = 'plot'
LINE_WIDTH3 = 3


# クラス
class Graph:
    def __init__(self, x, y, marker, color, label, type, line_width):
        self.x = x
        self.y = y
        self.marker = marker
        self.color = color
        self.label = label
        self.type = type
        self.line_width = line_width


# 関数
def main(graph):
    # グラフの設定
    #plt.style.use('ggplot')                    #グラフのスタイル
    plt.rcParams['figure.figsize'] = [GRAPH_SIZE_WIDTH, GRAPH_SIZE_HEIGHT]   # グラフサイズ設定
    plt.rcParams["font.size"] = FONT_SIZE             # 文字の大きさ
    plt.rcParams['axes.axisbelow'] = GRID_BELOW       # グリッド線を背面にするか
    #plt.rcParams["font.family"] = "MS Gothic"  # 文字のフォント
    plt.title(MAIN_TITLE_NAME, fontsize=MAIN_TITLE_SIZE)     # グラフのタイトル
    plt.xlabel(X_TITLE_NAME, fontsize=X_TITLE_SIZE)       # x軸のタイトル
    plt.ylabel(Y_TITLE_NAME, fontsize=Y_TITLE_SIZE)       # y軸のタイトル
    plt.xlim([X_MIN, X_MAX])                    # x軸の数値の範囲
    plt.ylim([Y_MIN, Y_MAX])                    # y軸の数値の範囲
    plt.xticks(np.arange(X_MIN, X_MAX+1, X_INTERVAL))   # x軸のメモリの間隔指定
    plt.yticks(np.arange(Y_MIN, Y_MAX+1, Y_INTERVAL))   # y軸のメモリの間隔指定
    plt.xticks(rotation=ROTATION)

    for el in graph:
        if el.type == "plot":
            plt.plot(el.x, el.y, marker=el.marker, color=el.color, label=el.label, linewidth=el.line_width)      # 折れ線
        elif el.type == "scatter":
            plt.scatter(el.x, el.y, color=el.color, label=el.label)
        elif el.type == "bar":
            plt.bar(el.x, el.y, color=el.color, label=el.label)
        else:
            raise Exception
    plt.legend(loc=LOC, prop={'size':LOC_SIZE,})  # 凡例
    if GRID:
        plt.grid()
    plt.show()

graph = []
graph.append(Graph(X1_LIST, Y1_LIST, MARKER1, COLOR1, LABEL1, GRAPH_TYPE1, LINE_WIDTH1))
graph.append(Graph(X2_LIST, Y2_LIST, MARKER2, COLOR2, LABEL2, GRAPH_TYPE2, LINE_WIDTH2))
graph.append(Graph(X3_LIST, Y3_LIST, MARKER3, COLOR3, LABEL3, GRAPH_TYPE3, LINE_WIDTH3))

main(graph)
