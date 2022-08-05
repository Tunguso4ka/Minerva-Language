import os, sys, lexer, language
res = ''
shl = '\033[92m~$ \033[0m'
shlbasic = '\033[92m: \033[0m'
shdbg = False
version = "220731.1"

def shcmds():
    global res, shdbg
    res = res.split(' ')
    for i in res:
        i = str(i)
        i = i.split('=')
        match i[0]:
            case 'debug':
                if i[1] == 'true': language.debug = lexer.debug = shdbg = True
                else: language.debug = lexer.debug = shdbg = False
                if shdbg: print(shdbg, lexer.debug, language.debug)
            case 'exit': res = 'c'
            case 'clear': os.system('clear')
            case 'info': print('ml-shell 220416.1:\nAdded:\ngetmoduleversion lexer language ml-shell\nUpdated:\nlexer language modules')
            case 'version':
                print(f'main files: ml-shell({version}), language({language.version}), lexer({lexer.version})')
                line = 'used modules: '
                for i in language.names:
                    f = language.names[i]
                    if f.type == 'tt_module': line += f"{i}({f.version}) "
                print(line)
            case 'run':
                f = open(i[1]+'.minerva')
                lines = f.readlines()
                f.close()
                language.execute_code(lexer.lex(lines))
def sh():
    global res
    while res != 'c':
        res = input(shl)
        if 'shell' in res:shcmds()
        else: language.execute_code(lexer.lex(res))
#START
language.add_code()
print(f'Minerva Language\nml-shell({version}), language({language.version}), lexer({lexer.version})\nshell commands: exit debug=true/false info clear version')
#CHECK AND EXECUTE ARGUMENTS
if len(sys.argv) > 0:
    res = ''
    for i in sys.argv[1:]: res += str(i) + ' '
    if shdbg: print('arguments:', res)
    shcmds()
#START SH
sh()
