# Sweeft_Algoes_Python_D
repo for "Sweeft Digital" algoes, in Python - Data Engineering



Exercise 1: ⬤
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
Constraints:
1 ≤ n ≤ 105
The sum of the lengths of all the words do not exceed 106 All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, n.
The next n lines each contain a word.
Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
Sample Input:
4 bcdef abcdefg bcde bcdef
Sample Output
3
2 1 1
Explanation
There are 3  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.



Exercise 2: ⬤
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
●       It must be greater than the original word
●       It must be the smallest word that meets the first condition
Example w = abcd
The next largest word is abdc.
Create the function bigger_Is_greater and return the new string meeting the criteria. If it is not possible, return no answer.
Function Description
Function has the following parameter(s):
    	●	string w: a word
Returns
    	- 	string: the smallest lexicographically higher string possible or no answer
Input Format
The first line of input contains T, the number of test cases. Each of the next T lines contains w.
Constraints
●   	1 ≤ T ≤ 105
●   	1 ≤ length of w ≤ 100
●   	w will contain only letters in the range ascii[a...z]

Sample Input:
5 
ab bb hefg dhck dkhc

Sample Output
ba no answer
hegf dhkc hcdk
Explanation Test case 1: ba is the only string which can be made by rearranging ab. It is greater.
Test case 2:
It is not possible to rearrange bb and get a greater string.
Test case 3: hegf is the next string greater than hefg.
Test case 4: dhkc is the next string greater than dhck. Test case 5: hcdk is the next string greater than dkhc.
Sample Input: 6 lmno dcba dcbb abdc abcd fedcbabcd
Sample Output lmon no answer no answer acbd abdc Fedcbabdc






REST URL Shortener API
URL shortening is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL. For example, the URL "https://example.com/assets/category_B/subcategory_C/Foo/" can be shortened to
"https://example.com/Foo", and the URL "https://en.wikipedia.org/wiki/URL_shortening" can be shortened to "https://w.wiki/U". Often the redirect domain name is shorter than the original one. A friendly URL may be desired for messaging technologies that limit the number of characters in a message (for example SMS), for reducing the amount of typing required if the reader is copying a URL from a print source, for making it easier for a person to remember, or for the intention of a permalink. In November 2009, the shortened links of the URL shortening service Bitly were accessed 2.1 billion times.
Other uses of URL shortening are to "beautify" a link, track clicks, or disguise the underlying address. Although disguising of the underlying address may be desired for legitimate business or personal reasons, it is open to abuse.[2] Some URL shortening service providers have found themselves on spam blocklists, because of the use of their redirect services by sites trying to bypass those very same blocklists. Some websites prevent short, redirected URLs from being posted.
Required features:
-        API to create URL with random short name (something like this url/78sda8s6d), url random name should be fixed size string and unique per url
-        API for premium clients to create URL with custom name (url/<custom>)
-        Input url validation, that it is a correct url and size must be below 250 characterAu
-        Counters - how many times the url was accessed (optional requirement)
-        Automatic deletion of urls older than 30 days (optional requirement)
