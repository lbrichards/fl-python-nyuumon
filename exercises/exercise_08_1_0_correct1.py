# =-=-=-=-=-=-=-=　#
#  辞書の練習      #
# =-=-=-=-=-=-=-=　#
"""
     ------   問題解説   -------
下記のmirrorless_camerasという、辞書の辞書を入力として、それぞれのカメラの
メガピクセル単価を計算し、新しい辞書を生成しましょう。

返り値の辞書は、キーをカメラ名とし、値をメガピクセル単価とします。

なお、定価のデータ型は文字列で、カンマを含んでいるため、
文字列の.replace関数を次のように使う必要があります。

    price = price_string.replace(",", "")

するとpriceを簡単にfloatに変換することができます。

"""

cameras = {
    "Sony Alpha a7 III": {"Maker": "Sony", "Max Megapixels": 24.2, "List Price (JPY)": "219,800"},
    "Fujifilm X-T4": {"Maker": "Fujifilm", "Max Megapixels": 26.1, "List Price (JPY)": "236,500"},
    "Canon EOS R5": {"Maker": "Canon", "Max Megapixels": 45, "List Price (JPY)": "541,800"},
    "Nikon Z6 II": {"Maker": "Nikon", "Max Megapixels": 24.5, "List Price (JPY)": "269,500"},
    "Panasonic Lumix GH5": {"Maker": "Panasonic", "Max Megapixels": 20.3, "List Price (JPY)": "238,000"},
    "Olympus OM-D E-M1 Mark III": {"Maker": "Olympus", "Max Megapixels": 20.4, "List Price (JPY)": "256,600"},
    "Leica SL2": {"Maker": "Leica", "Max Megapixels": 47.3, "List Price (JPY)": "1,003,000"},
    "Sigma fp": {"Maker": "Sigma", "Max Megapixels": 24.6, "List Price (JPY)": "275,000"},
    "Hasselblad X1D II 50C": {"Maker": "Hasselblad", "Max Megapixels": 50, "List Price (JPY)": "1,170,000"},
    "Ricoh GR III": {"Maker": "Ricoh", "Max Megapixels": 24.2, "List Price (JPY)": "83,600"}
}


def calculate_megapixel_unit_prices():
    mp_unit_price = {}
    for camera, spec in cameras.items():
        mpx = spec["Max Megapixels"]  # 正解例
        price = float(spec["List Price (JPY)"].replace(",", ""))  # 正解例
        mpx_unit_price = price / mpx  # 正解例
        mp_unit_price[camera] = mpx_unit_price  # 正解例
    return mp_unit_price

# データが長い場合、pprintの方が綺麗に見える
# 使用例
from pprint import pprint
pprint(calculate_megapixel_unit_prices())



# ---

from pprint import pprint

def f():
    mp_unit_price = {}
    for camera, spec in cameras.items():
        mpx = spec["Max Megapixels"]
        price = float(spec["List Price (JPY)"].replace(",", ""))
        mpx_unit_price = price / mpx
        mp_unit_price[camera] = mpx_unit_price
    return mp_unit_price


def test():
        expected = f()
        found = calculate_megapixel_unit_prices()
        if found == expected:
            print(
                f"""正解です。""")
            pprint(found)

        else:
            print(f"""
残念でした。もう一度チャレンジしましょう。""")

test()