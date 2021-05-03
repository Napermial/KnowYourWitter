import argparse
from know_your_witter.typer import guess
from threading import Thread
from time import sleep


def parse_arguments():
    parser = argparse.ArgumentParser(prog="KnowYourWitter",
                                     description='Command line utility for twitter based personality guessing')
    parser.add_argument('username', metavar='-u',
                        help='the twitter handle of the user')
    parser.add_argument('--version', action='version', version='%(prog)s 0.01 Beta')

    return parser.parse_args().username


def guess_type(username):
    print(f"accessing twitter API for the tweets of {username} ")

    guesser = Thread(target=guess.guess_personality(username), daemon=True)
    guesser.start()
    while guesser.is_alive():
        print("loading.")
        sleep(0.5)
        print("loading..")
        sleep(0.5)
        print("loading...")
        sleep(0.5)
    guesser.join()



if __name__ == '__main__':
    username = parse_arguments()
    guess_type(username)