# Montgomery College Python coursework

An archive of my CMSC 135 — Introduction to Scripting work from Montgomery College, Fall 2022, with related scripting exercises recovered from my Obsidian vault.

The original Python files are preserved byte for byte. This collection records my learning history; it includes completed assignments, class exercises, supplied examples, and unfinished drafts.

## Contents

| Folder | Contents |
| --- | --- |
| `assignments/` | 9 programs with explicit author headers: cookie calculations, magic-date checking, rainfall totals, ticket revenue, file averages and exception handling, list statistics, and date formatting |
| `classwork/` | 7 personally named class exercises, including hashing, IPv4 validation, file I/O, lists, functions, and a cipher draft |
| `reference-examples/` | 61 course attachments without established personal authorship; these are not presented as original projects |
| `drafts/` | 3 incomplete or empty files, retained as historical work |
| `recovered-from-screenshots/` | A Python greeting transcribed from my September 19, 2022 coursework screenshot |
| `related-scripting/` | PowerShell variable exercises and a Bash script transcribed from submitted screenshots |

## Run an assignment

Python 3 and the standard library are sufficient for the standalone assignments. Programs are interactive. For example:

```text
python assignments/04-ticket-sales/main.py
```

For the file-average assignments, change into the assignment directory first so the program can find its bundled `numbers.txt`:

```text
cd assignments/05-file-average
python main.py
```

The reference UDP example opens a network socket and is not part of the run checks. Screenshot transcriptions are labeled separately from recovered originals.

## Dates and provenance

`provenance.json` records the original attachment names, SHA-256 hashes, author evidence, header due dates, ZIP entry timestamps, syntax status, and duplicate source locations. Five duplicate Python entries were consolidated, leaving 80 distinct original Python files. One additional Python file and two shell exercises were transcribed from screenshots.

The Obsidian course journal establishes Fall 2022. Due dates are not creation dates, and ZIP timestamps are not necessarily creation dates. Some assignment headers say January 2022 even though the course journal and a November 2022 ZIP record place the work in the fall semester. Those conflicts are preserved explicitly. Exact source-file creation dates are unknown where the evidence does not establish them.

This archive was imported to GitHub on November 26, 2026. New commits use the actual import date.

## Validation

All original Python files received syntax checks. Two unfinished drafts have syntax errors; one file is empty. Selected authored assignments were also checked with controlled sample inputs. Known learning-stage limitations remain: the magic-date program checks a specific date, the cipher returns after one character, and the IPv4/date examples have incomplete validation. The originals have not been rewritten to hide those limitations.

## Attribution

The named assignment headers identify Onjatiana Razafimanjaka and CMSC 135. Classwork and reference files may adapt course or textbook examples, including material associated with *Starting Out with Python*, 4th edition. Their inclusion does not claim original authorship. Instructor slides, assignment PDFs, account information, and complete private reports are not included.
