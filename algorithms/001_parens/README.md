# Problem


First we started with the following problem:
Given a string with parentheses, find the index of starting parens and their matching ending parens.

[Matching Closing Parens](https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/matchingClosingParenthesis/matchingClosingParenthesis.md)

Output could be something like: [(3, 58), (12, 57), (24, 45)] with pairs of indices.


Here is a simpler version of a simpler version of a similar problem:

Given a string with parentheses in it, tell me whether, for every opening parens, there is a corresponding parens.  In otherwords, are the parens correct in the given string?

((cat)) # true
()(() # false
)()( # false
()((()) # true


