# LoveLocal

------------------------------------------------------------- EASY 1: LAST WORD LENGTH ---------------------------------------------------------------------------------------

Logic and algorithm :

1. Splitting input strings:

The input for the function lastword is a string s.
The split() method is used without any arguments to split the input string s into a list of words. This technique eliminates leading and trailing whitespaces and separates the string at spaces.
The list of words that is produced is kept in the variable word.

2. Look for a blank string

The function determines whether the word (word) list is empty. Cases where the input string is empty or contains only spaces are handled by this condition.
The method returns 0 if there are no words, meaning that there isn't a last word to measure.

3. Length of Return for Last Word:

The method returns the length of the last word in the list if there are any words in it. Negative indexing involves counting from the end, so to accomplish this, use words[-1] to access the last entry of the words list, and then len(words[-1]) to determine the word's length.

4. Gather User Data and Present Outcome:

Then, using input("Enter a string:"), the software requests input from the user.
Using the user's input, it calls the lastword function, storing the outcome in the response variable.
Lastly, print("Length:", response) is used to output the final word's length.

------------------------------------------------------------- MEDIUM 2: MAJORITY ELEMENTS ------------------------------------------------------------------------------------

Logic and algorithm :

1. Initialization:

person1, person2: Two potential persons for  elements. Initialized to float('inf') as placeholders.
countOne, countTwo: Counters for the respective persons, initialized to 0.

2. First Pass: Finding Potential persons:

Iterate through the array (nums).
If the current number is equal to person1, increment countOne.
If the current number is equal to person2, increment countTwo.
If countOne becomes 0, update person1 to the current number and reset countOne to 1.
If countTwo becomes 0, update person2 to the current number and reset countTwo to 1.
If none of the above conditions is met, decrement both countOne and countTwo.

3. Reset Counters:

Reset countOne and countTwo to 0.

4. Second Pass: Count Actual Occurrences:

Iterate through the array again.
Count the occurrences of person1 and person2.

5. Check for  Elements:

If the count of person1 is greater than ⌊ n/3 ⌋, add it to the result list.
If the count of person2 is greater than ⌊ n/3 ⌋, add it to the result list.

6. Return Result:

Return the list of elements.

------------------------------------------------------------- HARD 3: COUNTING DIGIT ---------------------------------------------------------------------------------------

Logic and algorithm :

Algorithm Explanation:

The algorithm uses a loop to iterate through each place value (ones, tens, hundreds, etc.) in the range from 0 to n. The variable count accumulates the total count of digit 1 in this range.

Details of the Algorithm:

Initialize count to 0, factor to 1, and i to 1.

Start a loop that continues until i becomes greater than n.

Inside the loop, calculate divider as i * 10. This divider represents the next higher place value.

Update count using the following formula:
count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
(i) (n // divider) * => This part counts the occurrences of digit 1 at the current place value for the full cycles (e.g., in the tens, hundreds, etc. places).
(ii) min(max(n % divider - i + 1, 0), i) => This part handles the remaining digits at the current place value after the full cycles. It ensures that we don't count more than the actual remaining digits.

Multiply i by 10 to move on to the next lower place value.

Repeat the loop until the entire range is covered.

Return the final count.
