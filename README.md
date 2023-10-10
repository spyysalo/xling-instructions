# xling-instructions

Generate instruction-formatted data from translation pairs

## Quickstart

Download a Tatoeba dataset

```
wget https://object.pouta.csc.fi/Tatoeba-Challenge-v2023-09-26/eng-fin.tar
```

Unpack

```
tar xf eng-fin.tar
```

Generate

```
python3 generate_xling.py eng fin data/release/v2023-09-26/eng-fin/train.{src,trg}.gz | head -n 4
```

Expected output:

```
python3 generate_xling.py eng fin data/release/v2023-09-26/eng-fin/train.{src,trg}.gz | head -n 4
<|im_start|>user
Translate into Finnish: You're not helping, grace.<|im_end|>
<|im_start|>assistant
- Et auta, Grace.<|im_end|>
```
