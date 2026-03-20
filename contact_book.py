contacts = []
try :
    file = open("contacts.txt","r")
    for line in file :
        name, phone, email = line.strip().split(",")
        contact = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        contacts.append(contact)
    file.close()
except FileNotFoundError :
    pass 
while True :
    print("============================Contact Book ===========================================")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice :")

    if choice == '1' : #Add contact
        name = input("Enter your name :")
        phone = input("Enter phone number :")
        email = input("Enter your Email :")

        duplicate = False
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                duplicate =True
                break 
        if duplicate: 
            print("The contact with same name alredy exist ...")
        else :
            contact = {
                "name" : name,
                "phone" : phone,
                "email" : email
            } 
            contacts.append(contact)
            file = open("contacts.txt","a")
            file.write(name + "," + phone + "," + email + "\n")
            file.close() 
            print("Contact Added Successfully !!")
           



    elif choice=='2': #view contact
        if len(contacts)==0:
            print("No contact found ")
        else:
            print("*********************************Contact list**************************************")
            for i , contact in enumerate(contacts,start=1):
                print(f"{i}. name : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact.get('email','Not Available')}")
                print("------------------------------------------------------")
                    

    elif choice== '3': #search contact
        search_name = input("Enter a name to search :")
        found= False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(f"name : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact.get('email','Not Available')}")
                found = True 
                break

        if not found:
            print("Contact not found !!")


    elif choice == '4': #delete contact 
        delete_name = input("Enter name to delete: ")
    
        found = False
        new_contacts = []

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                found = True
            else:
                new_contacts.append(contact)

        if found:
            contacts = new_contacts   # update list

            file = open("contacts.txt", "w")
            for c in contacts:
                file.write(f"{c['name']},{c['phone']},{c['email']}\n")
            file.close()

            print("Contact Deleted Successfully!")
        else:
            print("Contact not found")

            
    elif choice =='5':
        print("Existing ....")
        break

    else :
        print("Invalid choice !! Try again..")