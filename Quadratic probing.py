class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        i = 1
        while self.table[index] is not None:
            index = (index + i**2) % self.size
            i += 1
        self.table[index] = key
    
    def search(self, key):
        index = self.hash_function(key)
        i = 1
        start_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + i**2) % self.size
            i += 1
            if index == start_index:
                break
        return -1
    
    def delete(self, key):
        index = self.search(key)
        if index != -1:
            self.table[index] = None

size = int(input("Enter the size of the hash table: "))
ht = HashTable(size)

while True:
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display Table\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        key = int(input("Enter the key to insert: "))
        ht.insert(key)
    elif choice == 2:
        key = int(input("Enter the key to search: "))
        result = ht.search(key)
        if result != -1:
            print(f"Key {key} found at index {result}")
        else:
            print(f"Key {key} not found")
    elif choice == 3:
        key = int(input("Enter the key to delete: "))
        ht.delete(key)
        print(f"Key {key} deleted")
    elif choice == 4:
        print("Hash Table:", ht.table)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

