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
    python manage.py loaddata fixtures/stock_stockprice.json
    ```

6. 管理画面ログイン用のスーパーユーザーを作成

    ```shell
    python manage.py createsuperuser
    ```

7. ローカルサーバーを起動

    ```shell
    python manage.py runserver
    ```

8. ブラウザで管理画面にログイン

   `http://127.0.0.1:8000/admin/` からログインできることを確かめる

