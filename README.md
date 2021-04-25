# survey_piano_fingering

## 背景

    - 手の大きさ、稼働域といった個人差
    - 演奏するテンポや、フレーズに対するふさわしさ
    - １音符内での替え指、１指で２音以上を弾く（必ずしも音符と指番号が１対１ではない）
    - アーティキュレーションなどの表現（必ずしも弾きやすい指で弾くわけではない）
    - ペダリング、音長の省略といった補助
    - 曲の時代背景（古典運指など）
    - ミニ鍵盤など鍵盤の大きさによる違い

## 運指

### 古典運指

http://www.scholabachen.com/usui_invention.html
> 今日一般に用いられている運指法は、音階が自然に流れるようになることをモットーに発想されたものであり、これこそが楽曲をより早く、確実に再現するための第一歩であると考えられている。
> 今日のものと16世紀の運指法との間に見られるこの違いはどこから来ているのかを調べると、その相違は各時代に固有の考えに基づいているものであることが分かる。つまり16世紀のそれは「良い音」に対して「良い指」を、「悪い音」に対して「悪い指」を用いる、という考えである。

https://ontomo-mag.com/article/interview/minako-tsukatani-goldberg/
> オルガンにはオルガンの奏法、演奏習慣というものがあり、ピアノでそれをやると、まったくうまくいきません。ところが、トイピアノにはバッハの時代の古典運指法が合っているんです。

http://lepetitclavecin.hatenablog.com/entry/2017/02/16/190000
> バッハをメインに弾くなら、上はレまであれば問題ないと思います。

## ソフトウェア

ピアノマスターdp
https://cm.kawai.jp/products/pmdp/

運指レッスン フィンガリ‪ン‬
https://apps.apple.com/jp/app/%E9%81%8B%E6%8C%87%E3%83%AC%E3%83%83%E3%82%B9%E3%83%B3-%E3%83%95%E3%82%A3%E3%83%B3%E3%82%AC%E3%83%AA%E3%83%B3/id942390847

## 楽譜

https://www.amazon.co.jp/dp/4276434130

https://www.amazon.co.jp/dp/4401029089

https://www.amazon.co.jp/dp/4276401593

## アニメーション生成

https://www.vice.com/en/article/v7m8xd/watch-these-ai-hands-attempt-to-play-an-unplayable-song-on-the-piano

https://qiita.com/yamatohkd/items/0f5b9b031ec0976d872a

## 録画

https://sairie.com/movie-sp/

https://pf.classicmusic.tokyo/rec/

https://seminar.piano.or.jp/news/2020/06/entry_265.html

## Reference repositories

https://github.com/serenado/PianoFingeringProject

https://github.com/marcomusy/pianoplayer

https://github.com/Guwalgiya/Piano-Fingering-Generators

https://github.com/maxhirsch/Piano-Fingering-Prediction

https://github.com/mpg/pypiano-fingers

## Datasets

PIG Dataset
https://beam.kisarazu.ac.jp/~saito/research/PianoFingeringDataset/index-ja.html

> PIG データセッ
トは西洋クラシック作曲家のピアノ曲から成り，ピアノ演
奏者により付けられた運指が含まれている．現在，150 曲
の楽曲が収められており，各楽曲には一つあるいは複数の
運指が与えられている．なるべく多様なスタイルの音楽を
含めるため，少量の楽曲の全曲に対して運指を付けるので
はなく，多くの曲の一部分に対して運指のラベル付けを
してある．運指付けされた部分の典型的な長さは，楽譜 1
ページ程度で，小節数は約 20，音符数は約 300 である．

MAESTRO
http://createwith.ai/dataset/20181106/1358

> インターネット上のピアノ演奏コンペティション International Piano-e-Competition でのピアニストの演奏を集めることで作成されており...演奏数1,184，曲数430 ものデータが用意されており，ピアノ演奏のデータセットとしては現時点で最大規模のデータセット
