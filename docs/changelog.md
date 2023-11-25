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

/// wiki | v0.13 Alpha
|         |                                                                                                                                                                                |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added   | Golden tiles. They have a 1% chance of a x10 multiplier on all tiles. (25% discount on shop tiles)                                                                             |
|         | Button to UI to save player data to database, rather than waiting for cache to unload it.                                                                                      |
|         | Custom Twitch emotes added.                                                                                                                                                    |
| Changed | King can complete purchases in shop tiles now without leaving the throne.                                                                                                      |
|         | Win prize is now the sum of all bids made, including raffle.                                                                                                                   |
|         | [Danger Zone]: Additional points are rewarded for every round a player survives.                                                                                               |
|         | [Quip Battle]: Each vote is now worth 1/10th pf the total win prize of the tile.                                                                                               |
|         | Text size increased on point buckets.                                                                                                                                          |
|         | Players who already started participating in the game can no longer be recruited. Only players who haven't joined the current game or have been inactive for a while may work. |
|         | Removed transparency on ticket particles in effort to reduce bitrate drops on twitch.                                                                                          |
| Fixed   | Bug causing points to not save properly when application shut down with players still spawned in.                                                                              |
|         | Prize not resetting after tile change.                                                                                                                                         |
|         | Bug causing non-global emotes to not load in speech bubbles.                                                                                                                   |
|         | Blocking lag spike caused by downloading non-global emotes. Only new emotes used by broadcaster are downloaded now.                                                            |
|         | Bug causing PFPs to temporarily not load correctly afer api refresh 4 hours into stream.                                                                                       |
///

/// wiki | v0.12 Alpha
|         |                                                                                                                                                      |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added   | Epic tile [Trail Shop]: Allows spending gold on trail colors. Said colors will be random each time the tile appears.                                 |
|         | [`!givegold`][givegold-command] command to give a player some of your gold.                                                                          |
|         | [`!cancelbid`][cancelbid-command] command to cancel your current bid tickets or bits and removes you from queue. Won't refund them to you.           |
|         | [`!wiki`][wiki-command] command sharing a link to this very wiki you're reading.                                                                     |
|         | Total number of tickets spent to stats.                                                                                                              |
| Changed | Auction discs no longer turn gray when a player moves to their bidding position.                                                                     |
|         | [Quip Battle]: Messages starting with `!` are no longer read by the TTS system.                                                                      |
|         | Reduced physics timestep by 50%. Physics accuracy increased x2 (Should match Gen 2 physics now).                                                     |
| Fixed   | Lava getting stuck on invisible blocks in default defense.                                                                                           |
|         | Bug caused by longer usernames causing the twitch prediction api call to error.                                                                      |
///

/// wiki | v0.11 Alpha
|       |                                                                                 |
|-------|---------------------------------------------------------------------------------|
| Added | [Quip Battle]: New prompts.                                                     |
| Fixed | [Quip Battle]: Voices not being high-pitched.                                   |
|       | Bug causing speech bubbles to flash incorrect size one frame before growing in. |
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
|         | [`!playlist` command][playlist-command] to get a link to the spotify playlist used in the game.      |
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
