/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_ptr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <lmezzaba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:15:09 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/21 11:53:06 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	ft_put_addr(unsigned long addr, size_t *count)
{
	if (addr >= 16)
		ft_put_addr(addr / 16, count);
	ft_put_char(BASE_HEX_LO[addr % 16], count);
}

void	ft_put_ptr(void *p, size_t *count)
{
	if (!p)
	{
		ft_put_str("(nil)", count);
		return ;
	}
	ft_put_str("0x", count);
	ft_put_addr((unsigned long)p, count);
}
