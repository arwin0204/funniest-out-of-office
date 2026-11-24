# The Funniest Out-of-Office

Entry for the make.fun bounty "The Funniest Out-of-Office" — a single-line
out-of-office auto-reply, 140 characters or fewer.

## Entry

> I'm out of office until Monday — my inbox is unsupervised, has my passwords, and has already asked HR for my job.

(113 characters, one line, no link.)

## How to run

```sh
python3 main.py
```

This writes the entry text to `/output/entry.txt`. The program is
deterministic: every run writes exactly the same text. It uses only the
Python 3.13 standard library, makes no network requests, and has no
dependencies.

## License

MIT — see LICENSE.
