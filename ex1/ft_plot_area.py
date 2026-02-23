# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: junior <junior@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 16:50:19 by junior            #+#    #+#              #
#    Updated: 2026/02/19 12:43:21 by junior           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    total = length * width
    print(f"Plot area: {total}")