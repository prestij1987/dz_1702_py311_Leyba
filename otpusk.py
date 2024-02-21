'''Человек работает в компании с накоплением отпускных дней и автоматическим 
индексированием зарплаты: каждый месяц она увеличивается на  100 рублей, 
а за каждые две недели появляется один день отпуска. Отпускные рассчитываются как 
зарплата на конец предыдущего месяца. Человек вводит дату поступления на работу. 
Вывести количество дней отпуска и сумму отпускных, предполагая, что он ещё ни разу 
не брал отпуск.
3. Усложнение: человек вводит своё имя. В "базе данных" хранится для каждого 
человека количество взятых дней отпуска. {'Вася': 42'''

'''sallary = input('Введите сумму зарплаты: ')
kolvo_day = input('Введите чило дней: ')
otpusk_summ = 100
#summ_otpusk = input('Введите сумму отпускных: ')
mouth_work = int(input('Введите количество отработанных месяцев '))
mouth_work_all = mouth_work + 100

mouth_year = 12
week_year = 365 / 7
print(week_year)
#money = int(kolvo_day * summ_otpusk)'''

from datetime import datetime

data_priema = int(input('Vvedite daty(1-12):' ))
data_yvoln = int(input('Vvedite daty yvolneya(1-12): '))
summ = int(input('Vvedite summy: '))
limit_zarpl = (summ + 100) * 12
data_raboty = data_yvoln - data_priema

vremy_raboty = int(datetime.date(2023, 7, 1))
vremy_raboty2 = int(vremy_raboty)
if (data_raboty < vremy_raboty):
    work_all = int(vremy_raboty )- data_raboty

day_otpusk = work_all * 2

staj = data_priema - data_yvoln
day_otpusk = (2 * staj) * 100 + summ
summ_otpusk = (day_otpusk * limit_zarpl)

print('Summa nachisl', summ_otpusk, 'day', day_otpusk)



