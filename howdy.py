from pyfiglet import Figlet
from plumbum import cli
from questionary import prompt
import questionary

def print_banner(text):
    print(Figlet(font='starwars').renderText(text))

#ask questions
answers = questionary.form(
    answer_date = questionary.text("What day is today ?"),
    howdy = questionary.select("how's your day so far ?", choices=["good", "soso", "bad"]),
    special = questionary.text("what is one thing special about today? ")
).ask()

#store the answer to mood.txt in new line
date = answers['answer_date']
mood = answers['howdy']
with open('mood.txt', 'a') as f :
    f.write(date + ' ' + mood+ "\n" )


#reads the moood.txt file and get data
with open('mood.txt', 'r') as a :
    lines = a.readlines()
    count = 0
    good = 0
    soso = 0
    bad = 0
    for line in lines :
        count += 1
        if "good" in line :
            good += 1
        elif "soso" in line :
            soso += 1
        else :
            bad +=1

good_rate = good/count 
soso_rate = soso/count
bad_rate = bad/count
if soso_rate > good_rate or bad_rate > good_rate :
    print('recently you are not having a good mood, talk to some friends !')
else :
    print('You are doing good! your average good rate is: ', good_rate)
        


class Howdy(cli.Application):
    VERSION = "1.0"
    good = cli.Flag(["g", "good"], help = "Hope you are having a good day")

    def main(self):
        print_banner("Howdy")
        

if __name__ == "__main__":
    Howdy()

def test_store_answers() :
    assert len(lines) == 10, 'the lines should be updating '

def test_format_answers() :
    assert len(line.split()) == 2, 'there should be only 2 data stored '

