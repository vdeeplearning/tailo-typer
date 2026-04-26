\# TaiLoTyper



Type \*\*Taiwanese Hokkien in Tâi-lô\*\* on a standard English keyboard using \*\*tone-number input\*\*.



TaiLoTyper converts text like:



```text

Gua2 e5 tshu3-ting2 u7 tsit8 tsiah niau1-a2.

```



into:



```text

Guá ê tshù-tíng ū tsi̍t tsiah niau-á.

```



\## Why this exists



Windows can display Unicode Tai-lo, but it does \*\*not include a built-in, ergonomic input method\*\* for typing Tai-lo on a standard English keyboard.



TaiLoTyper provides a simpler workflow:



\- Type normal letters

\- Add tone numbers at the end of each syllable

\- Convert to proper tone-marked Tai-lo



This is intended as a lightweight, beginner-friendly way to write Taiwanese Hokkien without memorizing special keyboard layouts.



\## Features (MVP)



\- Convert tone-number input to tone-marked Tai-lo

\- Preserve hyphenated syllables

\- Handle common tones:

&#x20; - 1 (no mark)

&#x20; - 2 (acute)

&#x20; - 3 (grave)

&#x20; - 5 (circumflex)

&#x20; - 7 (macron)

&#x20; - 8 (vertical mark / combining mark)

\- Simple Python converter

\- Test suite with `pytest`



\## Example conversions



| Input | Output |

|---|---|

| `gua2` | `guá` |

| `e5` | `ê` |

| `tshu3` | `tshù` |

| `u7` | `ū` |

| `tsit8` | `tsi̍t` |

| `tshu3-ting2` | `tshù-tíng` |

| `niau1-a2` | `niau-á` |



\## Current status



This repo currently contains:



\- A \*\*Python MVP converter\*\*

\- Unit tests for basic tone conversion

\- Initial project structure for a future \*\*Windows typing helper\*\*



Planned next step:



\- A \*\*Windows AutoHotkey tool\*\* that converts selected text with a hotkey (for example, `Ctrl+Alt+T`)



\## Quick start



\### 1. Clone the repo



```bash

git clone https://github.com/YOURUSERNAME/tailo-typer.git

cd tailo-typer

```



\### 2. Create a virtual environment



\*\*Windows PowerShell:\*\*



```powershell

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install -U pip

pip install pytest

```



\### 3. Run the converter



```powershell

python src\\tailo\_converter.py "Gua2 e5 tshu3-ting2 u7 tsit8 tsiah niau1-a2."

```



Expected output:



```text

Guá ê tshù-tíng ū tsi̍t tsiah niau-á.

```



\### 4. Run tests



```powershell

pytest

```



\## Project structure



```text

tailo-typer/

├── README.md

├── docs/

│   └── user-guide.md

├── src/

│   ├── \_\_init\_\_.py

│   └── tailo\_converter.py

├── tests/

│   └── test\_tailo\_converter.py

└── examples/

&#x20;   └── examples.txt

```



\## Design goals



\- \*\*Ergonomic:\*\* easy to type on a normal English keyboard

\- \*\*Simple:\*\* no custom keyboard layout required

\- \*\*Portable:\*\* future Windows utility should be easy to distribute

\- \*\*Transparent:\*\* rules should be understandable and documented

\- \*\*Extensible:\*\* converter logic should be testable and improvable



\## Known limitations (current MVP)



This is an early prototype.



Current limitations include:



\- Tone-mark placement uses simplified heuristics

\- Not all Tai-lo orthographic edge cases are handled yet

\- No dictionary validation yet

\- No live Windows hotkey utility yet

\- Some vowel combinations may need improved placement rules



\## Roadmap



\- \[x] Python tone-number converter MVP

\- \[x] Basic test suite

\- \[ ] Improve vowel nucleus detection rules

\- \[ ] Add more test coverage

\- \[ ] Create CLI polish / packaging

\- \[ ] Build AutoHotkey Windows hotkey converter

\- \[ ] Add demo GIF

\- \[ ] Add downloadable release



\## Why this is interesting



This project is small, but it touches several non-trivial problems:



\- Unicode and combining diacritics

\- Orthography-aware text transformation

\- Input ergonomics

\- Language-tool UX

\- Windows-first distribution



\## Contributing



Contributions, bug reports, and suggestions are welcome—especially from Taiwanese speakers, Tai-lo learners, and anyone familiar with Taiwanese orthography.



\## License



TBD

