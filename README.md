# [pyhf Poster for IRIS-HEP 2020 Poster Session](https://indico.cern.ch/event/894127/)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3697213.svg)](https://doi.org/10.5281/zenodo.3697213)

## Notes
- Posters need to be sized 30" x 40" and file format in PDF.
- The audience are typically not high-energy physicists &mdash; so avoid lingo. Simple and clear posters are definitely preferred.

## Build

To build the poster first create a Python virtual environment and activate it and then install the `requirements` and then build the poster with `make`

```shell
$ python3 -m venv poster-session
$ source poster-session/bin/activate
(poster-session) $ python -m pip install -r requirements.txt
(poster-session) $ make
```
