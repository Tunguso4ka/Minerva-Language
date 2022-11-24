import modules.notforuse.getvalue as getvalue, mtoken
version = "2022.11.24.1"
type = "tt_module"

def main(values, names, levels, position):
    result = None
    nvalues = []
    for i in values:
        if i.type != 'tt_comma': nvalues.append(getvalue.get(i, names))
    if len(nvalues) == 2: result = nvalues[0][:nvalues[1]]
    elif len(nvalues) == 3: result = nvalues[0][nvalues[1]:nvalues[2]]
    return mtoken.t('tt_char', result), names, levels, position
