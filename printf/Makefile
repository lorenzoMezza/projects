# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 11:15:46 by lmezzaba          #+#    #+#              #
#    Updated: 2026/05/20 11:15:50 by lmezzaba         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	=	libftprintf.a

SRC		=	ft_printf.c		\
			ft_put_char.c	\
			ft_put_str.c	\
			ft_put_nbr.c	\
			ft_put_uint.c	\
			ft_put_hex.c	\
			ft_put_ptr.c	\

OBJS	=	$(SRC:.c=.o)

CC		=	gcc
CFLAGS	=	-Wall -Werror -Wextra
AR		=	ar crs
RM		=	rm -rf

$(NAME):	$(OBJS)
	$(AR) $(NAME) $(OBJS)

all:		$(NAME)

clean:
	$(RM) $(OBJS)

fclean:		clean
	$(RM) $(NAME)

re:			fclean all

.PHONY:		all clean fclean re
