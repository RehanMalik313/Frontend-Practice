#Task03:
#Create a list of six school subjects. Ask the user which of these subjects they don’t like. Delete the subject they have chosen from the list before you display the list again.

school_subj = ['math', 'english', 'science', 'bio', 'urdu', 'chemistry']
print(school_subj)
print()
user = input('Which subject you don`t like: ' )
getrid = school_subj.index(user)
del school_subj[getrid]
print(school_subj)

#Another Logic:

school_subj = ['math', 'english', 'science', 'bio', 'urdu', 'chemistry']
print(school_subj)
print()
user = input('Which subject you don`t like: ' )
if user in school_subj:
    school_subj.remove(user)
    print(school_subj)
else:
    print(f'{user} is not in the list.')
