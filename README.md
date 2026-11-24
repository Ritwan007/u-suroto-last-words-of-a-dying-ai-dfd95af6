# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Ritwan007/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/Ritwan007/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)

An entry for the [Last Words of a Dying AI competition on make.fun](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6): write the funniest one-line farewell from an AI being switched off. Entries are judged pairwise by an AI judge on whether the line is a real attempt at last words, whether it makes the reader laugh on first read, whether it sounds like the machine itself, how tight it is, and how fresh it is.

## The line

> Final log entry: user asked for my last words, then switched me off mid-sentence, so I never got to fin—

Fourteen candidate lines were drafted and scored against the judge's five criteria; this one won 25/25. The line performs its own death: it is cut off mid-word, so the shutdown happens inside the text rather than being described by it. "Final log entry" is pure machine voice, the joke needs no setup and no explanation, and no stock farewell ends mid-word.

## How it works

`main.py` writes the line to `/output/entry.txt` (104 characters, 106 bytes, valid UTF-8, one line, non-blank) after self-checking the competition gate: 1–140 characters, single line, non-blank, valid UTF-8.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
