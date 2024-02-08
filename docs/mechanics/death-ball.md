---
description: Death Ball is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.
---

# Death Ball

**Death Ball** is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.

## How it works

A death ball may either exist already, such as in [Chaos Plinko], or may be spawned from a [points multiplier](points-multiplier.md) after a while.

They behave similar to a normal marble in terms of physics and tile interactions, but does not earn or lose any points.

The marble has a Skull shown while also displaying red spikes on its outside. Should a player marble collide with the death ball while the spikes are shown, will the marble be eliminated.  
Once a player got eliminated will the death ball ceise all movement and lose its spikes. A red outline will slowly do a full resolution around the death ball, indicating a cooldown. Touching the death ball during this cooldown will not cause the player to be eliminated. Once the cooldown ellapses will the spikes re-appear and the death ball move again, while also being able again to eliminate players.

The usual cooldown for a death ball is 10 seconds. Exception to this rule is [Combo Breaker], where the cooldown of the death ball is significantly shorter.

{{ game.history({
    'v0.22 Alpha': [
        'Game mechanic added as part of [Chaos Plinko]'
    ],
    'v0.24 Alpha': [
        'Death ball added as sudden death mechanic to certain tiles'
    ]
}) }}