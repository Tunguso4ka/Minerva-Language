import modules.notforuse.getvalue, random
version = "220730.1"
type = "tt_module"

class template:
  def __init__(self, name='template', do=False, startpos=0, currentpos=0):
    self.name = name
    self.value = 0
    self.startpos = startpos
    self.currentpos = currentpos
    self.do = do
    self.type = 'if'
  def level_end(self, names, levels, position):
    if self.do == True: position = self.startpos - 1
    else:
        self.do = False
        levels.pop()
    return names, levels, position

def main(values, names, levels, position):
    do = modules.notforuse.getvalue.get(values[0], names)
    if levels[-1].split('-')[0] != f'while{str(position)}':
        name = f'while{str(position)}-{str(random.randint(0,999))}'
        levels.append(name)
    else: name = levels[-1]
    names[name] = template(name, do, position, position)
    return None, names, levels, position
