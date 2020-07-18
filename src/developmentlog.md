#### first status report - 14/07/20
When creating the movement function I encountered an overflow error as the view port neared the
edges of the map. I predicted this error during the planning phase of my application and
at the time I decided I would remedy the situation by making it so that the viewport would
stop moving as the character entered into the dead zones.
However while figuring out how I would implement the feature I was also debating whether
that would be confusing for the end user especially if they planned to move multiple steps at once.
Instead I decided to pad out the edges of the map with extra characters that way the dead zones
aren't reachable by the player. Upon testing I can conclude that this worked perfectly
and the implementation was much less of a headache than attempting to add new flow control statements.

#### last status report - 15/07/20
As I wrap up my project I find that my code has become extremely messy and difficult to update. Changing one
thing results in several other things being broken forcing me to look for ways to completely rewrite
the code in a more efficient manner.
Testing the code reveals small bugs that result in exceptions being thrown however I am certain that I
will be able to iron most of the bugs. However, i've yet to use try and except clauses extensively;
Instead i've put more emphasis on preventing exceptions rather than handling them.
Based on my developmental plans my project did not end up the way I expected it to and I found myself
wanting to start over with a new more entertaining project.
Furthermore, I wasn't able to completely predict how the functions will interact each other and so there
are inconsistencies in my flow chart.
Using the os.path modules to create save documents was enjoyable and taught me how to use json and I believe
what I learned will come in handy in the future when using the pickle module to create encrypted files.
