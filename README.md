
# De Dup Engine

It is an engine which will suggest if any duplicate data is present in 
our database and if it possible to track atleast the top 5 matched records
from our database. If the data is unique then it is stored in the original
database else a suggestion is given with the closest dataset.


## Optimizations

Initially we have tried implementing using the fuzzywuzzy library which 
turned out to be slower than usual. So we are working on the levenstein distance
along with numpy and panda library for making it faster.
## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

**Database:** CSV File

**Web Framework:** Django
  