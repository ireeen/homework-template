import json
import random as r


class GameStart(object):
    def __init__(self, mode):
        self.mode = mode

    def word_generator(self, human_check):
        json_data = open('words.json').read()
        loaded_word = json.loads(json_data)
        rand_word = r.randint(0, len(loaded_word['words']) - 1)
        final_word = loaded_word['words'][rand_word]
        Computer.word_guess(final_word, human_check)

    def set_mode(self):
        if self.mode == '1':
            print('So, the word is: \n')
            human_check = False
            GameStart.word_generator(self, human_check)
        elif self.mode == '2':
            human_check = True
            print('Think up a word:')
            tword = input()
            if tword.isalpha():
                print('So, the word is: \n')
                Human.word_guess(tword, human_check)
            else:
                print('Use only english letters!')
                GameStart('2').set_mode()
        else:
            raise KeyboardInterrupt


class Computer(object):
    def __init__(self, word):
        self.word = word

    def word_guess(self, human_check):
        spaces = list()
        attempts = 4
        amount = 0
        for i in range(len(self)):
            spaces.append(' _')
            s = ''.join(spaces)
        print(s)
        while attempts != 0:
            print('Guess the letter (lowercase):')
            letter = input()
            if (letter in self) and (letter != '') and (len(letter) == 1):
                print('Nice!')
                amount += 1
                for i in range(len(self)):
                    if letter == self[i]:
                        spaces[i] = letter
                s = ' '.join(spaces)
                print(s)
                if '_' not in s:
                    print('YOU WON! \nAttempts left: {} \n'
                          'Number of guessed letters: {} '
                          .format(attempts, amount))
                    Human.get_status('win', human_check)
                    break
                else:
                    continue
            else:
                attempts -= 1
                print('Wrong! {} attempts left!'.format(attempts))
                if attempts == 3:
                    print(' ┌ \n │\n │\n ┴')
                elif attempts == 2:
                    print(' ┌----┐ \n │\n │\n ┴')
                elif attempts == 1:
                    print(' ┌----┐ \n │    │\n │\n ┴')
                elif attempts == 0:
                    print(' ┌----┐ \n │    │\n │ (✖╭╮✖)\n ┴')
                    print('YOU LOSE!')
                    Human.get_status('lose', human_check)
                    break


class Statistics(object):
    p1 = 0
    p2 = 0
    rounds = 1


class Human(Computer, Statistics):
    def get_status(self, human_check):
            if human_check is True:
                while (Statistics.p1 < 2) and (Statistics.p2 < 2):
                    if Statistics.rounds % 2 == 1:
                        if self == 'lose':
                            Statistics.p2 += 1
                        elif self == 'win':
                            Statistics.p1 += 1
                    else:
                        if self == 'lose':
                            Statistics.p1 += 1
                        elif self == 'win':
                            Statistics.p2 += 1
                    print('Score {} : {}'.format(Statistics.p1, Statistics.p2))
                    Statistics.rounds += 1
                    if Statistics.p1 == 2:
                        print('P1 WON!')
                        return True
                    elif Statistics.p2 == 2:
                        print('P2 WON!')
                        return True
                    else:
                        GameStart('2').set_mode()
            else:
                pass


def main():
    print('Select mode:\n'
          '1. Playing with computer \n'
          '2. Playing with human \n'
          'Enter. Exit')
    m = input()
    mode = GameStart(m)
    mode.set_mode()


if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('Goodbye!')