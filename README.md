# Minerva-Language
a python-based language with Rust like syntaxis.

##### How to run a Minerva Language?
Terminal:
```
python3 shell.py
```
or by doubleclick on shell.py

##### How to run a .mlapp app?
to run a.mlapp in folder apps:
write in Minerva Shell
```
shell run apps/a
```

##### Hello, World! example:
```
use write;
write "Hello, World!";
```

##### while example:
```
use let write while;
let a = 5;
while a != 0 {
   write a " thanks for using Minerva Language!";
   let a--;
}
```

##### switch example:
```
use let write switch case;
let a = 5;
switch a {
   case 0 { write a " == 0"; }
   case 1 { write a " == 1"; }
   case 2323235734 { write a " == some big numbers"; }
}
```

##### function example:
```
use write fn;

fn a() {
  write "write in a()";
}

write "write before a()";
fn a();
```
