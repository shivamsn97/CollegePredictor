import json
import inquirer
from inquirer import errors

data = {}
with open("data.json",'r') as jsfile:
    data = json.loads(jsfile.read())

def int_validator(answers, current):
    if not current.strip():
        raise errors.ValidationError('', reason='Please provide a rank!')
    try:
        int(current)
        return True
    except ValueError:
        raise errors.ValidationError('', reason='Provided value is not an integer!')

questions = [
    inquirer.Text('college',
                  message='Keywords to find in college name (Leave blank for all)?',
                  default=''),
    inquirer.Checkbox('quota',
                  message='Quota? (Use space to deselect, X = selected, O = not selected)',
                  choices=data["values"]["quota"],
                  default=["AI", "OS"]),
    inquirer.Checkbox('category',
                      message='Category?',
                      choices=data["values"]["category"],
                      default=[x for x in data["values"]["category"] if ("gen" in x.lower() or "obc" in x.lower()) and "pwd" not in x.lower()]
                      ),
    inquirer.Checkbox('seat_pool',
                      message='Seat Pool?',
                      choices=data["values"]["seat_pool"],
                      default=["Gender-Neutral"]
                      ),
    inquirer.Text('streams',
                      message='Keywords to find in stream (Leave blank for all)?',
                      default=""
                      ),
    inquirer.Text(
        "rank",
        message="Tell me your rank",
        validate=int_validator
    )
]

answers = inquirer.prompt(questions)

predict = []
for i in data["data"]:
    if(
        answers["college"].lower() in i["college"].lower() and
        i["quota"] in answers["quota"] and
        i["category"] in answers["category"] and
        i["seat_pool"] in answers["seat_pool"] and
        answers["streams"].lower() in i["stream"].lower() and
        i["closing_rank"] >= int(answers["rank"])
    ):
        predict.append(i)

if not predict:
    inquirer.text(message="Done. Press Enter to exit. ")
    exit()

predict.sort(key=lambda x: x["closing_rank"])

for i in predict:
    print(f"""----------------------------------------------------------
Name: {i["college"]}
Stream: {i["stream"]}
Round: {i["round"]}
Quota: {i["quota"]}
Category: {i["category"]}
Seat Pool: {i["seat_pool"]}
Opening Rank: {i["opening_rank"]}
Closing Rank: {i["closing_rank"]}
    """)


if inquirer.list_input("Save to file?",choices=['Yes', 'No']) == "Yes":
    fl_name = inquirer.text(message="Enter file name.")
    if not fl_name.endswith(".txt"): fl_name+=".txt"
    with open(fl_name, "w") as file:
        for i in predict:
            file.write(f"""----------------------------------------------------------
Name: {i["college"]}
Stream: {i["stream"]}
Round: {i["round"]}
Quota: {i["quota"]}
Category: {i["category"]}
Seat Pool: {i["seat_pool"]}
Opening Rank: {i["opening_rank"]}
Closing Rank: {i["closing_rank"]}
    """)
    inquirer.text(message="Done. Press Enter to exit. ")
    exit()
