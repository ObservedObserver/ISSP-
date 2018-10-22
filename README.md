# ISSP-Web-Crawler
ISSP-Web-Craler is to collect data about internet security events about companines in China, analysis the influence on those compaines.
## Project Structure
```bash
.
├── LICENSE
├── README.md
├── analysis
│   └── filter.py
├── baidu
│   ├── __pycache__
│   │   ├── parse.cpython-36.pyc
│   │   ├── request.cpython-36.pyc
│   │   └── utils.cpython-36.pyc
│   ├── index.py
│   ├── parse.py
│   ├── request.py
│   └── utils.py
├── dataset (ignore)
│   ├── beijing_inc.csv
│   ├── bi_safe.json
│   ├── bj_safe_baidu.json
│   ├── bj_safe_baidu2017.json
│   └── bj_safe_baidu_0.json
└── toutiao
    ├── __pycache__
    │   ├── parse.cpython-36.pyc
    │   └── request.cpython-36.pyc
    ├── index.py
    ├── parse.py
    └── request.py
```
+ `baidu`
+ `toutiao`
+ `dataset(gitignore)`
+ `analysis`