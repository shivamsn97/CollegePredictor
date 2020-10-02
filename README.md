# College Predictor
Predict Colleges Using JOSAA Counselling Based On Your Rank Using Last Year's Data.

# Data Source
[Josaa Official Website](https://josaa.nic.in/webinfo/Page/Page?PageId=6&LangId=P)

# Installation and Running
Your System Must Have Python Installed (python 3),
Pip And Git Cli Are Installed And Added In Path.


#### Open Terminal on Linux / cmd on Windows

```sh
$ git clone https://github.com/shivamsn97/CollegePredictor
$ cd CollegePredictor
$ pip install -r requirements.txt     # pip3 in case of linux systems.
$ python .     # python3 in case of linux systems.
```

# Notes:
1. Back Button May Not Work On Windows As Expected
2. You Will Have To Enter Rank According To What You Are Expecting, Like If You Have Selected Obc In Caste, You Should Enter Obc Rank. Selecting Multiple Categories Are Not Recommended.
3. If You Have Changed The Source Pdfs, You Will Need To Run Convert-pdfs.py To Generate Json From Them. To Do So, First You Will Need To Install Java, Then A Python Module Named Tabula-py Using `pip Install Tabula-py`
4. The Schema Of Table Inside The Pdfs May Be Different For Different Pdfs. This Program Is Made As Per The Official Pdfs Provided By Josaa For Councelling Session 2019.
5. Please Star The Repo If It Helped  :sweat_smile:

## Contributing
Pull requests are welcome. For major changes, Please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
