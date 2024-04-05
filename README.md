# Video-Compressor-Service

## 概要
ユーザーが動画ファイルをアップロードして、サーバーのリソースを使ってさまざまな動画処理を行うことができる動画圧縮サービスです

## 詳細
ユーザーは圧縮雨や解像度・アスペクト比の調整、音声変換、GIPの作成などを使いやすいインターフェースから実行できます。

また基本的な機能としては下記の機能を提供しています。

- 動画ファイルを圧縮する(圧縮度をlow,medium,highの3段階から選択できます)
- 動画の解像度を変更する
- 動画の縦横比を変更する
- 動画をオーディオに変換する
- 指定した時間範囲からGIFを作成する




## 前提条件
このサービスを実行するには、FFmpegというライブラリを事前にインストールしておく必要があります。いかに手順を示します。

### FFmpeg
FFmpegは無料のオープンソースのソフトウェアプロジェクトであり、マルチメディアファイルを扱うためのツールとライブラリ、及びオーディオや動画ファイルを変換・処理するコマンドラインユーティリティを提供しています。

1. [Download FFmpeg](https://ffmpeg.org/download.html)からダウンロードすることもできます。

2. FFmpegがインストールされたことを確認する。<br>ffmpeg version/configurationなどが表示されていれば、FFmpegのインストールができています。
```
ffmpeg -version
```

### エンコーダー
Ubuntuを利用している場合は、MP4ファイルが再生できないことがあります。

その場合は、下記記事を参考にしてエンコーダーをインストールしてください。

[Ubuntu 22.04でMP4ファイルが再生できない場合の対処法](https://blog.janjan.net/2022/08/15/ubuntu-play-mp4-movie-file/)


## 使用方法
1. inputとoutputフォルダに入っている不要なファイルを削除する
2. インプット用の動画を用意してinputフォルダに格納する
3. 1つ目のターミナル(**サーバ用ターミナル**とする)を起動する
4. サーバ用ターミナルに下記コマンドを入力する
```
python3 VCserver.py
```
5. 2つ目のターミナル(**クライアント用ターミナル**とする)を起動する
6. クライアント用ターミナルに下記コマンドを入力する
```
python3 VCclient.py
```
7. `Type in a file to upload: `と表示されたら、Inputのパスを入力する<br>
8. 下記指示が表示されたら、利用したい機能を0から4の中から選択して入力する<br>`Please enter a number from 0 to 4`<br>`0 : Compress your video`<br>`1 : Change the resolution of the video`<br>`2 : Change the aspect ratio of the video`<br>`3 : Change your video to audio`<br>`4 : Produce a GIF from time range specified yb you`
9. その後、追加で指示が表示されたら、指示に従い入力する
10. サーバ用ターミナルが動き出したら、クライアント用ターミナルに`File generated.`と表示されるまで待つ
11. `Do you want to continue ?`と表示されたら、サービスを続けるか選択する(0 : 終了する/1 : 続ける)
12. outputフォルダにダウンロードされた動画を確認する

## 開発環境
VirtualBox</br>
Ubuntu 22.04.4LTS</br>

## 使用モジュール
FFmpeg


