import inquirer

def select_input_file(choices = ['example.txt', 'input.txt']):
    questions = [
        inquirer.List('choice',
                    message="select file to read?",
                    choices=choices,
                ),
    ]
    return inquirer.prompt(questions)['choice']

# print(select_input_file())
