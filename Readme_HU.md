# H.utsuboのRead.meファイル

## 2022/12/20

- 自分用のReadmeファイルを作成する

- 少し書きにくいかも
  - Visual Studio Codeで書いてみましょう
- 今日の時点では株式売買履歴のHTMLペ－ジを追加
- Markdown All in も追加した
- まあMarkdownの書き方もおぽえましょう

## 2022/12/21

- 小川先生の宿題
  - 次回迄に色々いじっていみる
  - error_views.pyが鍵かな？
  - [場所](C:\Mypython\flask_to_django-main_20221218\main\views)
- デコレータ－の解説動画は少し分からない
- djangoのフォルダ削除コマンドは便利

## 2022/12/22

- Scraypingのgitのコンフリクトを解消した
- git.ignoreを追加。今まで余計なファイルを格納しすぎていた
- 今日はやっとerror_views.pyをいじれた
- HTML変換もようやく出来た。まだ先は長いが・・

## 2022/12/24

- visual Stusio でファイル開いてみた
- 小川先生もシンプルに書いている
- 色文字の修飾と特にされていない。特に覚えないか単純なものでいいかも
- **`配色の基本`**
- `バッククォート１つで囲む`
- `Shift + @` で書くようで難しい
- EQスクレイピング久しぶりにやったが色々忘れているな
  - 手順も整えなくてはね!

![画像1](20221224231246.jpg)

- こうやったら遊べるのね

## 2022/12/25

- エクイティスクレイピングの一発版のコ－ドを修正
- 可能であればgithubで確認いただきたい
- 一応対応は出来た

## 2022/12/26

- エクイティのは明日投稿してみよう
- 今日は伊久磨さんの件で小川さんも忙しそう

1. sample01

- C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\servers\basehttp.py
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\base.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\exception.py
      - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\__init__.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\logging.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\staticfiles.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\headers.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\timer.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\middleware.py



2. 403エラーのサンプル

- C:\mypython\flask_to_django-main_20221218\main\urls.py
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\contrib\staticfiles\handlers.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\exception.py
      - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\__init__.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\logging.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\staticfiles.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\headers.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\panels\timer.py
        - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\debug_toolbar\middleware.py
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\utils\deprecation.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\exception.py
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\base.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\wsgi.py
      - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\contrib\staticfiles\handlers.py
  - C:\Users\hutsu\AppData\Local\Programs\Python\Python310\Lib\wsgiref\handlers.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\servers\basehttp.py

- C:\mypython\flask_to_django-main_20221218\main\urls.py
  - C:\mypython\flask_to_django-main_20221218\main\views\error_views.py

- C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\http\response.py

- 400
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\exceptions.py

- 500
  - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\base.py
    - C:\mypython\flask_to_django-main_20221218\venv\Lib\site-packages\django\core\handlers\exception.py


## 2022/12/27

- スクレイピングの投稿してみました
- 整理するExcelの関数が滅茶苦茶。あれでは使えないよ
- 今日は教科書を読むことにする

## 2022/12/28

- スクレイピングに対する小川先生のコメント
  - Pyhontnはスネークケース（snake_case）で
    - 単語と単語の間のスペースに、アンダースコア（_）を置く書き方のことです
    - 各単語の頭文字を小文字にすることも特徴の一つです
    - 後は波線がついていた理由が理解出来た
- 一応公開した以上。自分の作業は別ブランチでやるべきだろうな

## 2023/01/01

- 外部で使用するミニノートはまだ不要だね
  - 実家でも使いたいと思わなかった
  - それ以前にキーボードを変えないとね

## 2023/01/04

- 実家で作業したことでバグが起きていましたね
  - まあ解消出来て良かった
- 株スクレイピングの見直し
  - 現状の思い
    - キャッシュフロー計算書等の全デ－タ取った方が楽になるかもしれないね
    - 会社によって様式も異なるので全部集めてデ－タベ－スから集計した方が将来的にはいいかも
    - APIの箇所で中途半端にPanda使うのは止めてみましょうか
    - まずはAPIの方から修正してみましょう
  - APIの見直し
    - とにかく階層が深い
    - databaseをリストにしてみますか
      - 結局dataframeをリストにして加工しているくらいやからね
    - jsonの扱いも再復習しないとね
    - GitHub Copilotも導入やね
      - これは夜の作業
  - Djangoの勉強
    - models.pyを見てみましょう
      - これは朝の作業

