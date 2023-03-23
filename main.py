import sys
import time
import os.path
import argparse
import email.utils
def read(inputFile): 
    list = []
    if os.path.isfile(inputFile):
         if os.path.getsize(inputFile):
            print("File exists and not empty!")
            with open(inputFile, "r") as f:
                for i in f.readlines():
                    if is_valid_email(i):
                        list.append(i)
                    else:
                        print("removing unvalidated mails")
                return list
         else:
            print("File exists and is empty.")

def is_valid_email(email):
    """
    Validate the format of an email address without using regular expressions
    """
    if '@' not in email:
        return False
    # Split the email address into the username and domain name parts
    username, domain = email.split('@')
    if not username or not domain:
        return False
    if '.' not in domain:
        return False
    # Split the domain name into the top-level domain and the subdomain parts
    subdomain, tld = domain.split('.')
    if not tld:
        return False

    return True 
# def is_valid_email(email):
#     try:
#         email = email.utils.parseaddr(email)[1]
#         if not email:
#             return False
#     except Exception:
#         return False
#     # Split the email address into username and domain
#     username, domain = email.split('@')
#     # Check if the domain has a valid format
#     if not domain.count('.') >= 1:
#         return False
#     # Check if the username and domain contain only valid characters
#     if not all(c.isalnum() or c in '.-_' for c in username):
#         return False
#     if not all(c.isalnum() or c in '-' for c in domain):
#         return False
#     return True
      
            # try: 
    #     with open(inputFile, 'r') as f: 
    #         lines = f.readlines() 
    #         rl= [line for line in lines if line.strip()] 
    #     if len(rl) == 0: 
    #         raise Exception(f"File {inputFile} present but data is missing, set operations can't be performed") 
    #     return rl 
    # except FileNotFoundError: 
    #     print("{0} not found".format(inputFile)) 
    #     sys.exit(1) 
  
    
#union   
def union(list1, list2):
   list3 = [] 
   for email in list1:
     if email   in list3:
        list3.append(email)
     for email in list2:
        if email not in list2:
            list3.append(email)
   return list3
def intersection(list1, list2):
    list3 = []
    for email  in list1:
        if email in list2: 
            list3.append(email)
    return list3 
# Minus
def minus(list1,list2):
    list3 = []
    for email in list1:
        if email not in list3:
            list3.append(email)
    for email in list2:
        if email not in list3:
            list3.append(email)
    return list3

#Result file creating
def create_file( func,list1,list2):
    with open(sys.argv[3], "w") as file3:
        definition = list(dict.fromkeys(func,(list1,list2))) 
        for email in definition:
            file3.write(email)
# ArgumentsValidation:
'''This validation is used to make the user to be aware of the correct nuber of arguments to be passed'''

message1 = "2 arguments have to be passed as per the instructions"
message2 = "Please create the missing file which is "

def Arguments_Validation(n,args_list):
    if len(n) != 4:
        try:
            print("Valid no of Arguments")
        except IndexError:
            print("require 4 Arguments")
            print('Please provide the required number of args and', message1)            
 #File validation
# inputFile ='inputFile' 
# if os.path.exists(inputFile):
#     print("File exists")
# else:
#     print("File does not exist") 

# Check if the file exists
# if os.path.exists(inputFile):
#     # Check if the file is not empty
#     if os.path.getsize(inputFile) > 0:
#         print(f'The file "{inputFile}" exists and is not empty.')
#     else:
#         print(f'The file "{inputFile}" exists but is empty.')
# else:
#     print(f'The file "{inputFile}" does not exist.')            

if __name__ == '__main__':
    #try:
        start_time = time.time()
        parser = argparse.ArgumentParser(description='two inputFile files containing email addresses.')
        parser.add_argument('File1', help='First inputFile file')
        parser.add_argument('File2', help='Second inputFile file')
        parser.add_argument('output', help='Output file')
        args = parser.parse_args()
        arg = sys.argv
        arg_list1 = read(args.File1)
         #print(len(list1))
        arg_list2 = read(args.File2)
    
        Arguments_Validation(arg_list1,arg_list2)
    
        is_valid_email(arg_list1)
        print(is_valid_email)
        is_valid_email(arg_list2)
        print(is_valid_email)
          
        with open(sys.argv[3], 'r') as f:
         list3 = f.readlines()
         length =len(list3)
        if sys.argv[0] == "Union.py":
            read(function[0], arg_list1, arg_list2)
        elif sys.argv[0] == "Intersection.py":
            read(function[1], arg_list1, arg_list2)
        elif sys.argv[0] == "Minus.py":
            read(function[2], arg_list1, arg_list2)
        end_time = time.time()
         # print(f"{(sys.argv[1])} emails,{(list3)}, {(sys.argv[2])} emails, {len(sys.argv[1])},Time taken: {end_time - start_time:.2f} seconds")
        print(f"output:{(sys.argv[1])} emails,{len(arg_list1)},{(sys.argv[2])} emails, {(len(arg_list2))},{(sys.argv[3])} emails,{(length)}, Time taken: {end_time -start_time} seconds")
    #except Exception as e:
        #print(e) 
