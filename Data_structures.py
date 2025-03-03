#HOW DO TEST CASES WORK

'''The prooblem is to write a progrram to  find the positon of given numbers in a 
list of numbers arranged in decreasing order.We also need to minimize the number of
times we access elements from a list '''

#input, card = the list  of numbers, query = a number whose position in  the aarray to be determined
#output = Postion  of the query in the array to  be determined.

#this is a linea function  with the O(n) solution, but this code isnt efficirnt enough
#signature function  
def locate_cards(cards, query):

    #create a function with  the value 0
    position = 0

    while position < len(cards):

        if cards[position] == query:
            return position
        
        position += 1

    return -1

#test cases
def run_test_cases():
    tests= []

    #query occurs in the middle
    tests.append({
        'input' : {
            'cards' : [13,11,10,7,4,3,1,0],
            'query' : 1
        },
        'output' : 6
    })

    #Query occurs in the first position
    tests.append({
        'input' : {
            'cards' : [4,2,1,-1],
            'query': 4
        },
        'output' : 0
    })

    #query occurs in the last position
    tests.append({
        'input' : {
            'cards' : [3,-1,-9, -127],
            'query': -127
        },
        'output' : 3
    })

    #query contains only one element
    tests.append({
        'input' : {
            'cards' : [6],
            'query': 6
        },
        'output' : 0
    })

    #query does not contain query
    tests.append({
        'input' : {
            'cards' : [9,7,5,2,-9],
            'query':4
        },
        'output' : -1
    })

    # cards is empty
    tests.append({
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    })
# numbers can repeat in cards
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    })

    for i, tests in enumerate(tests):
        input_data = tests['input']
        expected_output = tests['output']
        result = locate_cards(input_data['cards'],  input_data['query'])

        if result == expected_output:
            print(f'Test, {i + 1} passed1')
        else:
            print(f'Test {i + 1}  failed: Expected {expected_output},  but got {result}')

if __name__ == "__main__":
    run_test_cases()


#we can choose to use the binary search technique
class BinarySearch:
    def __init__(self, cards):
        self.cards = cards

    def search(self, query):
        left, right = 0, len(self.cards) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.cards[mid] == query:
                return mid
            elif self.cards[mid] > query:  # Since it's sorted in decreasing order
                right = mid - 1
            else:
                left = mid + 1
        return -1

def run_test_cases():
    tests = [
        {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
        {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
        {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
        {'input': {'cards': [6], 'query': 6}, 'output': 0},
        {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
        {'input': {'cards': [], 'query': 7}, 'output': -1},
        {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    ]

    for i, test in enumerate(tests):
        searcher = BinarySearch(test['input']['cards'])
        result = searcher.search(test['input']['query'])
        expected = test['output']
        
        if result == expected:
            print(f"Test {i + 1} passed!")
        else:
            print(f"Test {i + 1} failed: Expected {expected}, but got {result}")

if __name__ == "__main__":
    run_test_cases()

    Monthly_income = [2200,2350,2600,2130,2190]

    #In feb how many dollars did you spend extra compared to January?
    print("Much extra comparrd to Jan", Monthly_income[1]-Monthly_income[0])

    #Total expense in the first quarter of the year
    print("Totals: ", Monthly_income[0] + Monthly_income[1] + Monthly_income[2] + Monthly_income[3])

    #Find out if you spent exactly 2000 dollars in any month
    if 2000 in Monthly_income:
        print(2000)
    else:
        print('2000 is not in  Monthly income')
        print('Did I spend 20000 in any month?', 2000 in Monthly_income)

    #Total expense after June
    Monthly_income.append(1980)
    print("Expenses at the end of june",Monthly_income[0] + Monthly_income[1] + Monthly_income[2] + Monthly_income[3],Monthly_income[4] + Monthly_income[5])
    Total_sum =  sum(Monthly_income)
    print(Total_sum)

    #You returnd an  item iin june and got a refund of 200, makethe changes.
    Monthly_income[4] -= 200
    print("Monthly income after necessary chnages:",Total_sum - 200  )

    Total_Sum_After_Changes =  sum(Monthly_income)

    #Using 