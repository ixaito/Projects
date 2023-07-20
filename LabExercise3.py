class Phone:
    def __init__(self, id, brand, type, price):
        
        self.id = id
        self.brand = brand
        self.type = type
        self.price = price

class SmartPhone:
    
    def __init__(self):
        
        self.selectedPhone=[]
    
    
    def input_detail(self):
        
        print("ID\tBrand\t\tType\t\t\tPrice\n")
        print("1\tHuawei\t\tMate 50 Pro\t\tRM2599\n")
        print("2\tSamsung\t\tGalaxy A04S\t\tRM609\n")
        print("3\tApple\t\tiphone 14 pro\t\tRM5299\n")
        print("4\tVivo\t\tV25\t\t\tRM1239\n")
        
        try:
            with open("Smartphone.txt","w")as f:
            
                print("ID\tBrand\tType\tPrice\n",file=f)
                print("1\tHuawei\tMate 50 Pro\tRM2599\n",file=f)
                print("2\tSamsung\tGalaxy A04S\tRM609\n",file=f)
                print("3\tApple\tiphone 14 pro\tRM5299\n",file=f)
                print("4\tVivo\tV25\tRM1239\n",file=f)
            
        except Exception as e:
            
            print("Failed to upload data : {str(e)}")
            
        try:
            with open("Customer.txt","w+")as f:
                print("Name",file=f)
                strName=input("Please Enter Your Name :")
                f.write("f{strName}\n")
                
                while True:
                    
                    print("\nOption\n1.Order Phone\n2.Exit\n")
                    strChoice=input("-->")
                    
                    if strChoice=="1" :
                        
                        print("\nPlease spcify a phone ID of your choice")
                        iID=int(input("-->"))
                        print("")
                        print("Please specify a quantity:")
                        iQuantity=int(input("-->"))
                    
                        with open("Smartphone.txt","r+")as f:
                            data=f.readlines[1:]
                            data_row=data.split("\t")
                            if int(data_row[0]) == id:
                                selectedPhone = Phone(data_row[0], data_row[1], data_row[2], float(data_row[3][2:]))
                                selectedPhone.iQuantity = iQuantity
                                self.selectedPhone.append(selectedPhone)
                                print(f"{quantity} {selectedPhone.brand} {selectedPhone.type} is ordered !.")
                                break
                            
                        
                    elif strChoice=="2":
                        
                        break
                    
                    else:
                        
                        print("\nInvalid Input.Please try again!")
                        continue
                
                total = 0
                file.write("Ordered Smartphone:\n")
                for phone in self.selectedPhone:
                    price = phone.price * phone.quantity
                    file.write(f"{phone.id}\t{phone.brand}\t{phone.type}\t{phone.price}\t{phone.quantity}\t{price}\n")
                    total_price += price

                file.write(f"Total:RM {total_price}\n")
                print("Data has been registered !.")
                
        finally:
            print("Thank you for your visit !")
                        
                    
            
            
        
phone1=SmartPhone()
phone1.input_detail()