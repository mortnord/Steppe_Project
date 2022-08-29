import arcade
from arcade.gui import UITextArea, UITexturePane

import Enumerators
from Static_Data import Static_Data


def make_SpriteList_from_numbers(number_inn, x_position_inn, y_position_inn):
    sprite_list_temporary = arcade.SpriteList()
    SIZE_CONSTANT = 0.30
    string_number = str(number_inn)
    for number in string_number:
        if number == "0":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Zero.value, SIZE_CONSTANT))
        elif number == "1":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.One.value, SIZE_CONSTANT))
        elif number == "2":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Two.value, SIZE_CONSTANT))
        elif number == "3":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Three.value, SIZE_CONSTANT))
        elif number == "4":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Four.value, SIZE_CONSTANT))
        elif number == "5":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Five.value, SIZE_CONSTANT))
        elif number == "6":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Six.value, SIZE_CONSTANT))
        elif number == "7":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Seven.value, SIZE_CONSTANT))
        elif number == "8":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Eight.value, SIZE_CONSTANT))
        elif number == "9":
            sprite_list_temporary.append(arcade.Sprite(Enumerators.Numbers.Nine.value, SIZE_CONSTANT))
    for x, temp_list in enumerate(sprite_list_temporary):
        temp_list.center_x = x_position_inn + (x * 24)
        temp_list.center_y = y_position_inn
    return sprite_list_temporary


def create_card_indicators_from_backend():
    pass


def make_SpriteList_from_equipment_list(dwarf_in_backend, dwarf_in_frontend, scaling_x, scaling_y):
    equipment_sprite_list = arcade.SpriteList()
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.armor.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.weapon.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.ring.sprite, 0.20))
    equipment_sprite_list.append(arcade.Sprite(dwarf_in_backend.cloak.sprite, 0.20))
    for x, equipment in enumerate(equipment_sprite_list):
        equipment.center_x = (dwarf_in_frontend.center_x + 50) / scaling_x
        equipment.center_y = (dwarf_in_frontend.center_y - 75 + (50 * x)) / scaling_y
    return equipment_sprite_list


def make_panel_from_card(mouse_x, mouse_y, card_clicked_on):
    string_to_print = ""
    string_to_print += str(card_clicked_on.value) + " "
    string_to_print += str(card_clicked_on.type_of_card_general.value) + "\n"
    string_to_print += str(card_clicked_on.energy_required)
    string_to_print += " energy to use \n"
    string_to_print += card_clicked_on.text
    if card_clicked_on.one_time:
        string_to_print += "One time use per combat"
    text_area = UITextArea(x=mouse_x, y=mouse_y, width=150, height=50, text=string_to_print, text_color=(0, 0, 0, 255))
    return UITexturePane(text_area.with_space_around(right=20), tex=Static_Data.get_bg_text_panel(),
                         padding=(10, 10, 10, 10))


def make_panel_from_item(mouse_x, mouse_y, item_clicked_on):
    string_to_print = ""
    if item_clicked_on.bonus_attack > 0:
        string_to_print += str(item_clicked_on.bonus_attack) + " Bonus Attack \n"
    if item_clicked_on.bonus_defend > 0:
        string_to_print += str(item_clicked_on.bonus_defend) + " Bonus Defend \n"
    string_to_print += item_clicked_on.text

    text_area = UITextArea(x=mouse_x, y=mouse_y, width=150, height=50, text=string_to_print, text_color=(0, 0, 0, 255))
    return UITexturePane(text_area.with_space_around(right=20), tex=Static_Data.get_bg_text_panel(),
                         padding=(10, 10, 10, 10))
