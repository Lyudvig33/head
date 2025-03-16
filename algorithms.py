
# def select_sort():
#     with open('words.txt', 'r') as word_file:
#         sorted_word = []
#         for line in word_file:
#             words = line.split()
#             for word in words:
#                 if word.isalpha():
#                     sorted_word.append(word)

#     for i in range(len(sorted_word)):
#         min_ind = i
#         for j in range(i + 1, len(sorted_word)):
#             if len(sorted_word[j]) < len(sorted_word[min_ind]):
#                 min_ind = j
#         sorted_word[i], sorted_word[min_ind] = sorted_word[min_ind], sorted_word[i]

#     return sorted_word

# words = select_sort()
# print(words)

# def bubble_sort():
#     with open('words.txt', 'r') as file:
#         sorted_words = []
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word.isalpha():
#                     sorted_words.append(word)


#     for i in range(len(sorted_words)):
#         for j in range(0, len(sorted_words)-i-1):
#             if len(sorted_words[j]) > len(sorted_words[j+1]):
#                 sorted_words[j], sorted_words[j+1] = sorted_words[j+1], sorted_words[j]

#     return sorted_words

# sorted_words = bubble_sort()
# print(sorted_words)



# def create_tasks_in_txt():
#     print('what the adden in tasks list')

#     with speech_recognition.Microphone() as mic:
#         sr  = speech_recognition.Recognizer()
#         sr.adjust_for_ambient_noise(source=mic,duration=1)
#         audio = sr.listen(source=mic)
#         query  = sr.recognize_google(audio_data=audio)

#     with open("today_tasks.txt",'a') as file:
#             file.write(f"{query}\n")

#     return f"today Task's {query} has been added to today_tasks"



# def is_sorted(mlist):
#     flag = True
#     for i in range(len(mlist)):
#         if i == len(mlist)-1:
#             break
#         if mlist[i] > mlist[i+1]:
#             flag = False

#     if fla
# g == True:
#         return True
#     return False

# mlist = [1,2,3,4,5,6]
# print(is_sorted(mlist))



# def anagramma(str1,str2):
#     list1 = list(str1)
#     for i in str2:
#         if i not in list1:
#          return False
#         if list1.count(i) != str2.count(i):
#             return False
#     return True

# str1 = "helto"
# str2 = "olleh"
# print(anagramma(str1,str2))




