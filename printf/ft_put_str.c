/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_str.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:15:13 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:22 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_put_str(char *s, size_t *count)
{
	if (!s)
		s = "(null)";
	while (*s)
	{
		ft_put_char(*s, count);
		s++;
	}
}
