# katoさんdjangoアプリ

## 導入

1. 導入先のディレクトリを作る

2. 導入先のディレクトリに移動する

3. 以下のコマンドを実行する

   ```git clone https://github.com/k-brahma/flask_to_django.git .```

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

5. fixture からデータをロード

    ```shell
    python manage.py loaddata fixtures/metal_metal.json
    python manage.py loaddata fixtures/stock_stock.json
    ```

6. 管理画面ログイン用のスーパーユーザーを作成

    ```shell
    python manage.py createsuperuser
    ```

7. ローカルサーバーを起動

    ```shell
    python manage.py runserver
    ```
   (サーバの終了は、 [Ctrl] + [C] で)


8. ブラウザで管理画面にログイン

   `http://127.0.0.1:8000/admin/` からログインできることを確かめる  
   ブラウザが開かない場合は、ローカルサーバを終了して、ポート番号を変更して再度起動してみてください。  
   ブラウザが開かない場合は、ローカルサーバを終了して、ポート番号を変更して再度起動してみてください。  
   以下は、ポート 8001 でサーバを起動する例です。
   ```shell
    python manage.py runserver 8001
    ```

***

manage.py コマンドでは、以下のように --settings=config.mysql オプションをつけることで、 mysql のデータベースを使う設定で起動できます。  
(ローカル環境へのmysqlデータベースのインストール/起動/データベースの作成が必要です)。

    ```shell
    python manage.py migrate --settings=config.mysql
    python manage.py runserver --settings=config.mysql
    ```

***

データベーステーブルの簡易バックアップを以下のコマンドで生成できます。
```shell
python manage.py dumpdata metal.metal --indent 2 --format json > fixtures/metal_metal.json
python manage.py dumpdata stock.stock --indent 2 --format json > fixtures/stock_stock.json
```

windows環境で作成した場合は、テキストエディタ等で開いて UTF-8 (BOMなし) に変換してください。
