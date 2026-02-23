# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: junior <junior@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/19 16:04:36 by junior            #+#    #+#              #
#    Updated: 2026/02/19 16:57:09 by junior           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")