# -*- coding: utf-8 -*-

from wox import Wox
import requests
import json

class TranslateCiBa(Wox):

    def query(self, query):
        out = requests.get(f"http://fy.iciba.com/ajax.php?a=fy&f=auto&t=auto&w={query}").json()

        # 输入英文时
        if out['status'] == 0:
            mean = out['content']['word_mean'][0]

        # 输入中文时
        elif out['status'] == 1:
            mean = out['content']['out']

        else:
            mean = "get nothing"

        results = []
        results.append({
            "Title": "translate",
            "SubTitle": f"翻译: {mean}",
            "IcoPath":"Images/app.ico",
            "ContextData": "ctxData"
        })
        return results

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

if __name__ == "__main__":
    TranslateCiBa()
