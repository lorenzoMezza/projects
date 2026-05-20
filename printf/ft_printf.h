/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lmezzaba <mezzabarba.lorenzo@gmail.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 11:14:31 by lmezzaba          #+#    #+#             */
/*   Updated: 2026/05/20 11:15:38 by lmezzaba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

# define BASE_HEX_UP "0123456789ABCDEF"
# define BASE_HEX_LO "0123456789abcdef"

int		ft_printf(char const *fmt, ...);

void	ft_put_char(char c, size_t *count);
void	ft_put_str(char *s, size_t *count);
void	ft_put_nbr(int n, size_t *count);
void	ft_put_uint(unsigned int n, size_t *count);
void	ft_put_hex(unsigned int n, size_t *count, char *base);
void	ft_put_ptr(void *p, size_t *count);

#endif
