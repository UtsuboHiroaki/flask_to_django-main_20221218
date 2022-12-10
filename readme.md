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

4. マイグレーション

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
ブラウザが開かない場合は、ローカルサーバを終了して、ポート番号を変更して再度起動してみてください。  
ブラウザが開かない場合は、ローカルサーバを終了して、ポート番号を変更して再度起動してみてください。  
以下は、ポート 8001 でサーバを起動する例です。

```shell
python manage.py runserver 8001
```

動作確認できたら、 [Ctrl] + [C] でいったんサーバを止める。

***

## データの投入

1. 管理画面ログイン用のスーパーユーザーを作成

```shell
python manage.py createsuperuser
```

2. fixture からデータをロード

```shell
python manage.py loaddata fixtures/metal_metal.json
python manage.py loaddata fixtures/stock_stock.json
```

## fixtures ディレクトリ内にある、jsonファイルについて

データベーステーブルの簡易バックアップを以下のコマンドで生成できます。

```shell
python manage.py dumpdata metal.metal --indent 2 --format json > fixtures/metal_metal.json
python manage.py dumpdata stock.stock --indent 2 --format json > fixtures/stock_stock.json
```

windows環境で作成した場合は、テキストエディタ等で開いて UTF-8 (BOMなし) に変換してください。

***

## 更新メモ

### 2022/11/27 15:00

- mysql用のライブラリと、関連の設定ファイルを削除しました  
  Mac, Linux では mysqlclient のインストールが一筋縄ではいかないので、 requirements.txt から削除しました。  
  関連で、 config/mysql.py を削除しました。  
  この readme.md からも関連の記述を削除しました。

#### katoさんが当初リリースされた版からの主要な変更点というか、見どころメモ:

| ファイルパス          | 変更点                                          |
|-----------------|----------------------------------------------|
| metal/models.py | データベースの列名を変更した。                              |
| metal/views.py  | 新規にページを追加した。|
| metal/urls.py   | views.py での変更を反映。                            |

| url          | 変更点
|--------------|------------------------------------|
| /metal/_/    | /metal/ の関数 view 版                 |
| /metal/_buy/ | /metal/buy/ の関数 view 版             |
| /metal/buy/  | 購入完了時に thanks ページでメッセージを表示するようにした。 |
| /stock/      | 新規追加。                              |
| /stock/buy/  | 新規追加。クラスベースのview。                  |
| /stock/_buy/ | 新規追加。関数ベースのview。                   |

### 2022/12/11 08:00

django-debug-toolbar を導入しました。  
