# An Ergonomic Model of Keyboard Fingering for Melodic Fragments

https://www.researchgate.net/publication/249810172_An_Ergonomic_Model_of_Keyboard_Fingering_for_Melodic_Fragments
1997

> this is the first study of fingering that includes a
computational model,

始めての自動運指推定の研究
片手単旋律を対象に、Anatomy, motor constaints に基づく制約や、運指ルールから運指コストを推定する

## 目的

> The fingerings used by keyboard players are determined by a range of
ergonomic (anatomic/motor), cognitive, and music-interpretive constraints.

指同士の自然に開く距離/最大距離の定義から、音符列に対してありうる運指を生成し、
運指それぞれについて１２の規則によって運指の難易度を推定する

>  Most fingerings recommended
by pianists were among those fingerings predicted by the model to be
least difficult; but the model also predicted numerous fingerings that were
not recommended by pianists. A variety of suggestions for improving the
predictive power of the model are explored.

>  In spite
of insights of this kind, there still exists no systematic work that examines
the transduction of cognitive representations into physical movements.

演奏者の認知から運動への変換を計算的に求める研究は無かった

管楽器などは音と運指が１対１で対応するが、ピアノはそうではない

> Fingering strategies have always been of intense interest to keyboard
players, because fingering can significantly affect the technical and expressive qualities of a performance. There is rarely one “best” fingering in any
situation, some fingerings assisting precision and speed, others phrasing
and dynamic articulation, and yet others memorization;

正確性や速さ（運指の自然さ、簡単さ）、フレージングやアーティクル（演奏表現）、暗譜のしやすさ、といった要素によって望ましい運指は変わる

> A significant
component in piano instruction and pedagogy is concerned with assisting
the learner to choose fingerings that will best achieve an intended performance. There is still, however, virtually nothing in the way of direct empirical evidence to confirm or refute what pianists say.

> This paper is part of a larger project whose aim is investigate the fingering strategies of pianists of differing degrees of expertise and in different performing contexts.

> In the absence of previous research on fingering, an
important requirement is to establish some background predictions—a
baseline against which our empirical findings can be measured. 

## Model

> In its present form, the model is restricted to the right hand and deals
only with the fingering of consecutive notes in melodic fragments of limited length.

>  Previous research has
indicated that the number of notes held in working memory in advance of
the note currently being played (the eye-hand span, Sloboda, 1974) is no
more than about six and that more skilled music readers look farther ahead
than less skilled readers. Sloboda (1982) reported that professional musicians typically read about 2 s ahead of the music they are playing, a finding broadly confirmed by Goolsby (1994).

> Specifically, the input to the model is a series of pitches, which are entered as intervals in semitones above any C on the keyboard. Variations in
duration, articulation, dynamics, and other expressive features are ignored;

## Terms 

+ MaxPrac
  - the maximum practical span (MaxPrac). MaxPrac is understood as the
maximum stretch that a pianist would actually use in a musical performance to span two notes played either simultaneously or consecutively in
finger legato.

+ MinPrac
  - Minimum practical spans (MinPrac) are defined by analogy to MaxPrac
as the smallest spans a pianist would actually use in a musical performance
  - For finger pairs involving the thumb, MinPrac is the maximum distance
that a finger can pass over the thumb (or the thumb under the finger) and is
expressed as a negative number. 

## Rules

> Presently, there are 12 rules in the model

1. Stretch Rule: Assign 2 points for each semitone that an interval
exceeds MaxComf or is less than MinComf.

2. Small-Span Rule: For finger pairs including the thumb, assign 1
point for each semitone that an interval is less than MinRel. For
finger pairs not including the thumb, assign 2 points per semitone.

3. Large-Span Rule: For finger pairs including the thumb, assign 1
point for each semitone that an interval exceeds MaxRel. For finger
pairs not including the thumb, assign 2 points per semitone.

4. Position-Change-Count Rule: Assign 2 points for every full change
of hand position and 1 point for every half change. A change of hand
position occurs whenever the first and third notes in a consecutive
group of three span an interval that is greater than MaxComf or less
than MinComf for the corresponding fingers. In a full change, three
conditions are satisfied simultaneously: The finger on the second of
the three notes is the thumb; the second pitch lies between the first
and third pitches; and the interval between the first and third pitches
is greater than MaxPrac or less than MinPrac. All other changes are
half changes.

5. Position-Change-Size Rule: If the interval spanned by the first and
third notes in a group of three is less than MinComf, assign the
difference between the interval and MinComf (expressed in
semitones). Conversely, if the interval is greater than MaxComf,
assign the difference between the interval and MaxComf.

6. Weak-Finger Rule: Assign 1 point every time finger 4 or finger 5 is
used.

7. Three-Four-Five Rule: Assign 1 point every time fingers 3, 4, and 5
occur consecutively in any order, even when groups overlap.

8. Three-to-Four Rule: Assign 1 point each time finger 3 is
immediately followed by finger 4.

9. Four-on-Black Rule: Assign 1 point each time fingers 3 and 4 occur
consecutively in any order with 3 on white and 4 on black.

10. Thumb-on-Black Rule: Assign 1 point whenever the thumb plays
a black key. If the immediately preceding note is white, assign a
further 2 points. If the immediately following note is white, assign a
further 2 points.

11. Five-on-Black Rule: If the fifth finger plays a black key and the
immediately preceding and following notes are also black, assign 0
points. If the immediately preceding note is white, assign 2 points. If
the immediately following key is white, assign 2 further points.

12. Thumb-Passing Rule: Assign 1 point for each thumb- or fingerpass on the same level (from white to white or black to black).27
Assign 3 points if the lower note is white, played by a finger other
than the thumb, and the upper is black, played by the thumb.

1. 無理なく広げられる/縮められる距離よりも広い/狭い運指には２点を加える
2. MinRelよりも狭い運指には、親指を含む場合は１点、それ以外には２点を加える
3. MaxRelよりも広い運指には、親指を含む場合は１点、それ以外には２点を加える
4. 指くぐりや跳躍によるポジション移動を伴う場合、手の位置が完全に移動する場合は２点、それ以外には１点を加える。
5. MinComfよりも狭い音域でポジション移動が生じた場合、音域からMinComfを減じた点を加える。
6. ４指か５指を使った場合１点を加算する
7. ３，４，５指を連続で用いた場合（順不同）、１点を加える
8. ３指の次に４指が来た場合、１点を加える
9. 白鍵上の３指と黒鍵上の４指が連続した場合、１点を加える
10. １指で黒鍵を弾いた場合、１点を加える。直前が白鍵であった場合は２点、直後が白鍵である場合は２点を、更に加える。
11. ５指で黒鍵を弾いた場合、直前が白鍵であった場合は２点、直後が白鍵である場合は２点を加える。
12. 指くぐりに１点を加える。白鍵を弾いた状態で親指が黒鍵を弾く指くぐりには３点を加える。

これらのルールから各運指の点数difficulty valueを求める

> The algorithm described earlier can only be applied to relatively short
fragments (our implementation goes to eight notes), because the number of
possible fingerings for a fragment varies exponentially with the length of
the fragment. 

## experiments

> Seven short pieces were selected from the 160 Kurze Übungen op. 821 of Carl Czerny, as
published by Peters (Edition Nr. 2405, 1920).

> The 12 professional pianists and 3 students received the scores after participating in a companion study that involved sight-reading each piece twice. They took the
scores home before writing down their preferred fingerings. The other participants received
the scores by mail.

> They were asked to write on the score their “preferred fingerings”
for the right hand of the first two measures of each piece. In order to avoid ambiguity, they
were asked to write a finger number against each and every note. A preferred fingering was
defined as “the fingering that you would probably use in performance.”

チェルニーの練習曲を題材に、28人の演奏者の運指とモデルの出力を比較

## discussion

>　Table 4 shows that many of the fingerings chosen by the pianists were
among the fingerings predicted to be least difficult by the model. This confirms that the model encapsulates at least some of the factors that contribute to the technical difficulty of melodic legato fragments played on keyboard. The model also predicted many fingerings that were not proposed
by any of the pianists.

> model’s estimations of fingering difficulty
are roughly correct from the point of view of ergonomics but not of cognition.

人間工学的には難易度を評価できているが、認知的な負荷は反映できていないのではないか

1. Pianists may apply standard fingerings
2. Pianists may choose fingerings that are familiar from other pieces
3. The same or a similar fingering may be used when the same or similar passages recur within a single piece of music
4. Fingering patterns may be linked with low-level structural descriptions of the music, a procedure that involves musical interpretation as well as cognition.

> Clarke et al. (1997)
reported that pianists tend to use stronger fingers on metrical
accents and that changes of hand position are more likely to occur at phrase boundaries,

> No attempt has been made to incorporate the above cognitive-ergonomic
principles into the current model.

> Clarke et al. (1997) discuss several other important influences on fingering that are neglected by the present model
5. Rhythm. Other things being equal, pianists tend to use stronger
fingers at metrically stronger positions and at dynamic accents
(Bach, 1753/1957).
6. Tempo. The tendency to avoid ergonomic difficulties of the kinds
encapsulated by this model increases as tempo increases: the
higher the speed of performance, the greater the need to avoid
unnecessary movements of the hand (Czerny, 1839)
7. Articulation. A fingering that is optimal for legato playing is not
necessarily so in staccato (see, e.g., Werkenthin, 1888);
8. Register. A given fingering may be easier to play in one register
than another because of the angle the hand makes with the keyboard.
9. Style. It may be argued that the principles encapsulated by the
model are limited with regard to musical style (Neuhaus, 1958/
1973), 

> Sloboda et al. (in press) did a factor
analysis on difficulty estimates according to the separate rules for 7 of the
10 Czerny studies referred to in this paper. Five factors emerged, which
together accounted for 78% of the variance in fingerings performed by
pianists as they sight-read the studies. Rules 1, 3, 10, and 11 combined to
form a general “stretch” factor; rules 2, 4, and 5 formed a general “position change” factor; and rules 6, 7, and 8 represented “agility.” The other
two factors corresponded to the individual rules 9 and 12.

> For example, the “stretch” and “span” concepts developed here have not been central issues in historical writings. Pianists tend
to learn about these concepts intuitively, and so little guidance or discussion is needed in books that aim to give practical assistance to pianists.

> many 20th century piano
works, for example, require fingering procedures that were unknown in
earlier music. Finally, the piano itself has changed, so rules for avoiding
weak fingerings may be more relevant to the modern piano than to the
fortepiano, because the modern piano has a heavier action

> The purpose of the present model is not, then, to explain how fingerings
are determined in real time, but to explain why certain fingering patterns
predominate over others