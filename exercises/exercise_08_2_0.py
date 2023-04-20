# =-=-=-=-=-=-=-=　#
#  辞書の練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
下記のhydro_plantsという辞書には、７つの内部辞書が含まれています。
外部辞書のキーは水力発電所の名前です。内部辞書は、
それぞれの発電所のデータを含んでいます。

内部辞書のキーの解説：
'country'は、もちろん所在国名です
'head'は（川水の）落差で、単位はメーター
'flow rate'は流量で、単位は毎秒の立方メーター(m3/s)
'capacity (MW)'は発電容量で、単位はメガワット（１００万ワット）

ここが問題です。所在国名が'China'の発電所のみを取り出して、新しい辞書
chinese_hydro_plantsを生成してください。

ここでポイントとなるのは、update()という辞書関数です。A.update(B)のように
使うと、辞書Bの中身が辞書Aへ更新されます。つまり、この場合は、

C = {}
for k,v in A.items():　# この場合の"v"は内部辞書となります
    if v["country"]=="China":
        C.update({k:v})

のようにupdateを使います。（ここでのAとBとCはあくまでも例ですから、実際の変数名は
あなたのご判断になります。

なお、上記の例では、

C.update({k:v})　でも
C[k]=v でも

結果は同じですが、前者の方が望ましい場合があるため、ぜひ覚えておいてください。


"""

hydro_plants = {
  "Three Gorges Dam": {"head": 185, "flow rate": 34000, "country": "China", "capacity (MW)": 22500},
  "Itaipu Dam": {"head": 118, "flow rate": 62200, "country": "Brazil/Paraguay", "capacity (MW)": 14000},
  "Grand Coulee Dam": {"head": 168, "flow rate": 3000, "country": "USA", "capacity (MW)": 6809},
  "Sayano-Shushenskaya Dam": {"head": 242, "flow rate": 1060, "country": "Russia", "capacity (MW)": 6400},
  "Xiluodu Dam": {"head": 278, "flow rate": 17000, "country": "China", "capacity (MW)": 13860},
  "Guri Dam": {"head": 162, "flow rate": 4300, "country": "Venezuela", "capacity (MW)": 10235},
  "Churchill Falls Generating Station": {"head": 305, "flow rate": 3400, "country": "Canada", "capacity (MW)": 5428}
}

def extract_chinese_hydro_plants():
    chinese_hydro_plants = {}
    for name, data in hydro_plants.items():
        if data['country'] == 'China':
            chinese_hydro_plants.update({name: data})
    return chinese_hydro_plants

# 使用例
from pprint import pprint
pprint(extract_chinese_hydro_plants())

# ---

from pprint import pprint

def f():
    chinese_hydro_plants = {}
    # ここにプログラムのロジックを書いてください
    return chinese_hydro_plants


def test():
        expected = f()
        found = extract_chinese_hydro_plants()
        if found == expected:
            print("正解です。")
            pprint(found)

        else:
            print(f"""
残念でした。もう一度チャレンジしましょう。""")

test()