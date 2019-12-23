from pyfmodex.structures import REVERB_PROPERTIES

"""
Sets of predefined reverb properties. 
Source: https://documentation.help/FMOD-API/FMOD_REVERB_PRESETS.html
"""

reverb_list = []  # reverb list (reverbProperties, reverbName)

reverb_off = REVERB_PROPERTIES(
    1000, 7, 11, 5000, 100, 100, 100, 250, 0, 20, 96, -80.0)
reverb_list.append([reverb_off, "OFF"])

reverb_generic = REVERB_PROPERTIES(
    1500, 7, 11, 5000, 83, 100, 100, 250, 0, 14500, 96, -8.0)
reverb_list.append([reverb_generic, "GENERIC"])

reverb_paddedcell = REVERB_PROPERTIES(
    170, 1, 2, 5000, 10, 100, 100, 250, 0, 160, 84, -7.8)
reverb_list.append([reverb_paddedcell, "PADDEDCELL"])

reverb_stoneroom = REVERB_PROPERTIES(
    2300, 12, 17, 5000, 64, 100, 100, 250, 0, 7800, 71, -8.5)
reverb_list.append([reverb_stoneroom, "STONEROOM"])

reverb_hangar = REVERB_PROPERTIES(
    10000, 20, 30, 5000, 23, 100, 100, 250, 0, 3400, 72, -7.4)
reverb_list.append([reverb_hangar, "HANGAR"])

reverb_carpettedhallway = REVERB_PROPERTIES(
    300, 2, 30, 5000, 10, 100, 100, 250, 0, 500, 56, -24.0)
reverb_list.append([reverb_carpettedhallway, "CARPETTEDHALLWAY"])

reverb_hallway = REVERB_PROPERTIES(
    1500, 7, 11, 5000, 59, 100, 100, 250, 0, 7800, 87, -5.5)
reverb_list.append([reverb_hallway, "HALLWAY"])

reverb_stonecorridor = REVERB_PROPERTIES(
    270, 13, 20, 5000, 79, 100, 100, 250, 0, 9000, 86, -6.0)
reverb_list.append([reverb_stonecorridor, "STONECORRIDOR"])

reverb_alley = REVERB_PROPERTIES(
    1500, 7, 11, 5000,  86, 100, 100, 250, 0, 8300, 80, -9.8)
reverb_list.append([reverb_alley, "ALLEY"])

reverb_cave = REVERB_PROPERTIES(
    2900, 15, 22, 5000, 100, 100, 100, 250, 0, 20000, 59, -11.3)
reverb_list.append([reverb_cave, "CAVE"])

reverb_room = REVERB_PROPERTIES(
    400, 2, 3, 5000, 83, 100, 100, 250, 0, 6050,  88, -9.4)
reverb_list.append([reverb_room, "ROOM"])

reverb_bathroom = REVERB_PROPERTIES(
    1500, 7, 11, 5000, 54, 100, 60, 250, 0,  2900,  83, 0.5)
reverb_list.append([reverb_bathroom, "BATHROOM"])

reverb_livingroom = REVERB_PROPERTIES(
    500, 3, 4, 5000, 10, 100, 100, 250, 0, 160, 58, -19.0)
reverb_list.append([reverb_livingroom, "LIVINGROOM"])

reverb_auditorium = REVERB_PROPERTIES(
    4300, 20, 30, 5000, 59, 100, 100, 250, 0, 5850, 64, -11.7)
reverb_list.append([reverb_auditorium, "AUDITORIUM"])

reverb_mountains = REVERB_PROPERTIES(
    1500, 300, 100, 5000, 21, 27, 100, 250, 0, 1220, 82, -24.0)
reverb_list.append([reverb_mountains, "MOUNTAINS"])

reverb_underwater = REVERB_PROPERTIES(
    1500, 7, 11, 5000, 10, 100, 100, 250, 0, 500, 92, 7.0)
reverb_list.append([reverb_underwater, "UNDERWATER"])

reverb_forest = REVERB_PROPERTIES(
    1500, 162, 88, 5000, 54, 79, 100, 250, 0, 760, 94, -12.3)
reverb_list.append([reverb_forest, "FOREST"])

reverb_arena = REVERB_PROPERTIES(
    7200, 20, 30, 5000, 33, 100, 100, 250, 0, 4500, 80, -9.6)
reverb_list.append([reverb_arena, "ARENA"])

reverb_city = REVERB_PROPERTIES(
    1500, 7, 11, 5000, 67, 50, 100, 250, 0, 4050, 66, -26.0)
reverb_list.append([reverb_city, "CITY"])

reverb_sewerpipe = REVERB_PROPERTIES(
    2800, 14, 21, 5000, 14, 80, 60, 250, 0, 3400, 66, 1.2)
reverb_list.append([reverb_sewerpipe, "SEWERPIPE"])

reverb_concerthall = REVERB_PROPERTIES(
    3900, 20, 29, 5000, 70, 100, 100, 250, 0, 5650, 80, -9.8)
reverb_list.append([reverb_concerthall, "CONCERTHALL"])

reverb_quarry = REVERB_PROPERTIES(
    1500, 61, 25, 5000, 83, 100, 100, 250, 0, 3400, 100, -5.0)
reverb_list.append([reverb_quarry, "QUARRY"])

reverb_plain = REVERB_PROPERTIES(
    1500, 179, 100, 5000, 50, 21, 100, 250, 0, 1670, 65, -28.0)
reverb_list.append([reverb_plain, "PLAIN"])

reverb_parkinglot = REVERB_PROPERTIES(
    1700, 8, 12, 5000, 100, 100, 100, 250, 0, 20000, 56, -19.5)
reverb_list.append([reverb_parkinglot, "PARKINGLOT"])


def getReverbByIndex(index):
    """
    Gets a reverb from the list by the given index. (index % reverbList.length)
    """
    value = index % len(reverb_list)
    return reverb_list[value]
