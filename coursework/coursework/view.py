class View(object):

    @staticmethod
    def print_added_item(item_type, added_item, columns):
        print(f'New {item_type} has been added!')
        i = 0
        while i < len(added_item):
            print(f'{columns[i]}: {added_item[i]}')
            i += 1

    @staticmethod
    def print_updated_item(item_type, updated_item, columns):
        print(f'{item_type} has been updated! New values: ')
        i = 0
        while i < len(updated_item):
            print(f'{columns[i]}: {updated_item[i]}')
            i += 1

    @staticmethod
    def print_deleted_item(item_type, deleted_item, columns):
        print(f'{item_type} has been deleted! Deleted item values: ')
        i = 0
        while i < len(deleted_item):
            print(f'{columns[i]}: {deleted_item[i]}')
            i += 1

    @staticmethod
    def foreign_key_error(item_type, foreign_key, value):
        print(f'Error: Incorrect foreign key: {item_type} doesn\'t have {foreign_key} = {value}')

    @staticmethod
    def item_error(item_type, id, value):
        print(f'Error: There is no item with {id} = {value} in table {item_type}')

    @staticmethod
    def customer_error(email):
        print(f'Reader with email = \'{email}\' has already exist')

    @staticmethod
    def generation_message(seconds, number):
        print(f'{number} rows were generated and inserted by {seconds} seconds')

    @staticmethod
    def generation_error_message(number):
        print(f'Error while generating {number} rows')

    @staticmethod
    def database_error(e):
        print(e)

    @staticmethod
    def print_plot(plt):
        plt.show()

    @staticmethod
    def print_table(table):
        print(table)

    @staticmethod
    def print_tables(table1, table2, table3, table4, categories):
        print(categories[0])
        print(table1)
        print(categories[1])
        print(table2)
        print(categories[2])
        print(table3)
        print(categories[3])
        print(table4)

    @staticmethod
    def print_prices(differences, stores, categories):
        i = 0
        while i < 4:
            if differences[i][1] == 0:
                print(f'{categories[i]}:')
                print(f'Prices in {stores[0]} are bigger on {round(differences[i][0], 2)}%')
            else:
                print(f'{categories[i]}:')
                print(f'Prices in {stores[1]} are bigger on {round(differences[i][0], 2)}%')
            i += 1
