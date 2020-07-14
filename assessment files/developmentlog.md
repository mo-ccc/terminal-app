#### first status report
When creating the movement function I encountered an overflow error as the view port neared the
edges of the map. I predicted this error during the planning phase of my application and
at the time I decided I would remedy the situation by making it so that the viewport would
stop moving as the character entered into the dead zones.
However while figuring out how I would implement the feature I was also debating whether
that would be confusing for the end user especially if they planned to move multiple steps at once.
Instead I decided to pad out the edges of the map with extra characters that way the dead zones
aren't reachable by the player. Upon testing I can conclude that this worked perfectly
and the implementation was much less of a headache than attempting to add new flow control statements.
