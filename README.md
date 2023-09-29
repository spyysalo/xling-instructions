# xling-instructions

Generate instruction-formatted data from translation pairs

## Quickstart

Download a Tatoeba dataset

```
wget https://object.pouta.csc.fi/Tatoeba-Challenge-v2021-08-07/eng-fin.tar
```

Unpack

```
tar xf eng-fin.tar
```

Generate

```
python3 generate_xling.py eng fin data/release/v2021-08-07/eng-fin/train.{src,trg}.gz | head -n 2
```

Expected output:

```
<|user|>Translate into Finnish: Facebook is not dead or dying.
<|assistant|>Facebook ei ole kuollut eikä kuolemassa.
```
