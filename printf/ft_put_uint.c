/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_uint.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:15:17 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:55 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_put_uint(unsigned int n, size_t *count)
{
	if (n > 9)
		ft_put_uint(n / 10, count);
	ft_put_char('0' + n % 10, count);
}
