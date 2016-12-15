from collections import defaultdict as __default_dict


def __make_change(data):
    for ix in xrange(len(data)):
        if ix > 1 and data[ix-2].startswith('inc ') and data[ix-1].startswith('dec ') and data[ix]:
            dn = data[ix-1][-1]
            if data[ix] == 'jnz %s -2' % dn:
                up = data[ix-2][-1]
                before = data[:ix-2]
                after = data[ix+1:]
                newlines = ['nop', 'inc %s %s' % (dn, up), 'cpy 0 %s' % dn]
                return before + newlines + after

        if data[ix].startswith('jnz 1'):
            jump_val = data[ix].split()[-1]
            fixed = 'jmp %s' % jump_val
            data[ix] = fixed
    return None


def __pre_process(data):
    while True:
        new_data = __make_change(data)
        if new_data is None:
            return data
        data = new_data


def __parse(x, registers):
    if x is None:
        return x
    try:
        return int(x)
    except ValueError:
        return registers[x]


def __parts(words, val):
    cmd = words[0]
    target = words[-1]
    argument = None
    if len(words) > 2:
        argument = val(words[1])
    if cmd.startswith('j'):
        target, argument = argument, val(target)
    return cmd, target, argument


def run_program(data, **kwargs):
    data = __pre_process(data)

    register = __default_dict(int)

    def val(x):
        return __parse(x, register)

    program = map(str.split, data)

    for k in kwargs.keys():
        register[k] = kwargs[k]

    ix = 0
    while 0 <= ix < len(program):
        cmd, target, argument = __parts(program[ix], val)
        ix += 1
        if cmd == 'cpy':
            register[target] = val(argument)
        elif cmd == 'inc':
            register[target] += 1 if argument is None else argument
            continue
        elif cmd == 'dec':
            register[target] -= 1 if argument is None else argument
            continue
        elif cmd == 'jnz':
            if target != 0:
                ix -= 1
                ix += argument
        elif cmd == 'jmp':
            ix -= 1
            ix += argument
        elif cmd == 'nop':
            pass
        else:
            print 'unknown command:', cmd
            exit(1)
    return register
