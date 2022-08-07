# Minerva-Language
a python-based language with Rust like syntaxis.

##### How to run a Minerva Language?
Terminal:
```
python shell.py [args]
```
or by doubleclick on shell.py

##### How to run a .minerva app?
to run a.minerva in folder apps:
write in Minerva Shell
```
shell run=apps/a
```

##### Hello, World! example:
```
use (write);
write ("Hello, World!");
```

##### comment example:
```
#hello! Minerva supports comments like other normal languages.
```

##### while example:
```
use (let, write, while, sleep);
int a = 6;
while (solve(a!=0) {
  write (a);
  int a--;
  sleep(1);
}
```

##### switch example:
```
use(switch, case, write);
switch "a" {
  case "a" {
    write("case A");
  }
  case "b" {
    write("case B");
  }
}
```

##### fn example:
```
use(fn, write);
fn (hello) {
  write("hello Minerva!");
}

hello();
```
