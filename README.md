# Video Compressor Service
## 概要

このプログラムは、動画処理を行うサービスです。クライアントが指定した動画ファイルに対して、圧縮、解像度変更、アスペクト比変更、音声への変換、GIFへの変換のいずれかの操作をリクエストできます。

## インストール


`ffmpeg-python` パッケージをインストールします。

   ```bash
   pip install ffmpeg-python
   ```

## 使い方

### 事前準備
clientファイルの中のinputファイルに変更したいファイルを入れてください
(*2GBまでのファイルにしか対応していません)


### サーバーの起動

1. `server.py` を実行してサーバーを起動します。

   ```bash
   python server.py
   ```

### クライアントからのリクエスト

1. `client.py` を実行してクライアントとして動作させます。

   ```bash
   python client.py
   ```

2. コマンド番号を次のように入力します。
   - 1: 動画の圧縮
   - 2: 解像度の変更
   - 4: 音声ファイルに変換
   - 5: GIFへの変換
3. 変換するファイル名を指定します。
4. 出力ファイル名を入力します。
5. リクエストがサーバーに送信され、処理された動画ファイルがダウンロードされます。

## 注意事項

- サーバーはローカルホスト（localhost）上でのみ動作します。
- 処理された動画ファイルは、クライアントと同じディレクトリに保存されます。
