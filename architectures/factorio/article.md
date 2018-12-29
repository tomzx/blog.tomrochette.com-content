An initial seed is computed and stored in the game save file
Based on this seed, the world is pseudo randomly computed, using a certain chunk/block/tile size (e.g., 32x32, 128x128)
The world map is only generated on-demand, that is, as far as the player can see
When a new chunk is discovered, its blocks are computed and persisted in the save file
If there are no active components in a chunk that is not visible, the game will obviously not render it, it will only simulate it (position, item, velocity, etc)
Certain thing, for instance alien types and alien base size, may only be computed once they are observed. At first, maybe only a location anchor will exist to indicate where they should spawn, but the rest will be generated only when needed.
