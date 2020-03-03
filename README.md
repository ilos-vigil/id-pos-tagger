# ID PoS Tagger

Very simple PoS tagger trained with [Stanford Log-linear Part-Of-Speech Tagger
](https://nlp.stanford.edu/software/tagger.html) with [Indonesian Manually Tagged Corpus](https://github.com/famrashel/idn-tagged-corpus)

## Requirement

* Python 3.6
* NLTK
* StanfordNLP
* Java 8 (to train our model)

## How to create model

1. Generate props file

```
java -cp "stanford-postagger-basic/stanford-postagger.jar:lib/*" edu.stanford.nlp.tagger.maxent.MaxentTagger -genprops
```

2. Congigure props file

```ini
model = postagger-model-id.tagger
trainFile = format=TSV,idn-tagged-corpus/Indonesian_Manually_Tagged_Corpus.tsv
tagSeparator = _
arch = generic
openClassTags = NN MD RB VB JJ
# closedClassTags =
```

3. Generate model

```
java -cp "stanford-postagger-basic/stanford-postagger.jar:lib/*" -mx1g edu.stanford.nlp.tagger.maxent.MaxentTagger -props postagger-id.props
```

## Comparison

Comparison between our PoS tagger with [Stanford Indonesia PoS Tagger](https://stanfordnlp.github.io/stanfordnlp/models.html). Example sentences are taken from https://id.wikipedia.org/wiki/Bahasa_Indonesia and https://id.wikipedia.org/wiki/Kentang

* Bahasa Indonesia adalah bahasa Melayu yang dijadikan sebagai bahasa resmi Republik Indonesia dan bahasa persatuan bangsa Indonesia.

| Our PoS tagger       | Stanford ID PoS tagger |
| -------------------- | ---------------------- |
| ('Bahasa', 'NNP')    | ('Bahasa', 'NSD')      |
| ('Indonesia', 'NNP') | ('Indonesia', 'NSD')   |
| ('adalah', 'VB')     | ('adalah', 'O--')      |
| ('bahasa', 'NN')     | ('bahasa', 'NSD')      |
| ('Melayu', 'NN')     | ('Melayu', 'NSD')      |
| ('yang', 'SC')       | ('yang', 'S--')        |
| ('dijadikan', 'VB')  | ('dijadikan', 'VSP')   |
| ('sebagai', 'IN')    | ('sebagai', 'R--')     |
| ('bahasa', 'NN')     | ('bahasa', 'NSD')      |
| ('resmi', 'JJ')      | ('resmi', 'ASP')       |
| ('Republik', 'NNP')  | ('Republik', 'F--')    |
| ('Indonesia', 'NNP') | ('Indonesia', 'NSD')   |
| ('dan', 'CC')        | ('dan', 'H--')         |
| ('bahasa', 'NNP')    | ('bahasa', 'NSD')      |
| ('persatuan', 'NN')  | ('persatuan', 'NSD')   |
| ('bangsa', 'NN')     | ('bangsa', 'NSD')      |
| ('Indonesia', 'NNP') | ('Indonesia', 'NSD')   |
| ('.', 'Z')           | ('.', 'Z--')           |

* Bahasa Indonesia diresmikan penggunaannya setelah Proklamasi Kemerdekaan Indonesia, tepatnya sehari sesudahnya, bersamaan dengan mulai berlakunya konstitusi.

| Our PoS tagger          | Stanford PoS tagger          |
| ----------------------- | ---------------------------- |
| ('Bahasa', 'NNP')       | ('Bahasa', 'NSD')            |
| ('Indonesia', 'NNP')    | ('Indonesia', 'NSD')         |
| ('diresmikan', 'VB')    | ('diresmikan', 'VSP')        |
| ('penggunaannya', 'NN') | ('penggunaannya', 'NSD+PS3') |
| ('setelah', 'SC')       | ('setelah', 'R--')           |
| ('Proklamasi', 'NN')    | ('Proklamasi', 'X--')        |
| ('Kemerdekaan', 'NN')   | ('Kemerdekaan', 'NSD')       |
| ('Indonesia', 'NNP')    | ('Indonesia', 'NSD')         |
| (',', 'Z')              | (',', 'Z--')                 |
| ('tepatnya', 'NN')      | ('tepatnya', 'ASP+PS3')      |
| ('sehari', 'NN')        | ('sehari', 'ASP')            |
| ('sesudahnya', 'NN')    | ('sesudahnya', 'NSD+PS3')    |
| (',', 'Z')              | (',', 'Z--')                 |
| ('bersamaan', 'VB')     | ('bersamaan', 'VSA')         |
| ('dengan', 'IN')        | ('dengan', 'R--')            |
| ('mulai', 'VB')         | ('mulai', 'VSA')             |
| ('berlakunya', 'VB')    | ('berlakunya', 'VSA+PS3')    |
| ('konstitusi', 'NN')    | ('konstitusi', 'NSD')        |
| ('.', 'Z')              | ('.', 'Z--')                 |

* Di Timor Leste, bahasa Indonesia berstatus sebagai bahasa kerja.

| Our PoS tagger       | Stanford PoS tagger  |
| -------------------- | -------------------- |
| ('Di', 'IN')         | ('Di', 'R--')        |
| ('Timor', 'NNP')     | ('Timor', 'F--')     |
| ('Leste', 'NNP')     | ('Leste', 'F--')     |
| (',', 'Z')           | (',', 'Z--')         |
| ('bahasa', 'NNP')    | ('bahasa', 'NSD')    |
| ('Indonesia', 'NNP') | ('Indonesia', 'NSD') |
| ('berstatus', 'VB')  | ('berstatus', 'VSA') |
| ('sebagai', 'IN')    | ('sebagai', 'R--')   |
| ('bahasa', 'NN')     | ('bahasa', 'NSD')    |
| ('kerja', 'NN')      | ('kerja', 'NSD')     |
| ('.', 'Z')           | ('.', 'Z--')         |

* Kentang (Solanum tuberosum L.) adalah tanaman dari suku Solanaceae yang memiliki umbi batang yang dapat dimakan dan disebut "kentang" pula.

| Our PoS tagger       | Stanford PoS tagger   |
| -------------------- | --------------------- |
| ('Kentang', 'NN')    | ('Kentang', 'NSD')    |
| ('(', 'Z')           | ('(', 'Z--')          |
| ('Solanum', 'NN')    | ('Solanum', 'X--')    |
| ('tuberosum', 'NN')  | ('tuberosum', 'X--')  |
| ('L.', 'NNP')        | ('L', 'F--')          |
| ('.', 'Z--')         |
| (')', 'Z')           | (')', 'Z--')          |
| ('adalah', 'VB')     | ('adalah', 'O--')     |
| ('tanaman', 'NN')    | ('tanaman', 'NSD')    |
| ('dari', 'IN')       | ('dari', 'R--')       |
| ('suku', 'NN')       | ('suku', 'NSD')       |
| ('Solanaceae', 'NN') | ('Solanaceae', 'X--') |
| ('yang', 'SC')       | ('yang', 'S--')       |
| ('memiliki', 'VB')   | ('memiliki', 'VSA')   |
| ('umbi', 'NN')       | ('umbi', 'X--')       |
| ('batang', 'NN')     | ('batang', 'NSD')     |
| ('yang', 'SC')       | ('yang', 'S--')       |
| ('dapat', 'MD')      | ('dapat', 'VSA')      |
| ('dimakan', 'VB')    | ('dimakan', 'VSP')    |
| ('dan', 'CC')        | ('dan', 'H--')        |
| ('disebut', 'VB')    | ('disebut', 'VSP')    |
| ('``', 'NN')         | ('"', 'Z--')          |
| ('kentang', 'NN')    | ('kentang', 'NSD')    |
| ("''", 'VB')         | ('"', 'Z--')          |
| ('pula', 'RB')       | ('pula', 'D--')       |
| ('.', 'Z')           | ('.', 'Z--')          |

* Umbi kentang sekarang telah menjadi salah satu makanan pokok penting di Eropa walaupun pada awalnya didatangkan dari Amerika Selatan.

| Our PoS tagger              | Stanford PoS tagger          |
| --------------------------- | ---------------------------- |
| ('Penjelajah', 'NN')        | ('Penjelajah', 'NSD')        |
| ('Spanyol', 'NNP')          | ('Spanyol', 'NSD')           |
| ('dan', 'CC')               | ('dan', 'H--')               |
| ('Portugis', 'NNP')         | ('Portugis', 'X--')          |
| ('pertama', 'OD')           | ('pertama', 'CO-')           |
| ('kali', 'NND')             | ('kali', 'NSD')              |
| ('membawa', 'VB')           | ('membawa', 'VSA')           |
| ('ke', 'IN')                | ('ke', 'R--')                |
| ('Eropa', 'NNP')            | ('Eropa', 'NSD')             |
| ('dan', 'CC')               | ('dan', 'H--')               |
| ('mengembangbiakkan', 'NN') | ('mengembangbiakkan', 'VSA') |
| ('tanaman', 'NN')           | ('tanaman', 'NSD')           |
| ('ini', 'PR')               | ('ini', 'B--')               |
| ('.', 'Z'                   | ('.', 'Z--')                 |
