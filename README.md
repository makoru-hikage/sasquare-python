# SASQUARE
## Single Array Square Grid

A representation of a square matrix in with a single array. A Python implementation of https://github.com/makoru-hikage/sasquare-docs

Original implementation here: https://github.com/makoru-hikage/single-array-square
### Features
- Displays a text-based perfect square
- Highlights a chosen row or column of a perfect square
- Highlights all four corners of a square
- Highlights the center of a square
- Shows a cell's counterpart on the other side of a square

## Usage
Can be run in CMD or bash (and any unix terminal). Requires Python 3.
```bash
### Assure that sasquare.py has a +x permission
chmod +x sasquare.py
./sasquare.py
## OR
python sasquare.py
```

## Testing
Requires `unittest`. Just `cd` into the root of project directory and run this.
```bash
python -m unittest -v tests.celltests.TestCellFunctions
```

## License
[MIT](https://choosealicense.com/licenses/mit/)