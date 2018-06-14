# 0. Project Overview 
![alt text](https://cdn-images-1.medium.com/max/1191/0*vbw4wQW_Xq2_3eOo.jpg "Logo Title Text 1")  
## 0.1 What is DOTA?  
[DOTA](https://en.wikipedia.org/wiki/Dota_2) is an online multiplayer game which stands for Defense of the Ancients. The game is developped and published by valve and represents the second iteration of its kind. Originally, the game was developped by someone with the alias: "[IceFrog](https://dota2.gamepedia.com/IceFrog)" who published DOTA through a community-created mod using the Warcraft III engine.  

The game is played 5 vs. 5 on the same map every game. Each team must occupy and defend their own bases where resides 'the ancient'. The game ends when one team successfully destroys the ancient. Each player must independently control a powerful character also known as a hero. Each hero has a unique style of play and possesses on average 4 unique abilities. Throughout the gameplay, heros can accumulate gold and experience through combat versus the other team's heros, killing enemy creeps (NPC), or destroying enemy towers/structures.  

This game is regarded as having one of the steepest learning curves by the gaming community. Losing is extremely frustrating while winning feels extremely rewarding.  

## 0.2 Some DOTA History  
The game may seem simple at first glance due to each hero having access to only 4 skills, however the game is deceptively deep. The team composition permutations seem unumerable and every game is different from a previous one. Players with over 3000 hours of game time are still considered "Noobs" by the community.  

In 2017, Elon Musk assembled a team to create an AI capable of playing DOTA 2 matches known as [OpenAI](https://blog.openai.com/dota-2/). This AI was only designed to participate in 1 vs. 1 player matches in the "mid lane". This bot learned to play the hero known as "Nevermore" or by its title "ShadowFiend" and had the opportunity to demonstrate its skills against one of the best mid players in the world: [Dendi](https://liquipedia.net/dota2/Dendi). Needless to say, OpenAI crushed Dendi which resonated throughout the gaming community.  

Despite this victory, OpenAI is a very long way from learning to play 5 vs. 5 as it would have to learn every hero individually as well as team coordination strategies where the possibilities are seemingly endless.  


## 0.3 DOTA Trivia  
1. DOTA 2 generates \$18m per month
2. DOTA 2 holds the record for the largest prize pool in any e-sports at $24,687,919.00

## 0.4 Why DOTA?  
As mentioned in section 0.2, the game is quite complex during the play phase but this complexity is driven by the drafting phase. Before entering a game, players are presented at the hero selection screen where they can assemble a team of heroes with the goal of building as much synergy as possible. Certain teams favor pushing towers early in the game while other teams play for longevity thus giving the time and ressources for their heroes to become stronger. Regardless of a team's composition, the drafting phase will set the pace for the match.  

Drafting is known to be an art in the DOTA community since it is so difficult to execute correctly. Many games can be won or lost from this game phase.  

This research aims to find statistical evidence which will suggest to players which hero they should play/draft in order to maximize chances at victory.  

## 0.5 Questions
1. Is it possible to predict which team will win by the end of the drafting phase?

## 0.6 Hypothesis & Expectations
1. The margin by which a team wins does not matters. 
2. With only 10 000 matches there are a maximum of 100 000 unique players which is a lot of data to process for a notebook but not sufficient for a full research.
3. Players have a match making rating thus regrouping players of similar skills into the same matches. Despite some players climbing up or down the ladder to have their MMR reflect their skills, I assume that most players are ranked appropriately. This is important because we don't want ace/smurf players to skew the results by playing well with bad team compositions.
