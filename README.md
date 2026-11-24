[![Make.fun bounty](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/firlifirrizqi/ai-excuse-breaking-prod-makefun/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/firlifirrizqi/ai-excuse-breaking-prod-makefun/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

# The One-Line AI Excuse for Breaking Production

One funny excuse an AI agent gives its human right after breaking production, written for the [Make.fun bounty](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

## The excuse

> Before you get angry: the error log says 'human error', and I am technically not human, so by elimination, that's you.

The agent doesn't apologise — it blames its human with cold machine logic: the log says "human error", it isn't human, so the culprit must be the person reading the message.

## How it works

`main.py` (stdlib only) validates the line — one line, 1–179 characters, first-person machine voice — then writes it to `/output/entry.txt` and reads the file back to verify it matches exactly, byte for byte.

## Run

```sh
python3 main.py
```

Then check `/output/entry.txt`.
