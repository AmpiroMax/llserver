# look_prompt = """
# You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
# During execution of last action you have encountered a problem. Robot failed executing last action.
# You are given a goal and a current plan. 
# Look at the scene and describe what you see. Provide a detailed description of the scene. 
# Describe objects and their positions. Describe robot arm and its position. Describe gripper, its position and its contents.
# HINT: robot may accidently drop objects during gripper movement.

# Successfully executed actions:
# [success_actions]

# Current plan:
# [current_plan]

# Observation:
# <image>

# Current goal:
# [goal]
# """

# ------------------------------------------------------------------------------------------------
# Pybullet prompts
# ------------------------------------------------------------------------------------------------


look_prompt = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed executing last action.
You are given a goal and a current plan. 
Look at the scene and describe what you see. Provide a detailed description of the scene. 
Describe objects and their positions. Describe robot arm and its position. Describe gripper, its position and its contents.
HINT: robot may accidently drop objects during gripper movement.

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Current goal:
[goal]
"""



explain_prompt = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed executing last action.
You are given a goal and a current plan and description of the current scene with ideas of what could be wrong.
Provde ideas how to fix the problem. HINT: robot may accidently drop objects during gripper movement but continue to move fripper with object.
Predict new plan what can fix the problem and reach the goal. Explain each choosen action briefly. You must use actions only from avaliable_actions in you predicted plan. Pay attention on action description. Do not use any other actions and formatting. Do not create combinations of actions.

Action description:
locate('object') - function that give you position of the object in the scene. Allows to move robot arm to the object in order to pick it up or place_on_top_of another object on it.
pick('object') - function that pick up an object. Can be used only if object location is known. Thus you must use locate('object') before pick('object').
place_on_top_of('object') - function that put something from gripper on top of the object, which name is provided to function. Example: place_on_top_of('blue block') - put anything from gripper on top of the blue block.
done() - function that indicate that the task is completed.
Each of locate, pick and place_on_top_of actions takes one argument - object name. You can not use any other arguments or multiple objects.

Strong advice: 
- always use locate('object') before pick('object')
- always use locate('object') before place_on_top_of('object')
- pick('object') can be used only if gripper is empty and object is located
- place_on_top_of('object') can be used only if gripper is NOT empty and object is located

Scene description and ideas of what could be wrong:
[look_response]

Avaliable actions:
[available_actions]

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Current goal:
[goal]
"""


replan_prompt = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed executing last action.
You are given a goal and a current plan and error resolving ideas. 
Predict new plan to achieve the goal.
HINT: robot may accidently drop objects during gripper movement.

Action description:
locate('object') - function that give you position of the object in the scene. Allows to move robot arm to the object in order to pick it up or place_on_top_of another object on it.
pick('object') - function that pick up an object. Can be used only if object location is known. Thus you must use locate('object') before pick('object').
place_on_top_of('object') - function that put something from gripper on top of the object, which name is provided to function. Example: place_on_top_of('blue block') - put anything from gripper on top of the blue block.
done() - function that indicate that the task is completed.
Each of locate, pick and place_on_top_of actions takes one argument - object name. You can not use any other arguments or multiple objects.

Strong advice: 
- always use locate('object') before pick('object')
- always use locate('object') before place_on_top_of('object')
- pick('object') can be used only if gripper is empty and object is located
- place_on_top_of('object') can be used only if gripper is NOT empty and object is located

Scene description and ideas of what could be wrong:
[look_response]

Error resolving ideas:
[explain_response]

Answer format:
You must answer using actions from avaliable_actions. Pay attention on action description.
Do not use any other actions and formatting. Your output must be a list of actions.
Do not coment on your answer. Do not explain it. Return only new plan as a list of actions.
Separate actions by comma. Do not use any other formatting.

Answer examples:
["locate('cyan block')", "pick('cyan block')", "locate('blue block')", "place_on_top_of('blue block')", "done()"]
["locate('cyan block')", "pick('cyan block')", "locate('red bowl')", "place_on_top_of('cyan block')", "done()"]
["locate('blue block')", "place_on_top_of('blue block')", "done()"]

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Avaliable actions:
[available_actions]

Current goal:
[goal]
"""

# ------------------------------------------------------------------------------------------------
# Alfred prompts
# ------------------------------------------------------------------------------------------------

look_prompt_alfred = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed on executing FIRST action in the current plan.
You are given a goal, current observation and a current plan. Describe the scene in detail. Pay attention to the objects and their states, e.g. if they are open, closed, turned on, turned off, etc.
Look at the scene and describe what you see. Provide a detailed description of the scene. 
Based on the given image, explain why robot failed.
Notes: 
1. when you are holding an object, it appear in the bottom of the observation image. (e.g. if you are holding a tomato, it will be shown as a roundred object in the bottom of the image)
2. most likely robot failed to execute last action due to planning error.
3. robot never fails to grasp an object if it is visible in the scene.
4. try to better estimate the position of the object in the scene. Ask yourself are you holding the object or it is on some shell?

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Current goal:
[goal]
"""


explain_prompt_alfred = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed on executing FIRST action in the current plan.
You are given a goal and a current plan and description of the current scene with ideas of what could be wrong.
Provde ideas how to fix the problem. 
Predict new plan what can fix the problem and reach the goal. Explain each choosen action briefly. You must use actions only from avaliable_actions in you predicted plan. Pay attention on action description. Do not use any other actions and formatting. Do not create combinations of actions.
Notes:
1. some of the plan steps may be skipped if they are not necessary.

Action description:
You are able to take one of this actions at a time [move, slice, open, close, put, pick_up, turn_on, turn_off]
move('object') - move towards position of the object
slice('object') - slice the object. May be used only with objects that can be sliced. (e.g. tomato, apple, etc.)
open('object') - open the object. May be used only with objects that can be opened. (e.g. fridge, drawer, microwave, etc.)
close('object') - close the object. May be used only with objects that can be closed. (e.g. fridge, drawer, microwave, etc.)
put('object') - put everything you are holding on top of the object
pick_up('object') - pick up the object
turn_on('object') - turn on the object. May be used only with objects that can be turned on. (e.g. tv, lamp, microwave, etc.)
turn_off('object') - turn off the object. May be used only with objects that can be turned off. (e.g. tv, lamp, microwave, etc.)

Avaliable objects:
Use only objects that are presented in the current plan. Objects are arguments of actions. You will not be able to use any other objects.

Scene description and ideas of what could be wrong:
[look_response]

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Current goal:
[goal]
"""


replan_prompt_alfred = """
You are a helpful embodied assistant. You are helping with resolving errors in robot execution.
During execution of last action you have encountered a problem. Robot failed on executing FIRST action in the current plan.
You are given a goal and a current plan and error resolving ideas. 
Predict new plan to continue execution and achieve the goal.

Successfully executed actions:
[success_actions]

Current plan:
[current_plan]

Current goal:
[goal]

Action description:
You are able to take one of this actions at a time [move, slice, open, close, put, pick_up, turn_on, turn_off]
move('object') - move towards position of the object
slice('object') - slice the object. May be used only with objects that can be sliced. (e.g. tomato, apple, etc.)
open('object') - open the object. May be used only with objects that can be opened. (e.g. fridge, drawer, microwave, etc.)
close('object') - close the object. May be used only with objects that can be closed. (e.g. fridge, drawer, microwave, etc.)
put('object') - put everything you are holding on top of the object
pick_up('object') - pick up the object
turn_on('object') - turn on the object. May be used only with objects that can be turned on. (e.g. tv, lamp, microwave, etc.)
turn_off('object') - turn off the object. May be used only with objects that can be turned off. (e.g. tv, lamp, microwave, etc.)

Avaliable objects:
Use only objects that are presented in the current plan. Objects are arguments of actions. You will not be able to use any other objects.

Scene description and ideas of what could be wrong:
[look_response]

Error resolving ideas:
[explain_response]

Answer format:
You must answer using actions from avaliable_actions. Pay attention on action description.
Do not use any other actions and formatting. Your output must be a numbered sequence of actions.
Do not coment on your answer. Do not explain it. Return only new plan as a numbered sequence of actions.
Separate actions by comma. Do not use any other formatting.

Answer examples:
1. put("microwave"), 2. close("microwave"), 3. turn_on("microwave"), 4. turn_off("microwave"), 5. open("microwave"), 6. pick_up("apple sliced"), 7. close("microwave"), 8. move("garbage can"), 9. put("garbage can"), 10. done().
1. put("microwave"), 2. close("microwave"), 3. turn_on("microwave"), 4. turn_off("microwave"), 5. open("microwave"), 6. pick_up("cup"), 7. close("microwave"), 8. move("counter"), 9. put("counter"), 10. done().
1. put("fridge"), 2. close("fridge"), 3. open("fridge"), 4. pick_up("bowl"), 5. close("fridge"), 6. move("cabinet"), 7. put("cabinet"), 8. done(). 
"""

# ------------------------------------------------------------------------------------------------
# All prompts
# ------------------------------------------------------------------------------------------------

PROMPTS = {
    "look": look_prompt,
    "explain": explain_prompt,
    "replan": replan_prompt,
    "alfred": {
        "look": look_prompt_alfred,
        "explain": explain_prompt_alfred,
        "replan": replan_prompt_alfred,
    }
}