---
description: Chaos League allows you to recruit others, which makes you earn points through their wins.
---

# Recruiting

One Game mechanic available in Chaos League is recruiting.

Recruiting allows a player to share a link others can use to *join* their team. Joining the recruiting player will result in 50% of all points the player earns to also be given to the recruiting player. This means that if a recruited player earns 100 points, the player that recruited them will receive 50 points.  
These points are not removed from the recruited player's score.

## How to recruit

To recruit, a player can execute the [`!recruit` command](../chat-commands/twitch.md#recruit) in the stream chat. This will give them a URL that they can share with others.  
A URL is in the format `https://www.chaos-league.com/@:username` with `:username` being the handle of the player that recruits others.

This link when opened will prompt the player to authenticate with their streaming account.  
Once completed, the recruitment will be announced in the stream.

A player's alliance with another player will be indicated by a small avatar of the recruiter next to the player's Marble.

A recruiter can have multiple recruits.

## Requirements

In order for a player to be recruited, they need to not be active in the stream for a certain time. Additionally, they can only join one player per stream.  
If they try joining another player while already being recruited or being considered active by the game, the recruiting will fail.

{{ game.history({
    'v0.1 Alpha': [
        'Gameplay mechanic added'
    ]
}) }}