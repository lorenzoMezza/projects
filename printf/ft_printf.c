/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:14:21 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:40 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	ft_handle_hex(va_list ap, char spec, size_t *count)
{
	if (spec == 'x')
		ft_put_hex(va_arg(ap, unsigned int), count, BASE_HEX_LO);
	else
		ft_put_hex(va_arg(ap, unsigned int), count, BASE_HEX_UP);
}

static void	ft_dispatch(va_list ap, char spec, size_t *count)
{
	if (spec == 'c')
		ft_put_char(va_arg(ap, int), count);
	else if (spec == 's')
		ft_put_str(va_arg(ap, char *), count);
	else if (spec == 'p')
		ft_put_ptr(va_arg(ap, void *), count);
	else if (spec == 'd' || spec == 'i')
		ft_put_nbr(va_arg(ap, int), count);
	else if (spec == 'u')
		ft_put_uint(va_arg(ap, unsigned int), count);
	else if (spec == 'x' || spec == 'X')
		ft_handle_hex(ap, spec, count);
	else if (spec == '%')
		ft_put_char('%', count);
}

int	ft_printf(char const *fmt, ...)
{
	va_list	ap;
	size_t	count;

	if (!fmt)
		return (0);
	count = 0;
	va_start(ap, fmt);
	while (*fmt)
	{
		if (*fmt == '%')
		{
			fmt++;
			ft_dispatch(ap, *fmt, &count);
		}
		else
			ft_put_char(*fmt, &count);
		fmt++;
	}
	va_end(ap);
	return (count);
}
