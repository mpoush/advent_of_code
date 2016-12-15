from assembunny import run_program
import helpers


def run(program, **kwargs):
    return run_program(program, **kwargs)['a']


if __name__ == '__main__':
    input_data = helpers.get_all_lines('day11_input.txt')
    print run(input_data)
    print run(input_data) == 317993
    print run(input_data, c=1)
    print run(input_data, c=1) == 9227647
