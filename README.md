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
python3 generate_xling.py eng fin data/release/v2023-09-26/eng-fin/train.{src,trg}.gz | head -n 1
```

Expected output:

```
{"text": "<|im_start|>user\nKäännä englanniksi: - Et auta, Grace.<|im_end|>\n<|im_start|>assistant\nYou're not helping, grace.<|im_end|>\n"}
```
