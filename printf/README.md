*This project has been created as part of the 42 curriculum by lmezzaba.*

## Description

ft_printf is a re-implementation of the standard C library function `printf()`.
The goal is to learn how variadic functions work in C by handling a variable
number of arguments passed to a single function. The result is compiled into
a static library `libftprintf.a` that can be linked into any C project.

Supported conversions:

| Specifier | Description |
|-----------|-------------|
| `%c` | Prints a single character |
| `%s` | Prints a string |
| `%p` | Prints a pointer address in hexadecimal |
| `%d` | Prints a decimal integer |
| `%i` | Prints an integer in base 10 |
| `%u` | Prints an unsigned decimal integer |
| `%x` | Prints a number in hexadecimal lowercase |
| `%X` | Prints a number in hexadecimal uppercase |
| `%%` | Prints a literal percent sign |

## Algorithm and Data Structure

The format string is parsed character by character inside `ft_printf()`.
When a `%` is encountered, the next character is forwarded to `ft_dispatch()`,
which selects the correct output function through a chain of `if/else if`.
Each helper function (`ft_put_char`, `ft_put_str`, `ft_put_nbr`, `ft_put_uint`,
`ft_put_hex`, `ft_put_ptr`) is responsible for one conversion type and writes
directly to stdout via `write()`.

All helper functions receive a pointer to a `size_t` counter that tracks the
total number of characters written. This counter is returned by `ft_printf()`
as an `int` at the end, matching the behavior of the original `printf()`.

Numeric conversions (`%d`, `%u`, `%x`, `%X`, `%p`) use recursion to print
digits in the correct order without needing a temporary buffer or `malloc`.
The special case of `INT_MIN` (-2147483648) is handled explicitly in
`ft_put_nbr()` because negating it causes undefined behavior in C.

Internal helper functions that are not part of the public interface are declared
`static` to limit their visibility to their own translation unit, avoiding
name conflicts across the library.

No buffer management is implemented, as the subject explicitly forbids it.

## Instructions

**Compile the library:**
```
make
```

**Link it in your project:**
```
gcc main.c -L. -lftprintf -o program
```

**Example usage in code:**
```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hello, %s! Number: %d\n", "world", 42);
    return (0);
}
```

**Clean object files:**
```
make clean
```

**Remove everything including the library:**
```
make fclean
```

**Recompile from scratch:**
```
make re
```

## Resources

- printf manual page: https://man7.org/linux/man-pages/man3/printf.3.html
- Variadic functions in C (stdarg.h): https://en.cppreference.com/w/c/variadic
- ar command documentation: https://man7.org/linux/man-pages/man1/ar.1.html
