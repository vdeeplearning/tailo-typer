# TaiLoTyper

**Type Taiwanese Hokkien in Tâi-lô on a standard English keyboard.**

TaiLoTyper is a Windows-friendly tool that lets you type **Taiwanese Hokkien (Tâi-lô / Tai-lo)** using **tone numbers**, then convert it into proper **tone-marked Tai-lo**.

Instead of manually typing characters like:

- **á**
- **ê**
- **ū**
- **a̍**

you can type normal letters plus a number at the end of each syllable.

For example:

```text
Gua2 e5 tshu3-ting2 u7 niau1-a2.
```

becomes:

```text
Guá ê tshù-tíng ū niau-á.
```

---

# Why this exists

Windows can display Unicode Tai-lo, but it does **not include a built-in, ergonomic input method** for typing Tai-lo on a standard English keyboard.

TaiLoTyper provides a simpler workflow:

- Type normal letters
- Add tone numbers at the end of syllables
- Press a hotkey
- Get proper tone-marked Tai-lo

This project is designed for:

- Tai-lo learners
- Taiwanese Hokkien learners
- Teachers
- people making study materials
- anyone who wants a practical Tai-lo typing workflow on Windows

---

# The easiest way to use it (Windows)

## What it does

TaiLoTyper includes a **Windows hotkey tool**.

### Workflow

1. Type tone-number Tai-lo anywhere (Notepad, browser, docs, etc.)
2. Select the text
3. Press **Ctrl + Alt + T**
4. TaiLoTyper replaces the selected text with tone-marked Tai-lo

### Example

You type:

```text
Gua2 e5 tshu3-ting2 u7 niau1-a2.
```

After pressing **Ctrl + Alt + T**, it becomes:

```text
Guá ê tshù-tíng ū niau-á.
```

---

# Quick setup for non-programmers (Windows)

If you just want to **use** TaiLoTyper and do not care about Python details, follow these steps.

## Step 1: Download this project

Either:

- clone it with Git, **or**
- click **Code → Download ZIP** on GitHub, then unzip it somewhere easy to find

For example:

```text
C:\Users\YourName\tailo-typer
```

---

## Step 2: Install Python

Download Python from:

- https://www.python.org/downloads/

During installation:

- **IMPORTANT:** check the box that says:

```text
Add Python to PATH
```

Then finish the install.

To verify Python works, open **PowerShell** and run:

```powershell
python --version
```

You should see something like:

```text
Python 3.x.x
```

---

## Step 3: Install AutoHotkey v2

Download AutoHotkey v2 from:

- https://www.autohotkey.com/

**Important:** install **AutoHotkey v2**, not v1.

---

## Step 4: Update the script paths (one-time setup)

Open this file:

```text
src\windows\TaiLoTyper.ahk
```

Find these two lines:

```ahk
pythonExe := "C:\Users\tommy\tailo-typer\.venv\Scripts\python.exe"
scriptPath := "C:\Users\tommy\tailo-typer\src\tailo_converter.py"
```

Replace them with paths that match **your computer**.

### Example (if you are not using a virtual environment)

```ahk
pythonExe := "python"
scriptPath := "C:\Users\YourName\tailo-typer\src\tailo_converter.py"
```

### Example (if you *are* using the included virtual environment)

```ahk
pythonExe := "C:\Users\YourName\tailo-typer\.venv\Scripts\python.exe"
scriptPath := "C:\Users\YourName\tailo-typer\src\tailo_converter.py"
```

> **Tip:** If you are a normal user and just want it to work, using `pythonExe := "python"` is usually easiest *if Python is installed and on PATH*.

Save the file.

---

## Step 5: Run the hotkey script

Double-click:

```text
src\windows\TaiLoTyper.ahk
```

If AutoHotkey is installed correctly, the script will start running in the background.

You should see a green AutoHotkey icon in the Windows system tray.

---

## Step 6: Try it

Open **Notepad** and type:

```text
Gua2 e5 tshu3-ting2 u7 niau1-a2.
```

Select the text.

Press:

```text
Ctrl + Alt + T
```

It should change to:

```text
Guá ê tshù-tíng ū niau-á.
```

---

# How to type Tai-lo with tone numbers

The basic rule is simple:

- Type the syllable
- Put the **tone number at the end of the syllable**

### Examples

| You type | TaiLoTyper converts it to |
|---|---|
| `gua2` | `guá` |
| `e5` | `ê` |
| `tshu3` | `tshù` |
| `u7` | `ū` |
| `tsit8` | `tsi̍t` |
| `niau1-a2` | `niau-á` |

---

# Supported tone numbers (current MVP)

| Tone | Current behavior | Example input | Example output |
|---|---|---|---|
| 1 | no visible mark | `niau1` | `niau` |
| 2 | acute accent | `gua2` | `guá` |
| 3 | grave accent | `tshu3` | `tshù` |
| 4 | currently treated as no visible mark in MVP | `sik4` | `sik` |
| 5 | circumflex | `e5` | `ê` |
| 7 | macron | `u7` | `ū` |
| 8 | vertical mark / combining mark | `tsit8` | `tsi̍t` |

> **Note:** This is an early MVP. Tone 4 / checked-tone handling will improve in future versions.

---

# Example conversions

| Input | Output |
|---|---|
| `gua2` | `guá` |
| `e5` | `ê` |
| `tshu3` | `tshù` |
| `u7` | `ū` |
| `tsit8` | `tsi̍t` |
| `tshu3-ting2` | `tshù-tíng` |
| `niau1-a2` | `niau-á` |
| `tai5-uan5` | `tâi-uân` |

---

# If the hotkey does not work

## Make sure AutoHotkey is running

You should see a green AutoHotkey icon in the system tray.

If not:

- double-click `src\windows\TaiLoTyper.ahk` again

---

## If you edited the `.ahk` file

AutoHotkey does **not** automatically reload after edits.

If you changed the script:

1. Right-click the green AutoHotkey icon
2. Click **Exit**
3. Double-click `src\windows\TaiLoTyper.ahk` again

---

## If nothing happens when you press Ctrl + Alt + T

Check:

- Is text selected?
- Is AutoHotkey running?
- Did you set the correct `pythonExe` path?
- Did you set the correct `scriptPath` path?
- Does `python --version` work in PowerShell?

---

# Command-line usage (optional)

If you prefer, you can also use TaiLoTyper directly from the command line.

## Convert one phrase

```powershell
python src\tailo_converter.py "Gua2 e5 tshu3-ting2 u7 niau1-a2."
```

Output:

```text
Guá ê tshù-tíng ū niau-á.
```

---

## Interactive mode

Run with no arguments:

```powershell
python src\tailo_converter.py
```

Then type lines one at a time.

---

# For developers

This repo also includes a Python converter core and tests.

## Project structure

```text
tailo-typer/
├── README.md
├── docs/
│   └── user-guide.md
├── src/
│   ├── __init__.py
│   ├── tailo_converter.py
│   └── windows/
│       └── TaiLoTyper.ahk
├── tests/
│   └── test_tailo_converter.py
└── examples/
    └── examples.txt
```

---

## Local development setup (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pytest
```

Run tests:

```powershell
pytest
```

---

# Current status

## Working now

- Python Tai-lo tone-number converter
- Interactive CLI mode
- File-based conversion mode
- Windows AutoHotkey MVP
- Hotkey conversion using **Ctrl + Alt + T**
- Basic test suite

## Still planned

- Better tone-mark placement heuristics
- Improved checked-tone handling
- Better packaging for non-technical users
- A cleaner one-click Windows release
- Demo GIF / video
- Possibly a standalone `.exe`

---

# Known limitations

This is an early prototype.

Current limitations include:

- Tone-mark placement uses simplified heuristics
- Not all Tai-lo orthographic edge cases are handled yet
- No dictionary validation yet
- Tone 4 / checked-tone behavior is still simplified
- The Windows MVP currently requires local Python + AutoHotkey
- Paths in the `.ahk` script must currently be configured manually

---

# Why this is an interesting project

TaiLoTyper is small, but it touches several real engineering problems:

- Unicode and combining diacritics
- orthography-aware text transformation
- input ergonomics
- Windows automation
- UTF-8 encoding pitfalls
- user-focused tooling for under-served language workflows

---

# Contributing

Suggestions, bug reports, and example conversions are very welcome—especially from:

- Taiwanese speakers
- Tai-lo users
- Taiwanese Hokkien learners
- teachers creating romanized materials

If you find an incorrect conversion, please open an issue with:

- the input you typed
- the output you expected
- the output TaiLoTyper produced

---

# License

TBD