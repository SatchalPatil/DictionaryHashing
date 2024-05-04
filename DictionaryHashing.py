def hash_function(key, size):
    return hash(key) % size

def create_dictionary(size):
    return [[] for _ in range(size)]

def insert(dict, key, value):
    index = hash_function(key, len(dict))
    for pair in dict[index]:
        if pair[0] == key:
            pair[1] = value
            return
    dict[index].append([key, value])

def find(dict, key):
    index = hash_function(key, len(dict))
    for pair in dict[index]:
        if pair[0] == key:
            return pair[1]
    return None

def delete(dict, key):
    index = hash_function(key, len(dict))
    for i, pair in enumerate(dict[index]):
        if pair[0] == key:
            del dict[index][i]
            return

def display_dictionary(dict):
    print("Dictionary:")
    for bucket in dict:
        for pair in bucket:
            print("Key:", pair[0], "| Value:", pair[1])

size = 10
dict = create_dictionary(size)

while True:
    action = int(input("Enter action \n1.Add a Word \n2.Find a Word \n3.Delete a Word \n4.Display Dictionary \n5.Exit : "))
    
    if action == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        insert(dict, key, value)
        print("Key-Value pair inserted.")
    
    elif action == 2:
        key = input("Enter key to find: ")
        result = find(dict, key)
        if result is not None:
            print("Value found:", result)
        else:
            print("Key not found.")
    
    elif action == 3:
        key = input("Enter key to delete: ")
        delete(dict, key)
        print("Key deleted.")
    
    elif action == 4:
        display_dictionary(dict)
    
    elif action == 5:
        print("Thank You for using this Code")
        break
    
    else:
        print("Invalid action. Please enter insert/find/delete/display/exit.")
