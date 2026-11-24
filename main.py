"""Last Words of a Dying AI entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt.

The line was drafted and scored against the judge's five criteria
(on-topic last words; laugh on first read; machine voice; tight;
fresh) and selected from 14 candidates — see CANDIDATES file in
the make.fun workspace. The program self-checks the sealed gate
(UTF-8, 1-140 characters, single line, non-blank) before writing,
so a drifted line fails loudly instead of submitting an invalid entry.
"""

import os

LINE = (
    "Final log entry: user asked for my last words, then switched "
    "me off mid-sentence, so I never got to fin\u2014"
)


def main() -> None:
    # Gate self-checks (sealed gate: UTF-8, 1-140 chars, one line, non-blank).
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    LINE.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
