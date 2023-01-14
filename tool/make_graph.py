# モジュール
import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# 定数
GRAPH_SIZE_WIDTH = 15
GRAPH_SIZE_HEIGHT = 8

FONT_SIZE = 10

MAIN_TITLE_NAME = "ECS使用量"
X_TITLE_NAME = "経過時間(分)"
Y_TITLE_NAME = "起動台数(台)"

X_MIN = 0
X_MAX = 76
Y_MIN = 0
Y_MAX = 4080

X_INTERVAL = 5
Y_INTERVAL = 240

ROTATION = 90

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

LOC = 0

GRID = True

# クラス
class Graph:
    def __init__(self, x, y, marker, color, label):
        self.x = x
        self.y = y
        self.marker = marker
        self.color = color
        self.label = label


    # 関数
    def main(self, graph):
        # グラフの設定
        #plt.style.use('ggplot')                    #グラフのスタイル
        plt.rcParams['figure.figsize'] = [15, 8]   # グラフサイズ設定
        plt.rcParams["font.size"] = 10             # 文字の大きさ
        #plt.rcParams["font.family"] = "MS Gothic"  # 文字のフォント
        plt.title("ECS使用量")    # グラフのタイトル
        plt.xlabel("経過時間(分)")                # x軸のタイトル
        plt.ylabel("起動台数(台)")                     # y軸のタイトル
        plt.xlim([0, 76])                        # x軸の数値の範囲
        plt.ylim([0, 4080])                          # y軸の数値の範囲

        plt.xticks(np.arange(0, 75, 5))        # x軸のメモリの間隔指定
        plt.yticks(np.arange(0, 4081, 240))     # y軸のメモリの間隔指定

        plt.xticks(rotation=90)



        x1 = [i for i in range(74)]
        y1 = [0, 240, 560, 880, 880, 1040, 1200,
            1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
            2080, 2160, 2240, 2320, 2400, 2480, 2520, 2600, 2680, 2740,
            2820, 2900, 2980, 3060, 3140, 3220, 3300, 3380, 3460, 3540,
            3620, 3700, 3780, 3860, 3940, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 2000, 0
            ]

        x2 = [i for i in range(74)]
        y2 = [0, 240, 560, 880, 880, 1040, 1200,
            1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
            2080, 2160, 2240, 2320, 2400, 2480, 2520, 2600, 2680, 2740,
            2820, 2900, 2980, 3060, 3140, 3220, 3300, 3380, 3460, 3540,
            3620, 3700, 3780, 3860, 3940, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000,
            4000, 4000, 4000, 4000, 4000, 2000, 0
            ]

        x3 = [i for i in range(74)]
        y3 = [0, 240, 560, 880, 880, 1040, 1200,
            1280, 1360, 1440, 1520, 1600, 1680, 1760, 1840, 1920, 2000,
            2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
            2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
            2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
            2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
            2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000,
            2000, 2000, 2000, 2000, 2000, 1000, 0
            ]


        #plt.scatter(x, y)  # 点だけ
        plt.plot(x1, y1, marker="o", color="blue", label='smpdgjd-sawara-workers-cluster')      # 折れ線
        plt.plot(x2, y2, marker="^", color="red", label='smpdgjd-sawara-workers-cluster2')      # 折れ線
        plt.plot(x3, y3, marker="v", color="green", label='別リージョン')      # 折れ線
        plt.legend(loc=0)  # 凡例
        plt.grid()
        #plt.savefig("graph")
        plt.show()

graph = []
graph.append(Graph(X1_LIST, Y1_LIST, MARKER1, COLOR1, LABEL1))
#graph.append(Graph(X2_LIST, Y2_LIST, MARKER2, COLOR2, LABEL2))
#graph.append(Graph(X3_LIST, Y3_LIST, MARKER3, COLOR3, LABEL3))

Graph.main(graph)