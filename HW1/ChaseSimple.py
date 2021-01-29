#!/usr/bin/env python3

# import libraries
import random
import time

# Initiating variables 
imp_spd = (2,5)
golem_spd = (3,5)
head_start = 3
exit_position = 30

def move(steps):
  """ Move function randomly select number of steps for player and accepts one argument:
      step - the range how many steps the player can step ahead """
  return random.randint(*steps)


def chase_simple(imp_spd, golem_spd, head_start,exit_position):
  """ ChaseSimple function plays game for imp and golem and accepts 4 arguments:
        - iimp_spd: A two-element tuple where element 1 is the min # feet per second
                    and element 2 is the max # for the imp (instead of the static
                    1 and 7, respectively).
        - golem_spd: A two-element tuple identical to impSpd, but gives the golem’s
                     movement in feet per second
        - head_start: a single integer indicating the initial position of the imp in feet,
                      can not be less then 1. 
        - exit_position: A single integer indicating the foot at which the exit appears
  """ 

  # Imp's name
  imp = 'I' 
  # Golem's name
  golem = 'G'
  # Golem's initial position
  golem_position = 0 
  # Sleep time between each game 
  sleep_time = 1
  # Total number of games
  count = 0

  # Check that imp postion is between 0 and exit_position
  if head_start not in range(1,exit_position + 1):
    print(f'ERROR: Emp position should be between 1 and {exit_position}')
    return False

  # Check that imp_spd and golem_spd are tuple with length 2. 
  for element in imp_spd, golem_spd:
    if not isinstance(element, tuple) or len(element) != 2:
      print(f'ERROR: imp_spd/golem_spd should be tuple and contain 2 digits')
      return False
  
  # Check that exit_position is a digt and it should be greater then imp's or golem's
  # initial position

  if not isinstance(exit_position, int) or exit_position <= head_start:
    print(f'ERROR: exit_position can only be an integer and not less or equal head_start: {head_start}')
    return False

  # Play till imp reaches the end of the tunnel
  while head_start <= exit_position:
    # # Initiate the tunnel
    # tunnel = ['-'] * exit_position + ['X ']

    # Check if it is an inital position
    if count != 0:
      head_start += move(imp_spd)
      golem_position += move(golem_spd)

    if head_start > golem_position and head_start <= exit_position\
       and golem_position <= exit_position:
      # tunnel[head_start] = imp
      # tunnel[golem_position] = golem
      # print(*tunnel, count, 's', sep='')
      count += 1
      time.sleep(sleep_time)
    elif golem_position >= head_start:
      # Golem reaches Imp
      return False
    else:
      # Imp successfully escaped 
      return True


if __name__ == "__main__":
  if chase_simple(imp_spd, golem_spd, head_start, exit_position):
    print(f'THE IMP HAS ESCAPED TO FREEDOM. MISCHIEF AND TRICKERY AWAIT!')
  else:
    print(f'SADLY, IT’S BACK TO THE TOWER FOR THE IMP.')

