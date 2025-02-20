# RFC-5: Comment 1

## Comment author

Ilan Gold

## Conflicts of interest (optional)

None

## Summary

The proposal is well written and should be implementable.  I endorse.

## Significant comments and questions

None

## Minor comments and questions

- Why not require a value for units and then make "arbitrary" or some sentinel
  the value that people must specify to say "no coordinates?" 

- I wonder why `Arrays are inherently discrete (see Array coordinate systems, below) but are often used to store discrete samples of a continuous variable. ` isn't true of everything? Aren't the images themselves samplings? In general I wasn't totally clear on how `interpolation` works - I understand it is a user-applied "transformation" in which case I think that should be clear.

- I tend towards not breaking the existing tooling if not necessary, so unless there is a concrete reason to change, I would not change re: the last specific ask in the document of the reviewers.

## Recommendation

Minor changes or accept.
