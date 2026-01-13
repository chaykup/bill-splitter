# Dinner Bill Splitter
This app separates a group's meal bill into itemized subtotals with appropriate tax and tip percentages calculated.

# Features
- User can choose which items to add to each individual's total
- Tax and tip calculated automatically based on percentages input by user
- Venmo request individuals in group directly from app
- Share itemized sub-receipts through text or email

# Requirements
- PaddleOCR==3.3.2
- PaddlePaddle==3.0.0
- Numpy<2.0.0

# Getting Started

## MacOS / Linux
```bash
git clone <https://github.com/yourusername/bill-splitter.git>
cd bill-splitter

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Windows
```bash
git clone <https://github.com/yourusername/bill-splitter.git>
cd bill-splitter

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
```
