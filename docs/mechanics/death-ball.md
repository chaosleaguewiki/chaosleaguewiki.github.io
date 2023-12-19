---
description: Death Ball is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.
---

# Death Ball

**Death Ball** is a Game mechanic where a ball moves around a tile and eliminates marbles, should they touch its spikes.

## How it works

Depending on the tile, a death ball will already exist or will be spawned after enough time has passed.

In either case, a ball with a skull displayed will move inside the tile. They have the same physics applied as any normal marble.

If a player collides with a death ball while it has spikes shown, they will be eliminated. After elimination of a player, the spikes will disappear and the death ball will cease all movement immediately.  
It remains in this state for a while, indicated by a red outline slowly filling up. During this time, it cannot be moved by player marbles or components of the tile it is in. In addition, players can collide with it without being eliminated. Once the cooldown has passed, the spikes will reappear and the ball will resume movement once again.

Players eliminated by the death ball do not lose points to the king.

After a certain amount of time has passed, additional death balls will be spawned. This happens around every 30 seconds as additional death balls are spawned by the 3rd multiplication of a tile's x2 multiplier.

{{ game.history({
    'v0.22 Alpha': [
        'Game mechanic added as part of [Chaos Plinko]'
    ],
    'v0.24 Alpha': [
        'Death ball added as sudden death mechanic to certain tiles'
    ]
}) }}