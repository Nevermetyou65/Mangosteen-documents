This is part of Mangostten Dataset project

To use this repo

1. Install `uv`
2. Run `bash setup.sh`
3. Check if `documents` dir is there at root project
4. Put pdf documents in `documents/inputs`. Each source of pdf should be one folder like this

```
documents
|____inputs/
     |___<source_1>
     |___<source_2>
     ...
     |___<source_n>
```

5. Run `run_marker_loop.py` in terminal
6. Run code in `notebook/nb.ipynb`


We encourage users to implement pdf downloading pipeline and export to json pipeline yourself.
This repo only show experimenal code.

To learn more about marker, see https://github.com/datalab-to/marker