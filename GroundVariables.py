from GroundClass import *
from SubmissionVariables import *
from GroundStrikeVariables import *
from main import gEscape

# GroundClass(self, name, rank, attacks ,advance_Position, decrease_Position, sweep, reversed_Position, opp_New_Pos, opp_Dec_Pos, submissions, time_cost, judge_score, crowd_score):

stack_guard_Offense = GroundBehavior("Stack Guard Offense", 1, [gpunch], full_Guard_Offense, gEscape, gEscape, gEscape, full_Guard_Defense, stack_guard_Defense, [armbar], 3, 2, 2 )
stack_guard_Defense = GroundBehavior("Stack Guard Defense", -5, [gpunch], gEscape, gEscape, full_Guard_Offense, full_Guard_Defense, gEscape, stack_guard_Offense, [armbar], 1, 0, 0 )
full_Guard_Offense = GroundBehavior("Full Guard Offense", 2, [gpunch], half_Guard_Offense, stack_guard_Offense, full_Guard_Offense, full_Guard_Defense, half_Guard_Defense, full_Guard_Defense, [armbar], 3, 1, 2)
full_Guard_Defense = GroundBehavior("Full Guard Defense", -1, [gpunch], gEscape, gEscape, full_Guard_Offense, full_Guard_Defense, gEscape, full_Guard_Offense, [armbar], 3, 0, 0)
half_Guard_Offense = GroundBehavior("Half Guard Offense", 3, [gpunch], side_Control_Offense, full_Guard_Offense, half_Guard_Offense, half_Guard_Defense, side_Control_Defense, half_Guard_Defense, [armbar], 4, 1, 2)
half_Guard_Defense = GroundBehavior("Half Guard Defense", -2, [gpunch], full_Guard_Defense, gEscape, half_Guard_Offense, half_Guard_Defense, full_Guard_Offense, half_Guard_Offense, [], 4, 0, 0)
side_Control_Offense = GroundBehavior("Side Control Offense", 4, [gpunch], full_Mount_Offense, gEscape, side_Control_Offense, side_Control_Defense, full_Mount_Defense, side_Control_Defense, [armbar], 3, 2, 2)
side_Control_Defense = GroundBehavior("Side Control Defense", -3, [gpunch], half_Guard_Defense, half_Guard_Defense, side_Control_Offense, side_Control_Defense, half_Guard_Offense, side_Control_Offense, [armbar], 3, 0, 0)
full_Mount_Offense = GroundBehavior("Full Mount Offense", 5, [gpunch], back_Mount_Offense, side_Control_Offense, full_Guard_Offense, full_Guard_Defense, back_Mount_Defense, full_Mount_Defense, [armbar], 4, 3, 3)
full_Mount_Defense = GroundBehavior("Full Mount Defense", -4, [gpunch], side_Control_Defense, back_Mount_Defense, full_Guard_Offense, full_Guard_Defense, side_Control_Offense, full_Mount_Offense, [], 4, 0, 0)
north_South_Offense = GroundBehavior("North South Offense", 6, [gpunch], side_Control_Offense, side_Control_Offense, north_South_Offense, north_South_Defense, side_Control_Defense, north_South_Defense, [armbar], 5, 2, 1)
north_South_Defense = GroundBehavior("North South Defense", -5, [gpunch], side_Control_Defense, back_Mount_Defense, north_South_Offense, north_South_Defense, side_Control_Offense, north_South_Offense, [], 5, 0, 0)
back_Mount_Offense = GroundBehavior("Back Mount Offense", 7, [gpunch], full_Mount_Offense, gEscape, full_Guard_Defense, north_South_Defense, full_Mount_Defense, back_Mount_Defense, [armbar], 5, 2, 2)
back_Mount_Defense = GroundBehavior("Back Mount Defense", -6, [gpunch], full_Mount_Defense, gEscape, full_Guard_Offense, full_Guard_Defense, full_Mount_Offense, back_Mount_Offense, [], 5, 0, 0)




