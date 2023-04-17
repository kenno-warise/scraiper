# WebScraping

簡易的なWebスクレイピングパッケージです。

このパッケージでは、「requests」ライブラリと「bs4」ライブラリが使用されています。

### インストール

```bash
$ pip install --upgrade pip

$ pip install git+https://github.com/kenno-warise/webscraping.git
```

### 使用方法

```
>>> from webscraping import Scp
>>>
>>> scp = Scp()
>>> url = 'https://...'
>>> tag = 'h5'
>>>
>>> datas = scp.set_url_and_tag(url, tag)
>>> print(datas)
[..., ..., ...]
```

「datas」の中身はリスト型として値を取得します。

Web上に特定のタグや属性が無い場合は空のリストが返ってきます。
