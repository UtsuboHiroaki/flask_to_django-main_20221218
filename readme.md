# katoさんdjangoアプリ

## 導入

1. 導入先のディレクトリを作る

2. 導入先のディレクトリに移動する

3. 以下のコマンドを実行する

   ```git clone https://github.com/k-brahma/flask_to_django.git .```

***

## 起動まで

1. 仮想環境を作る

``` shell
python -m venv venv
```

2. 仮想環境に入る

``` shell
venv\Scripts\activate
```

3. 必要なパッケージをインストール

```shell
pip install -r requirements.txt
```

4. マイグレーション(データベースの設定)

```shell
python manage.py migrate
```

5. ローカルサーバーを起動

```shell
python manage.py runserver
```

(サーバの終了は、 [Ctrl] + [C] で)

6. ブラウザで管理画面にログイン

`http://127.0.0.1:8000/admin/` からログインできることを確かめる

動作確認できたら、 [Ctrl] + [C] でいったんサーバを止める。

***

## サンプルデータの投入

1. 管理画面ログイン用のスーパーユーザーを作成

```shell
python manage.py createsuperuser
```

2. fixture からデータをロード

```shell
python manage.py loaddata fixtures/metal_metal.json
python manage.py loaddata fixtures/stock_stock.json
```

サンプルデータ投入が済んだら、以下のページ等で表示を確かめてください。  
`http://127.0.0.1:8000/metal/`  
`http://127.0.0.1:8000/stock/`

***

## おつかされまでした！！

<span style="color: red;">**以上で、テスト環境構築作業は終わりです！**</span>
***

## <span style="color: red;">**注意! 以下は補足情報ですので、実行の必要はありません！**</span>

### python manage.py runserver をしてもブラウザでページを表示できない場合は？

> 補足:  
> ブラウザが開かない場合は、ローカルサーバを終了して、ポート番号を変更して再度起動してみてください。  
> 以下は、ポート 8001 でサーバを起動する例です。
>
> ```shell
> python manage.py runserver 8001
> ```
> 上記の例であれば、ブラウザでの動作確認時には、 8000 だったところを 8001 に読み替えて動作確認することになります。  
> 例: `http://127.0.0.1:8001/metal/'

### fixtures ディレクトリ内にある、jsonファイルについて

> データベーステーブルの簡易バックアップを以下のコマンドで生成できます。
>
> ```shell
> python manage.py dumpdata metal.metal --indent 2 --format json > fixtures/metal_metal.json
> python manage.py dumpdata stock.stock --indent 2 --format json > fixtures/stock_stock.json
> ```
> windows環境で作成した場合は、テキストエディタ等で開いて UTF-8 (BOMなし) に変換してください。
