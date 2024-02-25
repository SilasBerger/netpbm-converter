# NetPBM Converter
A command-line utility for converting images to Netpbm.

## Usage
### Initial setup
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Converting an image
Command format: `convert.py <magic_number> <input_path>`

Usage examples:
```sh
convert.py P1 /User/johndoe/Pictures/cat.png # creates /User/johndoe/Pictures/cat.pbm (black & white)
convert.py P2 /User/johndoe/Pictures/dog.jpg # creates /User/johndoe/Pictures/dog.pgm
convert.py P3 /User/johndoe/Pictures/capibara.jpeg # creates /User/johndoe/Pictures/capibara.ppm
```


## Supported Netpbm formats
| Type             | Magic number | Extension | Colors                |
|------------------|--------------|-----------|-----------------------|
| Portable BitMap  | `P1` (ASCII) | `.pbm`     | 0-1 (black & white)   |
| Portable GrayMap | `P2` (ASCII) | `.pgm`     | 0-255 (grayscale)     |
| Portable PixMap  | `P3` (ASCII) | `.ppm`     | 0-255 per RGB channel |

## Useful links
- [Netpbm (Wikipedia)](https://en.wikipedia.org/wiki/Netpbm)
