from Analyser import Analyser

if __name__ == '__main__':
    analyser = Analyser()
    print('First def example: \n' + str(analyser.get_group_amount_of_members(1000)))
    print('Second def example: \n' + str(analyser.get_group_amount_of_members(10, 99989)))
