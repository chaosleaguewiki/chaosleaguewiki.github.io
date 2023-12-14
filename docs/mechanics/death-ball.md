---
description: Death Ball is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.
---

# Death Ball

**Death Ball** is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.

## How it works

Depending on the tile will a death ball already exist or be spawned after enough time has passed.

In either case will a ball with a skull displayed move inside the tile. They have the same physics applied as any normal marble.

Should a player collide with a death ball while it has spikes show will they be eliminated. After elimination of a player will the spikes disappear and the death ball cease all movement imediatally.  
It remains in this for a while, indicated by a red outline slowly filling up. During this time can it not be moved by player marbles or components of the tile it is in. In addition can players collide with it without being eliminated. Once the cooldown has passed will the spikes reappear and the ball resume movement once again.

Players eliminated by the death ball do not lose points to the king.

Should enough time pass will additional death balls be spawned. This happens around every 30 seconds as additional death balls are spawned by the 3rd multiplication of a tile's x2 multiplier.

{{ game.history({
    'v0.22 Alpha': [
        'Game mechanic added as part of [Chaos Plinko]'
    ],
    'v0.24 Alpha': [
        'Death ball added as sudden death mechanic to certain tiles.'
    ]
}) }}