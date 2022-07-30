class t:
    def __init__(self, type="NONE", value="NONE"):
        self.type = type
        self.value = value

tokens = {
    "-": "tt_sub",
    "--": "tt_decrement",
    "-=": "tt_sub_and_equal",
    "+": "tt_add",
    "++": "tt_increment",
    "+=": "tt_add_and_equal",
    "*": "tt_mul",
    "*=": "tt_mul_and_equal",
    "/": "tt_div",
    "/=": "tt_div_and_equal",
    "//": "tt_div_without_remaind",
    "//=": "tt_div_without_remaind_and_equal",
    "%": "tt_rem",
    "%=": "tt_rem_and_equal",
    "=": "tt_equal",
    "==": "tt_equallity",
    "<": "tt_less",
    "<<": "tt_left_shift",
    "<=": "tt_less_or_equal",
    ">": "tt_greater",
    ">>": "tt_right_shift",
    ">=": "tt_greater_or_equal",
    "!": "tt_not",
    "!=": "tt_not_equal",
    "none": "tt_none",
    ";": "tt_line_end",
    "{": "tt_braces_open",
    "}": "tt_braces_close",
    "(": "tt_parenthes_open",
    ")": "tt_parenthes_close",
    "[": "tt_brackets_open",
    "]": "tt_brackets_close",
    ",": "tt_comma",
    "&&": "tt_and",
    "||": "tt_or",
    True: "tt_bool",
    False: "tt_bool",
    "toint": "tt_converttype",
    "tofloat": "tt_converttype",
    "tobool": "tt_converttype",
    "tochar": "tt_converttype",
    "": ""
}