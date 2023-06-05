# 如何製作web API
from . import api1
import pandas as pd
from flask import jsonify


@api1.route("/stockcode")
def stockcode():
    code_dataframe = pd.read_csv("api/codeSearch.csv")
    code_dataframe1 = code_dataframe[["code", "name"]]
    all_list = code_dataframe1.values.tolist()
    python_list = [{item[0]: item[1]} for item in all_list]
    return jsonify(python_list, ensure_ascii=False)


@api1.route("/stockcode/<int:code>")
def stockname(code):
    code_dataframe = pd.read_csv("api/codeSearch.csv")
    code_dataframe1 = code_dataframe[["code", "name"]]
    try:
        name = code_dataframe1.query("code==@code")["name"].values[0]
    except IndexError:
        return "fff{code}"

    return name
