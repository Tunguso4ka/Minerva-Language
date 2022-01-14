import language, os
#bool
shell_stop = False
#string
shell_input_text = "\033[92m~$ \033[0m"
shell_command_name = "shell"
#
def shell_commands(lresult):
  global shell_stop, shell_input_text, shell_command_name
  if lresult[1] in ['exit', 'stop']:
    shell_stop = True
  elif lresult[1] == 'input_text':
    shell_input_text = input('in:')
  elif lresult[1] == 'language':
    print(language.version)
  elif lresult[1] == 'debug':
    language.debug = not language.debug
    print(language.debug)
  elif lresult[1] == 'clear':
    language.modules = {}
    language.names = {}
    language.levels = []
    language.linenum = 0
    language.add_code()
    os.system('clear')
    print("Minerva Language", language.version, "\nshell commands: exit/stop run clear debug language input_text info")
  elif lresult[1] == 'run':
    shell_commands([shell_command_name,'clear'])
    print(shell_input_text + lresult[0],lresult[1], lresult[2])
    language.run_file(lresult[2] + '.mlapp')
  elif lresult[1] == 'rename':
    shell_command_name = input('in:')
  elif lresult[1] == 'info':
    print('ML 220114.1:\nAdded:\nshell info\nmodules mathformulas getvalue\nUpdated:\nmodules boolformulas if int bool while write let')
#
def lex(result):
  lresult = result.split(' ')
  if lresult[0] == shell_command_name:
    shell_commands(lresult)
  else:
    language.linenum = 0
    language.lex(result)
#
def proccess():
  while shell_stop == False:
    result = input(shell_input_text)
    lex(result)
#start
os.system('clear')
print("Minerva Language", language.version, "\nshell commands: exit/stop run clear debug language input_text")
proccess()
