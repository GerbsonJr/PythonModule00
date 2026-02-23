# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: junior <junior@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 19:46:47 by junior            #+#    #+#              #
#    Updated: 2026/02/19 12:43:43 by junior           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")