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
convert.py P1 ./example_data/images/cat.jpg # creates ./example_data/images/cat.pbm (black & white)
convert.py P2 ./example_data/images/dog.jpg # creates ./example_data/images/dog.pgm
convert.py P3 ./example_data/images/capibara.jpg # creates ./example_data/images/capibara.ppm
```

## Supported Netpbm formats
| Type             | Magic number | Extension | Colors                |
|------------------|--------------|-----------|-----------------------|
| Portable BitMap  | `P1` (ASCII) | `.pbm`    | 0-1 (black & white)   |
| Portable GrayMap | `P2` (ASCII) | `.pgm`    | 0-255 (grayscale)     |
| Portable PixMap  | `P3` (ASCII) | `.ppm`    | 0-255 per RGB channel |

## Useful links
- [Netpbm (Wikipedia)](https://en.wikipedia.org/wiki/Netpbm)

## Image sources
- `cat.jpg`: <a href="https://pixabay.com/de/users/jaclou-dl-5602247/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5098930">JackieLou DL</a> on <a href="https://pixabay.com/de//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5098930">Pixabay</a>
- `dog.jpg`: <a href="https://pixabay.com/de/users/picsbyfran-6087762/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2785074">Fran • @mallorcadogphotography</a> on <a href="https://pixabay.com/de//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2785074">Pixabay</a>
- `capibara.jpg`: <a href="https://pixabay.com/de/users/chacha8080-11915634/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5255073">Masakazu Kobayashi</a> on <a href="https://pixabay.com/de//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=5255073">Pixabay</a>
