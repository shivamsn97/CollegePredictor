# College Predictor
Predict Colleges Using JOSAA Counselling Based On Your Rank Using Last Year's Data.

# Data Source
[Josaa Official Website](https://josaa.nic.in/webinfo/Page/Page?PageId=6&LangId=P)

# Installation and Running
Your System must have python installed (python 3),
pip and git cli are installed and added in path.


#### Open Terminal on Linux / cmd on Windows

```sh
$ git clone https://github.com/shivamsn97/CollegePredictor
$ cd CollegePredictor
$ pip install -r requirements.txt     # pip3 in case of linux systems.
$ python .     # python3 in case of linux systems.
```

# Notes:
1. Back button may not work on windows as expected
2. You will have to enter rank according to what you are expecting, like if you have selected OBC in caste, you should enter obc rank. Selecting multiple categories are not recommended.
3. If you have changed the source pdfs, you will need to run convert-pdfs.py to generate json from them. To do so, first you will need to install java, then a python module named tabula-py using `pip install tabula-py`
4. The schema of table inside the pdfs may be different for different pdfs. This program is made as per the official pdfs provided by josaa for councelling session 2019.
5. Please star the repo if it helped 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
