from flask import Response, request
import random
import string
import os

class Database(object):

    def __init__(self,**kwargs):

        self.lang = 'en-us'
        self.file_size = 2000000
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.path_file = os.path.join(self.my_path,'../static/generated_file.txt')

        self.count_alfanum = 0
        self.count_real = 0
        self.count_integer = 0
        self.count_string = 0

        #respon structure
        self.payload = dict(
            error_code=0,
            results={},
            meta={},
            resp_message=''
        )

    def RandomText(self,text_len):
        letters = string.ascii_letters
        randomtext = ''.join(random.choice(letters) for i in range(text_len))
        return randomtext

    def RandomInteger(self,num_len):
        number = string.digits
        randomint = ''.join(random.choice(number) for i in range(num_len))
        return randomint

    def RandomAlfanum(self,alfanum_len):
        text = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        randomalfa = ''
        for i in range(alfanum_len):
            rand_idx = random.randint(0,len(text)-1)
            randomalfa +=''.join(text[rand_idx])

        return randomalfa

    def RandomRealnumber(self,realnum_len):
        rand_int = self.RandomInteger(realnum_len)
        rand_real = random.random()
        real_number = rand_real * int(rand_int)
        return real_number

    def GenerateRandom(self):
        random_len = random.randint(1,15)
        random_choise = random_len % 4 
        text_out = ''
        if random_choise == 0:
            text_out = self.RandomText(random_len)
            self.count_string += 1
        elif random_choise ==1:
            text_out = self.RandomInteger(random_len)
            self.count_integer += 1
        elif random_choise ==2:
            text_out = self.RandomAlfanum(random_len)
            self.count_alfanum += 1
        else:
            text_out = self.RandomRealnumber(random_len)
            self.count_real += 1
        
        return text_out

    def GetFile(self):
        '''generating whole file'''
        

        if os.path.exists(self.path_file):
            os.remove(self.path_file)

        idx=0
        while idx < 1:
            with open(self.path_file,'a') as fd:
                some_txt = self.GenerateRandom()
                fd.write(str(some_txt))
                fd.write(',')

                if int(os.path.getsize(self.path_file))> self.file_size:
                    idx += 1
                    fd.close()

        output = {
            'count_alfanum':self.count_alfanum,
            'count_realnumber':self.count_real,
            'count_integer':self.count_integer,
            'count_string':self.count_string,
            'file_location':'http://localhost:5000/omniapi/download/generated_file.txt'
        }
        
        self.payload['results']=output
        return self.payload

        


    # def get_bill(self):
    #     '''method untuk cek user dari no_hp dan email'''

    #     query = '''
    #     select * from discount
    #     '''
    #     result = self.cursor(query).fetchall()
    #     bills = []
    #     price_total = 0
    #     dis_total = 0
    #     count = 0
    #     for row in result :
    #         tipe = ''
    #         refund = ''
    #         discount = 0
    #         if row['dis_code'] == 1:
    #             tipe = 'Fashion'
    #             refund = 'Yes'
    #             discount = 0.1 * row['Price']
    #         if row['dis_code'] == 2:
    #             tipe = 'Furniture'
    #             refund = 'No'
    #             discount = 10 + (0.02 * row['Price'])
    #         if row['dis_code'] == 3:
    #             tipe = 'Jewelry'
    #             refund = 'No'
    #             if row['Price'] >= 100:
    #                 discount = 0.01 * (row['Price']-100) 

    #         amount = row['Price'] - discount

    #         price_total += row['Price']

    #         dis_total += discount

    #         count += 1

    #         bill = {
    #             'Name':row['name'],
    #             'DisCode':row['dis_code'],
    #             'Type':tipe,
    #             'Refundable':refund,
    #             'Price': row['Price'],
    #             'Discount': discount,
    #             'Amount':amount,
    #         }
    #         bills.append(bill)

    #     if count == 0 :
    #         self.payload['error_code']=204
    #         return self.payload
        
    #     meta = {
    #         'price_subtotal': price_total,
    #         'discount_subtotal': dis_total,
    #         'grand_total': price_total-dis_total
    #     }
    #     self.payload['results'] = bills
    #     self.payload['meta'] = meta

    #     return self.payload

    # def save_dis(self,prod,price,dis_code):
    #     '''method untuk menyimpan register data'''

    #     query = '''
    #     INSERT INTO discount (name, dis_code, price) 
    #     VALUES (%s, %s, %s);
    #     '''

    #     result = self.cursor(query,[prod,dis_code,price])

    #     if not result.rowcount:
    #         self.payload['error_code']=500
    #         return self.payload
        
    #     self.payload['results'] = 'saved successfully'
    #     return self.payload
        