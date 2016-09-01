# Pandio
Access python pandas in an "awk-like" manner in the command line -- inspired by [Rio](https://github.com/jeroenjanssens/data-science-at-the-command-line/blob/master/tools/Rio)

Install using setuptools:
```
cd pandio
python setup.py install
```
Usage as follows:
STDIN (or a file) is piped to an object called `df`. Numpy is accessed as `np`. Resulting operations in the `df` are piped to STDOUT.
```
'pandio COMMAND [--file FILE]'
```
Example:
```
'cut -f 1-10 data_frame.txt | pandio "np.log(df)"'
```

Note this is super simplistic, and naively uses python's `exec`, so it's sort of insecure at the moment.
