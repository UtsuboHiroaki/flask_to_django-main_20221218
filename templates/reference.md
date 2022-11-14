# サイト情報

## サイトパスメモ

| パス                           | コンテンツ    | メモ                              |
|------------------------------|----------|---------------------------------|
| /                            | 総合トップ    | index.html                      | 
| /about/                      | はじめての方へ  | about.html                      | 
| /metal/                      | 貴金属トップ   | metal/index.html                | 
| /metal/buy/                  | 貴金属取引    | metal/buy.html                  | 
| /metal/buy_thanks/           | 貴金属取引完了  | metal/buy_thanks.html           | 
| /metal/api/buy/              | 貴金属取引api | postのみ受けつける。該当する商品が見つからない場合は400 | 
| /metal/api/info/             | 貴金属情報api | すべてをリストで出力                      | 
| /metal/api/info/{type_name}/ | 貴金属情報api | 該当する商品が見つからない場合は404                    | 
| /stock/                      | 証券トップ    | stock/index.html                | 
| /stock/buy/                  | 証券取引     | stock/buy.html                  | 
| /stock/buy_thanks/           | 証券取引完了   | stock/buy_thanks.html           | 
| /stock/api/buy/              | 証券取引api  | postのみ受けつける。該当する商品が見つからない場合は400        |
| /stock/info/csv/             | 証券情報csv  | 全銘柄の情報をcsvファイルとして取得できる          |

***

### 貴金属の取引api

/metal/api/buy/ に以下のような json をPOSTで送信すると、貴金属を取引できる。

リクエスト例:

```json
{
  "name": "gold",
  "amount": 100,
  "email": "foo@bar.com",
  "user": "山田太郎"
}
```

レスポンス例:

```json
{
  "result": "success",
  "price": 1500
}
```

#### api リクエストのテストをコマンドラインから実行する方法(shellごとに記載):

windows powershell で実行するときは、以下のようにする。

```powershell
Invoke-RestMethod -Uri "https://flask.pc5bai.com/metal/api/buy/" -Method POST `
                  -Body (@{"name"="gold";"amount"=100;"email"="foo@bar.com";"user"="山田太郎"} | ConvertTo-Json) `
                  -ContentType "application/json; charset=utf-8"
```

windows の dos コマンドプロンプトで実行するときは、以下のようにする。

```dos
curl -X POST https://flask.pc5bai.com/metal/api/buy/ -H "Content-Type: application/json" -d "{\"name\":\"gold\",\"amount\":100,\"email\":\"foo@bar.com\",\"user\":\"taro yamada\"}"
```

linux, mac では以下でOK(いちおう動作確認済)

```bash
curl -X POST https://flask.pc5bai.com/metal/api/buy/ -H 'Content-Type: application/json' -d '{"name":"gold","amount":100,"email":"foo@bar.com","user":"taro yamada"}'
```

***

### 証券の取引api

/stock/api/buy/ に以下のような json をPOSTで送信すると、証券を取引できる。

リクエスト例:

```json
{
  "name": "orange",
  "amount": 1000,
  "email": "foo@bar.com",
  "user": "山田太郎"
}
```

レスポンス例:

```json
{
  "result": "success",
  "price": 1500
}
```

#### api リクエストのテストをコマンドラインから実行する方法(shellごとに記載):

windows powershell で実行するときは、以下のようにする。

```powershell
Invoke-RestMethod -Uri "https://flask.pc5bai.com/stock/api/buy/" -Method POST `
                  -Body (@{"name"="orange";"amount"=1000;"email"="foo@bar.com";"user"="山田太郎"} | ConvertTo-Json) `
                  -ContentType "application/json; charset=utf-8"
```

windows の dos コマンドプロンプトで実行するときは、以下のようにする。

```dos
curl -X POST https://flask.pc5bai.com/stock/api/buy/ -H "Content-Type: application/json" -d "{\"name\":\"orange\",\"amount\":1000,\"email\":\"foo@bar.com\",\"user\":\"taro yamada\"}"
```

linux, mac では以下でOK(いちおう動作確認済)

```bash
curl -X POST https://flask.pc5bai.com/stock/api/buy/ -H 'Content-Type: application/json' -d '{"name":"orange","amount":1000,"email":"foo@bar.com","user":"taro yamada"}'
```
