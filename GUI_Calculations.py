import arcade

import Enumerators




def make_SpriteList_from_numbers(number_inn, x_position_inn, y_position_inn):
    sprite_list_temporary = arcade.SpriteList()
    SIZE_CONSTANT = 0.30
    string_number = str(number_inn)
    for x in range(len(string_number)):
        if string_number[x] == "0":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Zero.value, SIZE_CONSTANT))
        elif string_number[x] == "1":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.One.value, SIZE_CONSTANT))
        elif string_number[x] == "2":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Two.value, SIZE_CONSTANT))
        elif string_number[x] == "3":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Three.value, SIZE_CONSTANT))
        elif string_number[x] == "4":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Four.value, SIZE_CONSTANT))
        elif string_number[x] == "5":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Five.value, SIZE_CONSTANT))
        elif string_number[x] == "6":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Six.value, SIZE_CONSTANT))
        elif string_number[x] == "7":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Seven.value, SIZE_CONSTANT))
        elif string_number[x] == "8":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Eight.value, SIZE_CONSTANT))
        elif string_number[x] == "9":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Nine.value, SIZE_CONSTANT))
    for x in range(len(sprite_list_temporary)):
        sprite_list_temporary[x].center_x = x_position_inn + (x * 24)
        sprite_list_temporary[x].center_y = y_position_inn
    return sprite_list_temporary


def make_SpriteList_from_equipment_list(dwarf_in_backend, dwarf_in_frontend):
    equipment_sprite_list = arcade.SpriteList()
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.armor.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.weapon.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.ring.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.cloak.sprite, 0.20))
    for x in range(len(equipment_sprite_list)):
        equipment_sprite_list[x].center_x = dwarf_in_frontend.center_x + 50
        equipment_sprite_list[x].center_y = dwarf_in_frontend.center_y - 75 + (50*x)
    return equipment_sprite_list