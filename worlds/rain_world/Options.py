from Options import Toggle, Range, Choice, Option
import typing

class NumberOfChallenges(Range):
    """Sets the number of challenges to be completed"""
    display_name = "Number of challenges"
    range_start = 5
    range_end = 20
    default = 10


# class FinalBossHP(Range):
#     """Sets the HP of the final boss"""
#     display_name = "Final Boss HP"
#     range_start = 100
#     range_end = 10000
#     default = 2000

# class FixXYZGlitch(Toggle):
#     """Fixes ABC when you do XYZ"""
#     display_name = "Fix XYZ Glitch"

# By convention we call the options dict variable `<world>_options`.
mygame_options: typing.Dict[str, AssembleOptions] = {
    "challenge_count": NumberOfChallenges
}