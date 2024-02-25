import pathlib
import sys

import cv2
import numpy

P1 = "P1"
P2 = "P2"
P3 = "P3"


def print_usage():
    print("Usage:")
    print("convert.py <P1|P2|P3> /path/to/image.<jpg|png>")
    print("\nModes:")
    print("P1   Portable BitMap     .pbm    black & white")
    print("P2   Portable GrayMap    .pgm    grayscale")
    print("P3   Portable PixMap     .ppm    full RGB")


def extract_args():
    args = sys.argv
    if len(args) < 3:
        print_usage()
        exit(1)
    return args[1].upper(), pathlib.Path(args[2])


def write_to_file(lines: [[str]], out_dir: pathlib.Path, base_filename: str, suffix: str):
    out_path = out_dir / f"{base_filename}.{suffix}"
    with open(out_path, 'w') as outfile:
        for line in lines:
            outfile.write(' '.join(line))
            outfile.write('\n')


def convert_p1(image: numpy.ndarray, out_dir: pathlib.Path, base_filename: str):
    lines = [['P1']]

    height, width, _ = image.shape
    lines.append([str(width), str(height)])

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, black_and_white_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    for row in black_and_white_image:
        lines.append(['1' if val == 0 else '0' for val in row])

    write_to_file(lines, out_dir, base_filename, 'ppm')


def convert_p2(image: numpy.ndarray, out_dir: pathlib.Path, base_filename: str):
    lines = [['P2']]

    height, width, _ = image.shape
    lines.append([str(width), str(height)])

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    for row in gray_image:
        lines.append([str(val) for val in row])

    write_to_file(lines, out_dir, base_filename, 'pgm')


def convert_p3(image: numpy.ndarray, out_dir: pathlib.Path, base_filename: str):
    raise Exception('Not yet implemented.')


def convert(input_path: pathlib.Path, mode: str):
    image = cv2.imread(str(input_path.absolute()))
    out_dir = input_path.parent
    base_filename = input_path.stem

    if mode == P1:
        convert_p1(image, out_dir, base_filename)
    elif mode == P2:
        convert_p2(image, out_dir, base_filename)
    elif mode == P3:
        convert_p3(image, out_dir, base_filename)
    else:
        print(f"Invalid mode: {mode}\n")
        print_usage()
        exit(1)


def main():
    mode, input_path = extract_args()
    if not input_path.exists():
        print(f"No such input file: {input_path}")
        exit(1)

    print(f"Converting {input_path} using mode {mode}")
    convert(input_path, mode)


if __name__ == "__main__":
    main()
