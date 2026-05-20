/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_hex.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:14:57 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:31 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_put_hex(unsigned int n, size_t *count, char *base)
{
	if (n >= 16)
		ft_put_hex(n / 16, count, base);
	ft_put_char(base[n % 16], count);
}
