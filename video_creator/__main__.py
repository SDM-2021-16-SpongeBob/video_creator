"""
Inlet of the program
"""

import argparse


def main():
    """Main function"""

    parser = argparse.ArgumentParser(
        description='Multiple videos in one and simple syncronization.')
    parser.add_argument('out_file', metavar='Output', type=str,
                        nargs=1, help='The result of the synthetic video')
    parser.add_argument('--input', nargs=2,
                        help='Entered video files')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
