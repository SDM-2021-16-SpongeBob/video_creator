# video_creator

[![ci_icon]][ci_link]

Use Python to multiple videos in one and simple syncronization.

## Requirements

- [numpy]>=1.21.4
- [opencv-python]>=4.5.4.58
- [pylint]>=2.11.1 (only for developers)

For details, please refer to [requirements.txt].

## Install

For Linux or MacOS:

```shell
make init
```

For Windows:

```shell
pip install -r requirements.txt
pip install -e .
```

## Usage

Use the following command:

```shell
video_creator [-h] [-i INPUT INPUT] OUTPUT
```

to multiple videos in one and simple syncronization.

### Positional arguments:

- `OUTPUT`: The result of the synthetic video

### Optional arguments:

  - `-h`, `--help`: Show this help message and exit
  - `-i`, `--input`: Entered video files

You can get more help message via `-h` or` --help` option:

```txt
$ video_creator --help
usage: video_creator [-h] [-i INPUT INPUT] OUTPUT

Multiple videos in one and simple syncronization.

positional arguments:
  OUTPUT                The result of the synthetic video

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT INPUT, --input INPUT INPUT
                        Entered video files
```

## Functional Specification

See [Functional Specification.md][functional_specification].


<!-- badge -->

[ci_icon]: https://github.com/SDM-2021-16-SpongeBob/video_creator/actions/workflows/build.yml/badge.svg
[ci_link]: https://github.com/SDM-2021-16-SpongeBob/video_creator/actions/workflows/build.yml

<!-- links -->
[requirements.txt]: https://github.com/SDM-2021-16-SpongeBob/video_creator/blob/main/requirements.txt
[numpy]: https://pypi.org/project/numpy
[opencv-python]: https://pypi.org/project/opencv-python
[pylint]: https://pypi.org/project/pylint
[functional_specification]: https://github.com/SDM-2021-16-SpongeBob/video_creator/blob/main/docs/Functional%20Specification.md
