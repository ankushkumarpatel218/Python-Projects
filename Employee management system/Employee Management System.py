# Employee Management System

from Add_Employee import *
from Remove_Employee import *
from Update_Employee import *
from Promote_Employee import *
from Search_Employee import *
from show_all_emp import *

def main():
    print("""\n***************************\nEmployee Management System\n***************************\n""")
    
    print('******************************************')
    print("1.Add Employee Data\n"
          "2.Remove Employee Data\n"
          "3.Update Employee Data\n"
          "4.Promotion of an Employee\n"
          "5.Search for an Employee Data\n"
          "6.Show All Employee in the Company\n"
          '*******************************************')

    choice = input('\nEnter the option number:')

    if choice == '1':
        add_employee()
        main()
        # function1 - Add Employee Data function

    elif choice == '2':
        remove_employee()
        main()
        # function2 - Remove Employee Data function

    elif choice == '3':
        update_employee()
        main()
        # function3 - Update Employee Data function

    elif choice == '4':
        promote_employee()
        main()
        # function4 - Promotion of an Employee function

    elif choice == '5':
        search_employee()
        main()
        # function5 - Search for an Employee Data function
    
    elif choice == '6':
        show_all_employee()
        main()

    else:
        print("Wrong Option! Pls try Again")
        main()


if __name__ == "__main__":
    main()
