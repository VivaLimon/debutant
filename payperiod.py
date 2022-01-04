#find out how many pay periods to get to full match

#part 1 - inputs: gross salary (can calculate from that hourly & biweekly pay) 
# company match max (% usually --> max contribution --> divide it by a certain number of weeks)
#output = number of pay periods, and contribution percent
import pandas

def pay_period():
    print('This is a calculator to help you max out your employer match ($!free money!$)')
    salary = int(input('Annual salary: '))
    hourly = round(salary / 2080,2)
    # daily = hourly * 8 
    # weekly = daily * 5
    # biweekly = weekly * 2
    biweekly = hourly * 8 * 5 * 2
    print(f'Hourly pay: {hourly} and biweekly pay: {biweekly}')

    company_match = float(input('% company match: '))
    annual_match_max = salary * company_match / 100
    print(f'Annual match max ($): {annual_match_max}')
    
    #this will print out all possible scenarios for you to choose how much to assign to the contribution%
    N = 26
    listN = []
    listoverNweeks = []
    listcontribution = []
    
    overNweeks = round(annual_match_max / N,  2 )
    contribution = round(overNweeks / biweekly * 100, 1)
    print(overNweeks, contribution)

    
    for i in range(26):
        
        overNweeks = round(annual_match_max / N,  2 )
        contribution = str(round(overNweeks / biweekly * 100, 1))+'%'
        print(N, overNweeks, contribution)
        listN.append(N)
        listoverNweeks.append(overNweeks)
        listcontribution.append(contribution)
        
        N -= 1
        i += 1
    #I dont like how unformatted the prints are, so I'm adding a table
    df = pandas.DataFrame(
        zip(listN,listoverNweeks,listcontribution) , 
        columns=['# of Pay Periods','Biweekly Deduction','Contribution %']      )

    print(df)

pay_period()
