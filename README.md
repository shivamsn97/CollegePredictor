# CollegePredictor
Predict colleges for Josaa councelling based on your rank using last year's data.

# Data Source
[Josaa official website](https://josaa.nic.in/webinfo/Page/Page?PageId=6&LangId=P)

# Installation and Running
First make sure python (version >= 3.6), pip and git cli are installed and added in path.

Then:

```shell
git clone https://github.com/shivamsn97/CollegePredictor
cd CollegePredictor
pip install -r requirements.txt     # may be pip3 in case of linux systems.
python .     # may be python3 in case of linux systems.
```

# Notes:
1. Back button may not work on windows as expected
2. You will have to enter rank according to what you are expecting, like if you have selected OBC in caste, you should enter obc rank. Selecting multiple categories are not recommended.
3. If you have changed the source pdfs, you will need to run convert-pdfs.py to generate json from them. To do so, first you will need to install java, then a python module named tabula-py using `pip install tabula-py`
4. The schema of table inside the pdfs may be different for different pdfs. This program is made as per the official pdfs provided by jossa for councelling session 2019.
5. Please star the repo if it helped  :sweat_smile:

