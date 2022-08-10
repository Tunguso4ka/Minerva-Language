import modules.notforuse.getvalue as getvalue, random
version = "2022.08.07.1"
type = "tt_module"

class template:
    def __init__(self, name, do, startpos, currentpos):
        self.name = name
        self.do = do
        self.startpos = startpos
        self.currentpos = currentpos
        self.type = "case"
    def level_end(self, names, levels, position):
        levels.pop()
        return names, levels, position

def main(values, names, levels, position):
    do = False
    name = f'case{str(position)}-{str(random.randint(0,999))}'
    if names[levels[-1]].type != 'switch': print('EE case must be in switch section')
    else: do = getvalue.get(names[levels[-1]], names) == getvalue.get(values[0], names)
    #print(getvalue.get(names[levels[-1]], names), getvalue.get(values[0], names) ,do)
    names[name] = template(name, do, position, position)
    levels.append(name)
    return None, names, levels, position

