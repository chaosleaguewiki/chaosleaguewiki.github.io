---
description: Past and current changes to the Chaos League Game
---

# Changelog

/// wip | This page needs work
If you can, contribute to this page to have it updated and improved.

**What is missing?**

- Possible Changelogs of versions between v0.3 Alpha and v0.6 Alpha
///

This page lists the recent updates for the past iterations of the Chaos League Game.

## CL 3

/// wiki | v0.11 Alpha
|         |                                                                                 |
|---------|---------------------------------------------------------------------------------|
| Added   | [Quip Battle]: New prompts.                                                     |
| Fixed   | [Quip Battle]: Voices not being high-pitched.                                   |
|         | Bug causing speech bubbles to flash incorrect size one frame before growing in. |
///

/// wiki | v0.10 Alpha
|         |                                                                                                                                                                       |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added   | Ticket option to fill Water and Lava Bucket with.                                                                                                                     |
|         | Announcement for Lava and Water Bucket activation.                                                                                                                    |
|         | SFX for lava and water bit contributions.                                                                                                                             |
|         | Button to reconnect API in settings.                                                                                                                                  |
|         | Button to refresh API token in settings.                                                                                                                              |
|         | [Quip Battle]: Error Handling and Timeout to not get stuck if reading the poll from API fails.                                                                        |
|         | Bot feedback for when a player uses the [`!lava`][lava-command] or [`!water` command][water-command] without any bits.                                                |
|         | [Zero or Hero]: Sign at the bottom to further hint that you can lose all your points.                                                                                 |
| Changed | Lava price reduced to 750 bits.                                                                                                                                       |
|         | Bot now replies with "You must hold the throne to use that command" when using the [`!left`][left-command] or [`!right`][right-command] while not holding the throne. |
|         | Speed of the [`!givepoints`][givepoints-command] traveling indicator was slowed down.                                                                                 |
| Fixed   | Bug causing the Lava and Water Bucket display to sometimes overlap with the raffle box.                                                                               |
|         | Spike crusher moving through the podium.                                                                                                                              |
|         | Bug causing [`!givepoints`][givepoints-command] to popup subtraction text twice.                                                                                      |
|         | Bug showing recruitment Profile picture icon in front of the throne holder.                                                                                           |
|         | Bug causing recruitment Profile picture icon to not load properly if the player is spawned in while recruited.                                                        |
///

/// wiki | v0.9 Alpha
|         |                                                                                                                                                                               |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added   | Common tile [Zero or Hero].                                                                                                                                                   |
|         | Lava release Bucket added. Used with [`!lava [bits]`][lava-command] to fill a progress bar. Once full releases a bucket of lava. Players killed by it lose half their points. |
|         | Water release Bucket. Extinguishes lava. Used with [`!water [bits]`][water-command] to fill a progress bar. Once full releases a bucket of water extinguishing lava.          |
|         | Animation to king tile fluid buckets to rotate oppossite from bidding queue.                                                                                                  |
| Changed | [Bounce House]: Gap increases own value by 5 every time a player passes through.                                                                                              |
|         | [Bounce House]: Spinning block is now 1 point and increases by 1 every time a player hits it.                                                                                 |
|         | [Royal Execution]: Timer is now 30 seconds.                                                                                                                                   |
|         | Multiple TTS messages at once are now possible. Announcements are still queued.                                                                                               |
| Fixed   | Twitch Access API Token refresh bug causing connection to duplicate after 4 hours refresh.                                                                                    |
|         | Bug causing points displayed on player in podium to not match the player's actual points.                                                                                     |
///

/// wiki | v0.8 Alpha
|         |                                                                                                                  |
|---------|------------------------------------------------------------------------------------------------------------------|
| Added   | Rare tile [Royal Execution].                                                                                     |
|         | Gold. Earned by the King every 15 seconds and when throne is captured. Value earned is equal to current viewers. |
|         | [`!stats` command][stats-command] now displays Gold too.                                                         |
| Changed | Refactored game tile prefab variants (backend improvements).                                                     |
| Fixed   | Bug causing player Marbles to get stuck in raffle when trying to attack the king.                                |
|         | Speech bubbles rendering behind player Marbles in certain situations.                                            |
|         | Bug causing new sub to not grant 5k bid bonus.                                                                   |
///

/// wiki | v0.7 Alpha
|         |                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------|
| Added   | Bidding while your Marble is spawned automatically queues you for the next time after elimination.   |
|         | [`!playlist` command][playlist-command]                                                              |
|         | Bid Bonus for subs and gifted subs, multiplied by tier.                                              |
| Changed | Moved player names above marbles on z-layer to not be obscured by each other.                        |
|         | [Stonks]: Tile survival rate got buffed.                                                             |
| Fixed   | Player moveing and positioning in queue got refactored.                                              |
|         | Bug causing tickets to not always impact correct position.                                           |
|         | Bug causing Arrows to flash for one frame after reuse.                                               |
|         | Text is now sanitized to prevent players from changing color and size of the text in speech bubbles. |
///

/// wiki | v0.6 Alpha
|         |                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------|
| Added   | Rare tile [Stonks].                                                                                            |
| Changed | [Hole in One]: Gaps at the edges got closed and now eliminate the player while transfering 100 points to King. |
///

/// wiki | v0.3 Alpha
|       |                             |
|-------|-----------------------------|
| Added | Common tile [Bounce House]. |
///

/// wiki | v0.1 Alpha
|       |                                   |
|-------|-----------------------------------|
| Added | Common tile [Danger Zone].        |
|       | Common tile [How Low Can You Go]. |
|       | Common tile [Quip Battle].        |
|       | Legendary tile [Hole In One].     |
///

<!-- other links -->
[playlist-command]: chat-commands/twitch.md#playlist
[stats-command]: chat-commands/twitch.md#stats-user
[lava-command]: chat-commands/twitch.md#lava-bits
[water-command]: chat-commands/twitch.md#water-bits
[left-command]: chat-commands/twitch.md#left
[right-command]: chat-commands/twitch.md#right
[givepoints-command]: chat-commands/twitch.md#givepoints-amount-user

<!-- minigame links -->
[Bounce House]: twitch-minigames/common/bounce-house.md
[Danger Zone]: twitch-minigames/common/danger-zone.md
[How Low Can You Go]: twitch-minigames/common/how-low-can-you-go.md
[Quip Battle]: twitch-minigames/common/quip-battle.md
[Zero or Hero]: twitch-minigames/common/zero-or-hero.md

[Stonks]: twitch-minigames/rare/stonks.md
[Royal Execution]: twitch-minigames/rare/royal-execution.md

[Hole In One]: twitch-minigames/legendary/hole-in-one.md
