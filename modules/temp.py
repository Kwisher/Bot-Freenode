import sopel.module
from sopel.formatting import *

import re

@sopel.module.commands('temp')
@sopel.module.example('.temp 60F')
def temp(bot, trigger):
  """Converts given temp to opposing unit."""
  user_input = trigger.group(2)
  if not user_input:
    return bot.reply("You need to give me a temp to convert! (e.g. .temp 60F)")
  
  # Extract temp and unit from input string
  input_temp = re.findall(r'(?:-?\d{1,3} ?[fcFC])', user_input)

  if len(input_temp) == 0:
    return bot.reply("I'm expecting a number followed by a unit (e.g. .temp 60F)")

  # Find unit
  unit = ''.join(filter(str.isalpha, input_temp[0].lower()))

  # Delete unit from input_temp
  temp = input_temp[0].lower().replace(unit, '').strip()

  if unit == 'c':
    # C = 0.55 x (F-32)
    calc_temp = (1.8 * float(temp)) + 32
    # Round calculated temp to nearest whole number
    output = str(int(round(calc_temp))) + 'F'
  elif unit == 'f':
    # F = [1.8 x C] + 32
    calc_temp = 0.55 * (int(temp) - 32)
    # Round calculated temp to nearest whole number
    output = str(int(round(calc_temp))) + 'C'

  bot.say("{} is {}".format(
    input_temp[0],
    output)
  )

