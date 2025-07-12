# main.py - The Last Light RPG

import random
import time

class Player:
   def __init__(self, name):
       self.name = name
       self.hp = 100
       self.max_hp = 100
       self.level = 1
       self.exp = 0
       self.gold = 10
       self.inventory = []
       self.karma = 0  # Tracks moral choices
       self.relationships = {}  # NPC relationships
       self.memories = []  # Story memories
       self.sanity = 100  # Mental state
       self.hope = 50  # World's hope level
       self.days_survived = 0

   def stats(self):
       return (f"{self.name} | HP:{self.hp}/{self.max_hp} | Level:{self.level} | "
               f"EXP:{self.exp} | Gold:{self.gold} | Karma:{self.karma} | "
               f"Sanity:{self.sanity} | Hope:{self.hope} | Days:{self.days_survived}\n"
               f"Inventory: {', '.join(self.inventory) or 'Empty'}")

   def add_memory(self, memory):
       self.memories.append(memory)
       print(f"[Memory added: {memory}]")

   def change_hope(self, amount):
       self.hope = max(0, min(100, self.hope + amount))
       if amount > 0:
           print(f"The world feels a little brighter... (Hope +{amount})")
       else:
           print(f"Darkness spreads... (Hope {amount})")

   def add_loot(self, item):
       self.inventory.append(item)
       print(f"You found: {item}")

class NPC:
   def __init__(self, name, story, alive=True):
       self.name = name
       self.story = story
       self.alive = alive
       self.trust = 0

def slow_print(text, delay=0.03):
   for char in text:
       print(char, end='', flush=True)
       time.sleep(delay)
   print()

def battle(player):
   enemies = [
       ("Hollow Survivor", "A person who lost everything, now consumed by rage"),
       ("Shadow of Regret", "Your past mistakes given form"),
       ("Despair Wraith", "The embodiment of hopelessness"),
       ("Corrupted Guardian", "A protector who failed and turned dark")
   ]
   
   enemy_name, enemy_desc = random.choice(enemies)
   enemy_hp = random.randint(30, 60)
   
   slow_print(f"\n{enemy_desc}")
   slow_print(f"The {enemy_name} emerges from the shadows... HP: {enemy_hp}")
   
   while enemy_hp > 0 and player.hp > 0:
       print(f"\nYour HP: {player.hp} | Enemy HP: {enemy_hp}")
       action = input("Fight, Mercy, or Flee? > ").strip().lower()
       
       if action == "fight":
           dmg = random.randint(15, 25)
           enemy_hp -= dmg
           slow_print(f"You strike with desperate fury! {dmg} damage!")
           
           if enemy_hp > 0:
               enemy_dmg = random.randint(10, 20)
               player.hp -= enemy_dmg
               player.sanity -= 2
               slow_print(f"The {enemy_name} claws at your soul! {enemy_dmg} damage!")
               
       elif action == "mercy":
           if random.random() < 0.3:
               slow_print(f"Your compassion reaches through the darkness...")
               slow_print(f"The {enemy_name} remembers what they once were and fades peacefully.")
               player.karma += 10
               player.change_hope(5)
               player.add_memory(f"Showed mercy to {enemy_name}")
               return
           else:
               slow_print("Your mercy is rejected! The enemy attacks with renewed fury!")
               enemy_dmg = random.randint(15, 25)
               player.hp -= enemy_dmg
               player.sanity -= 5
               
       elif action == "flee":
           slow_print("You escape into the darkness...")
           player.sanity -= 5
           return
       else:
           slow_print("In your panic, you hesitate...")
           
   if player.hp > 0:
       slow_print(f"The {enemy_name} falls... but victory feels hollow.")
       gained = random.randint(10, 20)
       player.exp += gained
       player.gold += random.randint(3, 8)
       player.karma -= 2  # Violence has consequences
       slow_print(f"Gained {gained} EXP. Your soul feels heavier.")
       
       if random.random() < 0.4:
           player.add_loot("Bitter Memory")
           
       level_up(player)
   else:
       slow_print("\nDarkness consumes you...")
       game_over(player)

def explore(player):
   player.days_survived += 1
   
   locations = [
       ("abandoned_school", "You find an abandoned school, children's drawings still on the walls..."),
       ("broken_bridge", "A bridge spans a chasm. Someone is calling for help from below..."),
       ("dying_tree", "An ancient tree withers. A small girl sits beneath it, crying..."),
       ("refugee_camp", "Desperate people huddle around dying fires..."),
       ("memory_shrine", "A shrine to the lost. Fresh flowers suggest someone still cares...")
   ]
   
   location, description = random.choice(locations)
   slow_print(f"\n{description}")
   
   if location == "abandoned_school":
       choice = input("Search the school or Leave respectfully? > ").strip().lower()
       if choice == "search":
           if random.random() < 0.5:
               slow_print("You find a child's diary. The last entry: 'I hope someone remembers us.'")
               player.add_memory("Found a child's final hope")
               player.change_hope(10)
           else:
               slow_print("You find nothing but echoes of laughter that will never return.")
               player.sanity -= 10
       else:
           slow_print("You whisper a prayer and move on. Some places deserve peace.")
           player.karma += 5
           
   elif location == "broken_bridge":
       choice = input("Try to help or Keep walking? > ").strip().lower()
       if choice == "help" or choice == "try to help":
           if random.random() < 0.6:
               slow_print("You risk everything to save them. They're just a child, lost and alone.")
               slow_print("'Thank you,' they whisper. 'I thought no one cared anymore.'")
               player.add_memory("Saved a child from the chasm")
               player.change_hope(15)
               player.karma += 15
               player.sanity += 10
           else:
               slow_print("You try to help, but the rope breaks. You watch them fall...")
               slow_print("Their final scream echoes in your mind forever.")
               player.sanity -= 25
               player.karma -= 10
               player.add_memory("Failed to save someone")
       else:
           slow_print("You walk away. Their cries follow you into the night.")
           player.sanity -= 15
           player.karma -= 5
           
   elif location == "dying_tree":
       choice = input("Approach the girl or Observe from distance? > ").strip().lower()
       if choice == "approach":
           slow_print("'My grandmother planted this tree,' she says without looking up.")
           slow_print("'She said it would outlive us all. She was wrong.'")
           comfort_choice = input("Comfort her or Share your food? > ").strip().lower()
           if comfort_choice == "comfort":
               slow_print("You sit beside her. Sometimes presence is enough.")
               player.sanity += 5
               player.karma += 5
           elif comfort_choice == "share" or "food" in comfort_choice:
               if "Bread" in player.inventory:
                   player.inventory.remove("Bread")
                   slow_print("You share your bread. She smiles for the first time in months.")
                   player.change_hope(10)
                   player.karma += 10
               else:
                   slow_print("You have no food to share. The guilt cuts deep.")
                   player.sanity -= 5
                   
   elif location == "refugee_camp":
       slow_print("Hollow eyes stare at you. They've lost everything.")
       if player.gold >= 20:
           choice = input("Share your gold or Keep walking? > ").strip().lower()
           if choice == "share":
               player.gold -= 20
               slow_print("Your gold feeds them for one more day. It's not much, but it's hope.")
               player.change_hope(10)
               player.karma += 10
       else:
           slow_print("You have nothing to give. Your empty hands feel like betrayal.")
           player.sanity -= 10
           
   elif location == "memory_shrine":
       slow_print("Names of the lost are carved in stone. So many names...")
       choice = input("Add a name or Leave an offering? > ").strip().lower()
       if choice == "add":
           name = input("Whose name do you carve? > ").strip()
           slow_print(f"You carve '{name}' into the stone. They will not be forgotten.")
           player.add_memory(f"Honored {name} at the shrine")
           player.change_hope(5)
       elif choice == "leave" or choice == "offering":
           if player.inventory:
               item = random.choice(player.inventory)
               player.inventory.remove(item)
               slow_print(f"You leave your {item}. The dead deserve remembrance.")
               player.karma += 5

def meet_npc(player):
   npcs = [
       ("Elena", "A doctor who still treats the wounded, though medicine is scarce"),
       ("Marcus", "A father searching for his lost daughter"),
       ("The Chronicler", "An old man who records the stories of the lost"),
       ("Anna", "A young woman who maintains the last garden in the wasteland")
   ]
   
   name, description = random.choice(npcs)
   
   if name not in player.relationships:
       player.relationships[name] = 0
       slow_print(f"\nYou meet {name}.")
       slow_print(description)
       
       if name == "Elena":
           slow_print("'I've seen too much death,' she says. 'But I keep trying to heal.'")
           choice = input("Offer to help or Ask for healing? > ").strip().lower()
           if choice == "help":
               slow_print("You spend the day helping her tend to the wounded.")
               player.relationships[name] += 10
               player.karma += 10
               player.change_hope(5)
               slow_print("Elena smiles sadly. 'Thank you. I'd forgotten what kindness looked like.'")
           else:
               if player.hp < player.max_hp:
                   player.hp = min(player.max_hp, player.hp + 20)
                   slow_print("Elena tends to your wounds without asking for payment.")
                   player.relationships[name] += 5
                   
       elif name == "Marcus":
           slow_print("'Have you seen a little girl? Brown hair, blue dress? She's all I have left.'")
           choice = input("Promise to look or Offer comfort? > ").strip().lower()
           if choice == "promise":
               slow_print("'Thank you,' he weeps. 'I won't give up. I can't give up.'")
               player.add_memory("Promised to help Marcus find his daughter")
               player.relationships[name] += 15
               player.karma += 10
               
       elif name == "The Chronicler":
           slow_print("'Stories are all we have left,' he says. 'They're how we remember who we were.'")
           choice = input("Share your story or Listen to his? > ").strip().lower()
           if choice == "share":
               slow_print("You tell him of your journey. He writes it down with shaking hands.")
               player.add_memory("Shared your story with the Chronicler")
               player.sanity += 10
               player.relationships[name] += 10
               
       elif name == "Anna":
           slow_print("'These flowers remember the world before,' she says, tending to wilted blooms.")
           choice = input("Help with the garden or Ask about the past? > ").strip().lower()
           if choice == "help":
               slow_print("You work together in silence. New shoots push through the ash.")
               player.change_hope(10)
               player.relationships[name] += 10
               player.sanity += 5

def critical_choice(player):
   slow_print("\n" + "="*50)
   slow_print("A MOMENT OF TRUTH")
   slow_print("="*50)
   
   slow_print("You find a group of starving children guarding a cache of food.")
   slow_print("They're armed with broken glass and desperation.")
   slow_print("You could easily take the food... but they would starve.")
   
   print("\nWhat defines you in this moment?")
   choice = input("Take the food, Share your supplies, or Walk away? > ").strip().lower()
   
   if choice == "take":
       slow_print("You take the food. The children scatter like frightened birds.")
       slow_print("You eat well tonight, but their faces haunt your dreams.")
       player.gold += 10
       player.sanity -= 30
       player.karma -= 25
       player.change_hope(-15)
       player.add_memory("Took food from starving children")
       
   elif choice == "share":
       slow_print("You empty your pack, sharing everything you have.")
       slow_print("The children stare in disbelief. 'Why?' one asks.")
       slow_print("'Because someone has to care,' you reply.")
       player.inventory = []
       player.gold = max(0, player.gold - 10)
       player.karma += 25
       player.change_hope(20)
       player.sanity += 15
       player.add_memory("Shared everything with starving children")
       
   else:
       slow_print("You walk away. Sometimes the right choice is the hardest.")
       player.sanity -= 10
       player.karma += 5

def game_over(player):
   slow_print("\n" + "="*50)
   slow_print("YOUR JOURNEY ENDS")
   slow_print("="*50)
   
   slow_print(f"You survived {player.days_survived} days in this broken world.")
   slow_print(f"Your final karma: {player.karma}")
   slow_print(f"The world's hope when you left: {player.hope}")
   
   if player.karma > 50:
       slow_print("\nYou died as you lived - with compassion.")
       slow_print("The people you helped remember your name.")
       slow_print("In the darkness, you were a light.")
   elif player.karma > 0:
       slow_print("\nYou tried to do good in an impossible world.")
       slow_print("It wasn't always enough, but you tried.")
   else:
       slow_print("\nThe world broke you, as it broke so many others.")
       slow_print("In trying to survive, you lost what made you human.")
   
   slow_print("\nYour memories:")
   for memory in player.memories:
       slow_print(f"- {memory}")
   
   slow_print(f"\nFinal Hope Level: {player.hope}/100")
   if player.hope > 70:
       slow_print("Against all odds, hope survived. The world might heal.")
   elif player.hope > 30:
       slow_print("A flicker of hope remains. Perhaps it's enough.")
   else:
       slow_print("Hope is nearly dead. The world grows darker.")
   
   exit()

def level_up(player):
   required_exp = player.level * 30
   if player.exp >= required_exp:
       player.level += 1
       player.max_hp += 15
       player.hp = player.max_hp
       player.exp = 0
       slow_print(f"\nYou've grown stronger... Level {player.level}")
       slow_print(f"Max HP increased to {player.max_hp}.")
       slow_print("But strength alone won't save this world.")

def main():
   slow_print("="*50)
   slow_print("THE LAST LIGHT")
   slow_print("="*50)
   slow_print("The world ended not with fire, but with the slow death of hope.")
   slow_print("You are one of the few who still remember what it means to be human.")
   slow_print("In this broken world, every choice matters.")
   slow_print("Every life you touch changes the fate of what remains.")
   
   name = input("\nWhat do they call you, wanderer? > ").strip()
   player = Player(name)
   
   slow_print(f"\nWelcome to the wasteland, {player.name}.")
   slow_print("Your choices will determine not just your fate, but the fate of hope itself.")
   
   # Starting items
   player.inventory = ["Bread", "Water", "Faded Photo"]
   player.add_memory("Left the safety of the vault")
   
   while True:
       if player.hp <= 0:
           game_over(player)
           
       if player.sanity <= 0:
           slow_print("You lose yourself to madness...")
           game_over(player)
           
       if player.days_survived >= 100:
           slow_print("You've survived 100 days. The world is changing because of you.")
           game_over(player)
           
       print("\n" + "="*50)
       print(f"Day {player.days_survived + 1}")
       print("="*50)
       
       # Random events
       if random.random() < 0.3:
           meet_npc(player)
       elif random.random() < 0.2:
           critical_choice(player)
       
       print("\nWhat do you do?")
       print("Options: stats, wander, rest, remember, inventory, meditate, quit")
       cmd = input("> ").strip().lower()
       
       if cmd == "stats":
           print(player.stats())
           
       elif cmd == "wander":
           if random.random() < 0.6:
               explore(player)
           else:
               battle(player)
               
       elif cmd == "rest":
           if "Shelter" in player.inventory:
               player.hp = min(player.max_hp, player.hp + 20)
               player.sanity += 10
               slow_print("You rest safely. Tomorrow brings new challenges.")
           else:
               player.hp = min(player.max_hp, player.hp + 10)
               player.sanity -= 5
               slow_print("You rest fitfully in the open. The cold seeps into your bones.")
               
       elif cmd == "remember":
           if player.memories:
               slow_print("You remember...")
               for memory in player.memories:
                   slow_print(f"- {memory}")
               player.sanity += 5
           else:
               slow_print("Your memories are still being written.")
               
       elif cmd == "inventory":
           print(f"You carry: {', '.join(player.inventory) or 'Nothing but hope'}")
           
       elif cmd == "meditate":
           slow_print("You sit in silence, remembering who you were before the world ended.")
           player.sanity += 10
           player.hp = min(player.max_hp, player.hp + 5)
           
       elif cmd == "quit":
           slow_print("Even in quitting, you make a choice.")
           slow_print("The world will remember what you did here.")
           break
           
       else:
           slow_print("In confusion, you hesitate. Time passes.")
           
       # Sanity and hope decay over time
       if random.random() < 0.1:
           player.sanity -= 1
           player.change_hope(-1)

if __name__ == "__main__":
   main()
