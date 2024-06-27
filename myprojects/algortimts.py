# def nums():
    
#     nums1 = [4,9,5]
#     nums2 = [9,4,9,8,4]
#     return list(set(nums1) & set(nums2))
# print(nums())



# state_codes = {
#     'Alabama': 'AL',
#     'Alaska': 'AK',
#     'American Samoa': 'AS',
#     'Arizona': 'AZ',
#     'Arkansas': 'AR',
#     'California': 'CA',
#     'Colorado': 'CO',
#     'Connecticut': 'CT',
#     'Delaware': 'DE',
#     'District Of Columbia': 'DC',
#     'Federated States Of Micronesia': 'FM',
#     'Florida': 'FL',
#     'Georgia': 'GA',
#     'Guam': 'GU',
#     'Hawaii': 'HI',
#     'Idaho': 'ID',
#     'Illinois': 'IL',
#     'Indiana': 'IN',
#     'Iowa': 'IA',
#     'Kansas': 'KS',
#     'Kentucky': 'KY',
#     'Louisiana': 'LA',
#     'Maine': 'ME',
#     'Marshall Islands': 'MH',
#     'Maryland': 'MD',
#     'Massachusetts': 'MA',
#     'Michigan': 'MI',
#     'Minnesota': 'MN',
#     'Mississippi': 'MS',
#     'Missouri': 'MO',
#     'Montana': 'MT',
#     'Nebraska': 'NE',
#     'Nevada': 'NV',
#     'New Hampshire': 'NH',
#     'New Jersey': 'NJ',
#     'New Mexico': 'NM',
#     'New York': 'NY',
#     'North Carolina': 'NC',
#     'North Dakota': 'ND',
#     'Northern Mariana Islands': 'MP',
#     'Ohio': 'OH',
#     'Oklahoma': 'OK',
#     'Oregon': 'OR',
#     'Palau': 'PW',
#     'Pennsylvania': 'PA',
#     'Puerto Rico': 'PR',
#     'Rhode Island': 'RI',
#     'South Carolina': 'SC',
#     'South Dakota': 'SD',
#     'Tennessee': 'TN',
#     'Texas': 'TX',
#     'Utah': 'UT',
#     'Vermont': 'VT',
#     'Virgin Islands': 'VI',
#     'Virginia': 'VA',
#     'Washington': 'WA',
#     'West Virginia': 'WV',
#     'Wisconsin': 'WI',
#     'Wyoming': 'WY'
# }



# def state_code(state_name):
#     if len(state_name) < 3:
#         return  "Validation error: Please put at least 3 characters."
#     if len(state_name) > 50:
#         return "Validation error: Please put maximum 50 characters."
    
#     arr = []
#     state_name = state_name.lower()
#     for i in state_codes:
#         if state_name == i.lower():
#             return state_codes[i]
#         elif state_name.lower() in i.lower():
#             arr.append(i)

#     if len(arr) > 0:
#         return "Maybe you mean: " + ' or '.join(arr)
#     else:
#         return "No data found"

# state_name = "ala"
    
# print(state_code(state_name))



# def stat_code(state_name):
#     if len(state_name) < 2:
#         return "Validation error: Please put at least 3 characters"
#     if len(state_name) > 50:
#         return "Validation error: Maximum chars limit exceeded" 
#     if state_name in state_codes:
#         return state_codes[state_name]
#     arr = []
#     for i in state_codes:
#        if state_name == i.lower():

#             return state_codes[i]
#        elif state_name.lower() in i.lower():
#            arr.append(i)

#     if len(arr) > 0:
#         return "Maybe you Mean: " +  ' or '.join(arr)
#     else:
#         return "No Data Found"
    
    

# state_name = 'ala'
# print(stat_code(state_name))







# def guess_number(guess):
#     numbers = '2019'
#     cow = 0
#     bull = 0

#     for i in range(len(numbers)):
#         if numbers[i] == guess[i]:
#             cow += 1
#         elif guess[i] in numbers:
#             bull += 1
#         else:
#             continue
#     print(cow,bull)
    
        


      
            
        




# guess  = input("enter number ")

# guess_number(guess)


# answer = []

# def words():
#     wovels = "aeouiy"
#     while True:
#         word = input("Entner  word ")
#         if word == "stop":
#             break
#         count = 0
#         for i in word:
#             if i in wovels:
#                 count += 1
#         if count > 2:
#             answer.append(word)
# words()
# print(answer)


# words = "hello word"
# def words_count():
#     mydict = {}
#     for k,v in words.items():
#         if v in mydict:
#             mydict[v].append(k)

#         else:
#             mydict[v] = [k]
#     return mydict

# print(words_count())

    





# def sumarr(mlist):
#     if mlist == []:
#         return 0
#     else:
#         return mlist[0] + sumarr(mlist[1:])
    
# print(sumarr(mlist=([1,2,3])))



# def quick_sort(mlist):
#     if len(mlist) < 2:
#         return mlist
    
#     pivot = mlist[0]
#     less = [i for i in mlist[1:] if i <= pivot]
#     great = [i for i in mlist[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(great)

# print(quick_sort([12,1,14,16,12,2,2,2,2]))


# def len_arr(mlist):
#     if mlist == []:
#         return 0
#     else:
#         return 1 + len_arr(mlist[1:])
    
# print(len_arr(mlist=([1,2,3])))





# import json

# data = {"name":"Alice",
#         "Age": 30,
#         "Hobbies":["Reading","Coding","Traveling"]
#         }
# json_String = json.dump(data,indent=4,sort_keys=True)
# print(json_String)











# def find_leters():
#     with open("letters.txt","r") as let:
#         text = let.read().split()
#         leters = {}
#         for let in text:
#             if let.isalpha():
#                 if let not in leters:
#                     leters[let] = 1
#                 else:
#                     leters[let] += 1
#     return leters



# def selection_Sort(arr):
#     for ind in range(len(arr)):
#         min_ind = ind
#         for j in range(ind+1,len(arr)):
#             if arr[j][1] < arr[min_ind][1]:
#                 min_ind = j
#         arr[ind],arr[min_ind] = arr[min_ind],arr[ind]
#     return arr


# def main():
#     words = find_leters()
#     words_list = list(words.items())
#     sorted_list = selection_Sort(words_list)
#     print(sorted_list)
# main()






# def bubble_sort(aray,mydict):
#     for i in range(len(aray)):
#         for j in range(0,len(aray)-i-1):
#             if mydict[aray[j]] > mydict[aray[j+1]]:
               
#                 mydict[aray[j]], mydict[aray[j+1]] = mydict[aray[j+1]], mydict[aray[j]]
#     result = {}

#     for l in array:
#         result[l] = mydict[l]

#     return result

# mydict = {
#      'a': 3,
#      'd': 7,
#      'c': 2,
#      'r': 1
# } 

# array = list(mydict.keys())

# print(bubble_sort(array,mydict))

# def bubble_Sort(mylis,mydict):
#     for i in range(len(mylis)):
#         for j in range(0,len(mylis)-i-1):
#             if mydict[mylis[j]] > mydict[mylis[j+1]]:

#                 mydict[mylis[j]],mydict[mylis[j+1]] = mydict[mylis[j+1]],mydict[mylis[j]]


#     result = {}
#     for l in mylis:
#         result[l] = mydict[l]

#     return result


# mydict = {
#     "a":3,
#     "b":8,
#     "c": 1,
#     "d": 2
# }


# mylis = list(mydict.keys())

# print(bubble_Sort(mylis,mydict))


# def bubble_sort(arr,mydcit):
#     for i in range(len(arr)):
#         for j in range(0,len(arr)-i-1):
#             if mydcit[arr[j]] > mydcit[arr[j+1]]:
#                 mydcit[arr[j]],mydcit[arr[j+1]] = mydcit[arr[j+1]],mydcit[arr[j]]
#     result = {}
#     for i in arr:
#         result[i] = mydcit[i]
#     return result

# mydict = {
#     'a': 3,
#     'b': 4,
#     'c': 1
# }



# arr = list(mydict.keys())

# print(bubble_sort(arr,mydict))



# def selection_sort(arr,dict,size):
#     for i in range(size):
#         min_ind = i
#         for j in range(i+1,size):
#             if dict[arr[j]] < dict[arr[min_ind]]:
#                 min_ind = j
#         arr[i],arr[min_ind] = arr[min_ind],arr[i]
    
#     results = {}

#     for l in arr:
#         results[l] = dict[l]
    
#     return results

# dict = {
#     "a": 5,
#     "b": 1,
#     "c": 2
# }
# arr = list(dict.keys())
# size = len(arr)
# print(selection_sort(arr,dict,size))




# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
    
#     pivot = arr[0]
#     left  = [i for i in arr[1:] if i <= pivot]
#     right = [i for i in arr[1:] if i > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)


# print(quick_sort([2,3,14,1,5,4]))
















# def quick_sort(mlist):
#     if len(mlist) < 2:
#         return dict(mlist)

#     pivot = mlist[0][1]

#     left = [(k, v) for k, v in mlist[1:] if v <= pivot]
#     right = [(k, v) for k, v in mlist[1:] if v > pivot]

#     return {**quick_sort(left), mlist[0][0]: pivot, **quick_sort(right)}

# mydict = {
#     'a': 3,
#     'd': 7,
#     'c': 2,
#     'r': 1
# }

# print(quick_sort(list(mydict.items())))







# def binary_search(arr,x):
#     low = 0
#     high = len(arr) - 1
#     mid = len(arr) // 2

#     while arr[mid] != x and low <= high:
#         if x > arr[mid]:
#             low = mid +1
#         else:
#             high = mid -1
#         mid = (low + high) //2
    
#     if low > high:


#         print("no value")
#     else:
#         print("index = ", mid)

# arr = [1,2,3,4,5,6,7,8,9]
# x = 9
# binary_search(arr,x)
    





        
# def rec(mylist):
#     if len(mylist) == 1:    
#         return mylist[0]
#     else:
#         res = mylist[0] * rec(mylist[1:]) 
#         print(res)
#         return res

# arr = [2,3,6,7]
# print(rec(arr))



    

# def print_array_recursive(arr, index=0):
#     if index < len(arr):
#         print(arr[index])
#         print_array_recursive(arr, index + 1)

# my_array = [1, 2, 3, 4, 5]
# print_array_recursive(my_array)



# def double_array_recursive(arr, index=0):
#     if index < len(arr):
#         arr[index] *= 2
#         double_array_recursive(arr, index + 1)


# my_array = [1, 2, 3, 4, 5]
# double_array_recursive(my_array)
# print(my_array)  



# def double_first_element_recursive(arr, index=0):
#     if index == 0 and len(arr) > 0:
#         arr[index] *= 2
#     elif index < len(arr):
#         double_first_element_recursive(arr, index + 1)


# my_array = [7, 2, 3, 4, 5]
# double_first_element_recursive(my_array)
# print(my_array) 




# def get_upper(mstr):
#     for i in mstr:
#         if i.islower():
#             yield i.upper()
      


# mstr = "hello world"

# for el in get_upper(mstr):
#     print(el)


            





