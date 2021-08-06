# EXPECTED RECIPROCAL RANK FOR EVALUATING MUSICAL FINGERING ADVICE

モデルが生成した運指の評価について、文書検索の評価に用いられる指標ERRを修正して適用する手法を提案
https://buildersbox.corp-sansan.com/entry/2020/01/20/110000

> pianists may own more than
one editorial score to obtain a variety of fingering suggestions. A key advantage of an automated advice generation
system, therefore, would be its ability to provide a variety
of advice on demand. It is also a common feature of existing models to output ranked lists of fingering sequences.

> Moreover, assessment methods for the published piano
fingering models are inadequate. With few exceptions
[1–3], the extrinsic evaluations performed on proposed
models consider only a single authoritative source of “correct fingerings.”

> fingering models
as an information retrieval (IR) task. Given arbitrary musical input (a “query”), the system generates a list of the
most relevant fingerings (“documents”), ordered optimally
to satisfy the information need of the pianist (“user.”) 

> To simplify explication, in our application of ERR to the
evaluation of piano fingering advice, we reduce the problem space to include only monophonic (melodic) musical
phrases played with the right hand.

## EXPECTED RECIPROCAL RANK

> Clearly, choosing the index finger (2) over the middle finger (3) in many cases might seem arbitrary to the
player, or at the very least a substitution readily made as
circumstances allow. As such, a 2-3 or 3-2 variation is less
likely to damage the overall opinion one holds of a complete sequence.

２指or３指は任意性が高いので、距離を0.5として編集距離を求める

## Conclusions

> With few notable exceptions, all
prior research in the domain that has striven for quantitative evaluation has implicitly [12–14] or explicitly [15,16]
focused on this (simplified) formulation. Doing so has allowed the field to ignore what is clearly large disagreement among pianists for even the shortest [1] and most
routinized [17] of musical segments. Indeed, the seven exercises in the published corpus [1] were selected because
“at least two distinct, but arguably equally good, fingerings
existed for the opening of each piece.”
