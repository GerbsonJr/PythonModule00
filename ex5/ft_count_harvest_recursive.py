# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: junior <junior@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/19 12:47:39 by junior            #+#    #+#              #
#    Updated: 2026/02/19 15:52:36 by junior           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	count(day, total):
    if day > total:
        print("Harvest time!")
        return
    print(f"Day {day}")
    count(day + 1, total)

def	ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count(1, days)