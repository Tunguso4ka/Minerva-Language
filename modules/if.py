import modules.notforuse.getvalue, random
version = "220425.1"
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
    levels.pop()
    return names, levels, position

def main(values, names, levels, position):
    name = f'if{str(position)}-{str(random.randint(0,999))}'
    do = modules.notforuse.getvalue.get(values[0], names)
    names[name] = template(name, do, position, position)
    levels.append(name)
    return None, names, levels, position
