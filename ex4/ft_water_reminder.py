# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: junior <junior@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 19:40:53 by junior            #+#    #+#              #
#    Updated: 2026/02/19 12:43:38 by junior           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
    water = int(input("Days since last watering: "))
    if water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")