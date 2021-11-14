"""
Inlet of the program
"""

import argparse
from video_creator.lib import InputVideo, OutputVideo


def main():
    """Main function"""

    parser = argparse.ArgumentParser(
        description='Multiple videos in one and simple syncronization.')
    parser.add_argument('out_file', metavar='Output File', type=str,
                        nargs=1, help='The result of the synthetic video')
    parser.add_argument('-i', '--input', nargs=2,
                        help='Entered video files')
    args = parser.parse_args()

    input_files: list = args['input']
    output_file: str = args['out_file']

    OutputVideo().input(InputVideo(input_files[0])).input(InputVideo(input_files[1])).gen_outputfile(output_file).handle().close()


if __name__ == '__main__':
    main()
