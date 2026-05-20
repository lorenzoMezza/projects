/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_nbr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:14:51 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:29 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_put_nbr(int n, size_t *count)
{
	if (n == -2147483648)
	{
		ft_put_nbr(n / 10, count);
		ft_put_char('8', count);
	}
	else if (n < 0)
	{
		ft_put_char('-', count);
		ft_put_nbr(-n, count);
	}
	else
	{
		if (n > 9)
			ft_put_nbr(n / 10, count);
		ft_put_char('0' + n % 10, count);
	}
}
