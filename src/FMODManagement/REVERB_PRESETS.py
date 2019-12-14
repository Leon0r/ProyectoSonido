from pyfmodex.structures import REVERB_PROPERTIES

"""
Sets of predefined reverb properties. 
Source: https://documentation.help/FMOD-API/FMOD_REVERB_PRESETS.html
"""

reverb_cave = REVERB_PROPERTIES(2900, 15, 22, 5000, 100, 100, 100, 250, 0, 20000, 59, -11.3)
reverb_room = REVERB_PROPERTIES(400, 2, 3, 5000, 83, 100, 100, 250, 0, 6050,  88, -9.4)
reverb_bathroom = REVERB_PROPERTIES(1500, 7, 11, 5000, 54, 100, 60, 250, 0,  2900,  83, 0.5)
reverb_livingroom = REVERB_PROPERTIES(500, 3, 4, 5000, 10, 100, 100, 250, 0, 160, 58, -19.0)
reverb_auditorium = REVERB_PROPERTIES(4300, 20, 30, 5000, 59, 100, 100, 250, 0, 5850, 64, -11.7)
reverb_mountains = REVERB_PROPERTIES(1500, 300, 100, 5000, 21, 27, 100, 250, 0, 1220, 82, -24.0)
reverb_underwater = REVERB_PROPERTIES(1500, 7, 11, 5000, 10, 100, 100, 250, 0, 500, 92, 7.0)
reverb_forest = REVERB_PROPERTIES(1500, 162, 88, 5000, 54, 79, 100, 250, 0, 760, 94, -12.3)
reverb_arena = REVERB_PROPERTIES(7200, 20, 30, 5000, 33, 100, 100, 250, 0, 4500, 80, -9.6)
reverb_city = REVERB_PROPERTIES(1500, 7, 11, 5000, 67, 50, 100, 250, 0, 4050, 66, -26.0)
reverb_sewerpipe = REVERB_PROPERTIES(2800, 14, 21, 5000, 14, 80, 60, 250, 0, 3400, 66, 1.2)
reverb_concerthall = REVERB_PROPERTIES(3900, 20, 29, 5000, 70, 100, 100, 250, 0, 5650, 80, -9.8)