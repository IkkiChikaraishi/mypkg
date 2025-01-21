<!--
  SPDX-FileCopyrightText:2025 Ikki Chikaraishi
  SPDX-Licence-Identifier:BSD-3-Clause
-->
# memory_pub
ロボットシステム学の課題2用に作成したプログラムです。
[![test](https://github.com/IkkiChikaraishi/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/IkkiChikaraishi/mypkg/actions/workflows/test.yml)


## パッケージの概要
現在のパソコンのメモリに関する情報を表示するros2パッケージです。

# 導入方法
このパッケージでは```psutil```というライブラリを使用するため、下記のコマンドを打ってライブラリのインストールを行ってください。
```
$ pip install psutil
```

# ノードの詳細
## トピック
### total_memory
- このトピックに、ノードがパソコンのメモリの合計に関するメッセージを送信します。

### used_memory
- このトピックに、ノードが現在使用されているメモリの合計に関するメッセージを送信します。

### free_memory
- このトピックに、ノードが現在使用されておらず、すぐに利用できるメモリの合計に関するメッセージを送信します。

## memory_pubノード
0.5秒ずつ、パソコンのメモリの合計、現在使用されているメモリ、現在利用されておらず、すぐに利用できるメモリをそれぞれ表示するノードです。

## listenerノード
テスト用のノードです。


## 使用例
以下のコマンドを入力することで、両ノードを同時実行することができます。
```
$ ros2 launch mypkg memory_listen.launch.py
```
実行結果として以下のように、パソコンのメモリの合計、現在使用されているメモリ、現在利用されておらず、すぐに利用できるメモリの情報が順番に表示されていきます。
```
[listener-2] [INFO] [1737443225.782169239] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443225.782808813] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443226.265508877] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443226.266949883] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443226.268487247] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443226.766349132] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443226.767371365] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443226.768864833] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443227.265621905] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443227.267210111] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443227.268948441] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443227.766039648] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443227.767610977] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443227.769017297] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443228.265920900] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443228.266942865] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443228.267734917] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443228.765613923] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443228.767274006] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443228.768974545] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443229.265188782] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443229.266487582] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443229.267716063] [listener]: Used_memory: 372924416
[listener-2] [INFO] [1737443229.765275291] [listener]: Free_Memory: 7555915776
[listener-2] [INFO] [1737443229.766572491] [listener]: Total_Memory: 8195694592
[listener-2] [INFO] [1737443229.768124791] [listener]: Used_memory: 372924416
```


## 動作環境
- ROS2 Foxy
  - OS : Ubuntu(20.04 LTS)
- ROS2 Humble(GitHub Actions)
  - OS : Ubuntu22.04
  - Docker ryuichiueda/ubuntu22.04-ros2:latest

## 参考資料
- https://chantastu.hatenablog.com/entry/2023/07/15/114657
- https://qiita.com/tochisuke221/items/e95216cd8b2ccbf1a5ca

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- ⓒ 2024 Ikki Chikaraishi
- このパッケージのコードの一部は、下記のものを、本人の許可を得て自身の著作としたものです。
  - https://github.com/ryuichiueda/emcl2/blob/master/.github/workflows/test.yml
