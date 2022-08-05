from datetime import datetime

position = 0
version = "2022.07.31.1"
debug = False
stop = False
names = {}
levels = []

class ccode():
    def __init__(self, name, startpos=0, currentpos=0):
        self.name = name
        self.value = 0
        self.startpos = startpos
        self.currentpos = currentpos
        self.do = True
        self.type = 'code'
    def level_end(self, names, levels, position):
        show_error('\033[91mEE', names[levels[-1]], 'error"Trying to end code":}')
        return names, levels, position

class template:
  def __init__(self, name='template', startpos=position, currentpos=position):
    self.name = name
    self.value = 0
    self.startpos = startpos
    self.currentpos = currentpos
    self.do = False
    self.type = 'template'
  def level_end(self, names, levels, position):
    levels.pop()
    return names, levels, position

def add_code():
    names['code'] = ccode('code', 0, position)
    levels.append('code')
    names['use'] = __import__('modules.usemodule', fromlist = [' '])
    names['remove'] = __import__('modules.removemodule', fromlist = [' '])

def show_error(type, module, code):
    examples = ['\033[91mEE', '\033[33mWW']
    try: print(f"{type} type:'{module.type}' name:'{module.name}' pos:{module.currentpos} msg:'{code}' \033[0m")
    except: print(f"{type} {module} {code} \033[0m")

def execute_line(line):
    global names, levels, position, value
    if names[levels[-1]].do != True:
        match line[-1].value:
            case '{':
                levels.append(template('skip'))
            case '}':
                levels.pop()
    elif line[-1].value == '}':
        names, levels, position = names[levels[-1]].level_end(names, levels, position)
    elif line[0].value in names and  names[line[0].value].type in ["tt_module"]:
        execute_module(line)
    else:
        show_error('\033[33mWW', names['code'], f"{line[0].value} not found in names.'")

#write(read());
#char a = read();
#if 5 == 2 + 3 == 5 {} => if formulas([5 == 2 + 3 == 5]) {}

def execute_module(gline):
    global names, levels, position
    line = []
    for i in gline:
        line.append(i)
    num = []
    f = 0
    while len(line) > f:
        if line[f].type in ['tt_module', 'tt_unknown'] and line[f+1].type in ['tt_int', 'tt_float', 'tt_char', 'tt_bool', 'tt_unknown', 'tt_parenthes_open', 'tt_braces_open']:
            num.append(f)
        f+=1
    a = 0
    while len(num) > 0:
        if debug:
            print('NUM:', num)
            print("START", position)
            for i in line:
                print(i.type, i.value)
            print("END")
            
        f = num[-1]
        a = i = f+1
        while len(line) > i:
            if line[i].type in ['tt_parenthes_open']:
                a = i + 1
            elif line[i].type in ['tt_parenthes_close', 'tt_braces_open']:
                break
            elif line[i].value in ['=', '+=', '-=', '*=', '/=', '//=', '%=']:
                i += 2
                break
            elif line[i].value in ['++', '--']:
                i += 1
                break
            i += 1
        value, names, levels, position = names[line[f].value].main(line[a:i], names, levels, position)
        a = 0
        while i > f:
            line.pop(i)
            i-=1
            a+=1
        if value != None:
            line[f] = value
        else:
            line.pop(f)
        num.pop()

def execute_code(clines):
    global position
    position = 0
    while len(clines) > position:
        if debug: print(position, clines[position], levels)
        execute_line(clines[position])
        position += 1
