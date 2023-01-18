### Installation

Prerequisites:

- Python 3
- Pip

Set up:

1. Install [ venv ](https://docs.python.org/3/library/venv.html):

   `pip install --user venv`

2. Create virtual environment:

   `python -m venv venv`

3. Activate virtual environment venv:

    * Windows: `.venv\Scripts\activate.bat` or `.\venv\Scripts\Activate.ps1`

    * MacOS/Linux: `source venv/bin/activate`

4. Install required packages:

   `pip install -r requirements.txt`

You're good to go!

### Development

Remember to activate virtual environment before developing/running code.

### Tests

Using pytest as test framework. Run `pytest` in root folder to verify tests.
