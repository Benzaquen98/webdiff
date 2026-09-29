# WebDiff

WebDiff is a command-line tool for comparing public web assets between websites using cryptographic fingerprints and similarity analysis.

It discovers publicly referenced JavaScript and CSS assets, calculates their SHA-256 hashes, and identifies identical assets observed across different websites.

## Features

- Extracts publicly referenced JavaScript and CSS assets.
- Resolves relative asset paths into absolute URLs.
- Calculates SHA-256 fingerprints for discovered assets.
- Detects identical assets across two websites.
- Calculates JavaScript, CSS, and overall similarity scores.
- Provides a simple command-line interface.

## Installation

Clone the repository:

```bash
git clone https://github.com/Benzaquen98/webdiff.git
cd webdiff
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install WebDiff:

```bash
pip install -e .
```
## Usage

Compare two websites by providing their URLs:

```bash
webdiff https://example.com https://example.org
```

Example output:

```text
WebDiff
=======

Site A: https://example.com/
Site B: https://example.org/

Assets discovered
-----------------
JavaScript A: 1
JavaScript B: 1
CSS A: 0
CSS B: 0

Similarity
----------
JavaScript: 100.0%
CSS: N/A
Overall: 100.0%

Matching assets
---------------
[JavaScript]
  Site A: https://example.com/s.js
  Site B: https://example.org/s.js
  SHA-256: ef81a2433631cf01e00954a93b7b1861e56ae475be74102aef4e3e2b2e92faf3
```
