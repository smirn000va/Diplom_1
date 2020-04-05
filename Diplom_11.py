import csv

def main():
    with open('data.csv', 'r', encoding='utf-8') as f:
        fields = ['first_name', 'last_name', 'birthday', 'place birthday', 'phone number', 'email']
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:
            print(row)
                
        pass

if __name__ == '__main__':
    main()


    #чтение базы данных клиентов