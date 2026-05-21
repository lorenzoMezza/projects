NAME    =   libftprintf.a

SRC     =   ft_printf.c     \
            ft_put_char.c   \
            ft_put_str.c    \
            ft_put_nbr.c    \
            ft_put_uint.c   \
            ft_put_hex.c    \
            ft_put_ptr.c    \

BONUS_SRC = ft_printf_bonus.c    \
            ft_put_char_bonus.c  \
            ft_put_str_bonus.c   \
            ft_put_nbr_bonus.c   \
            ft_put_uint_bonus.c  \
            ft_put_hex_bonus.c   \
            ft_put_ptr_bonus.c   \

OBJS        = $(SRC:.c=.o)
BONUS_OBJS  = $(BONUS_SRC:.c=.o)

CC      =   gcc
CFLAGS  =   -Wall -Werror -Wextra
AR      =   ar crs
RM      =   rm -rf

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

all: $(NAME)

bonus: $(BONUS_OBJS)
	$(AR) $(NAME) $(BONUS_OBJS)

clean:
	$(RM) $(OBJS) $(BONUS_OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re bonus