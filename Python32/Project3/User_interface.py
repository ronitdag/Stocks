#Ronit Ghosh 72805756 Lab Section 4 Late Pass
from datetime import date
import time
import Indicators
import Signal_strategies
import Download


def ticker_symbol():
   response=input('What is the ticker symbol for the company:')
   if response !='':
      return response
   else:
      return ticker_symbol()

today=date.today()
print(today)

def start_date():
   '''Returns the start date'''
   print('When you are typing in the month, 1 is January, 12 is December... etc.')
   response=input('Start date (yyyy-mm-dd): ')
   try:
      time.strptime(response, '%Y-%m-%d')
      if response < str(today):
         year,month,day=response.split('-')
         month=str(int(month)-1)
         print(month)
         if len(month)==1:
            month='0'+str(month)
         new_response='{}-{}-{}'.format(year, month, day)
         print(new_response)
         return new_response
      else:
         print('Sorry! The date is not before today. Please try again.')
         return start_date()
   except ValueError:
      print('Invalid date format!')
      return start_date()

ticker=ticker_symbol()
start=start_date()   


def end_date():
   '''Returns end date'''
   response=input('End date (yyyy-mm-dd): ')
   try:
      time.strptime(response, '%Y-%m-%d')
      if response < str(today) and response > str(start):
         year,month,day=response.split('-')
         month=str(int(month)-1)
         print(month)
         if len(month)==1:
            month='0'+str(month)
         new_response='{}-{}-{}'.format(year, month, day)
         print(new_response)
         return new_response
      else:
         print('Sorry! The date is not before today. Please try again.')
         return end_date()
   except ValueError:
      print('Invalid date format!')
      return end_date()
   
end=end_date()


def signal_days():
   response=input('How many days would you like your simple moving average to be?')
   try:
      answer=int(response)
      if answer>0:
         return answer
      else:
         print('Error! Number is smaller than 0')
         signal_days()
   except:
      print('Error! This is not an int')
      signal_days()

def signal_strategy():
   Download.url=HTTP
   Final_url = Download._final_url_contents()
   Date = Final_url[0]
   date_list=[]
   closing_price_list=[]
   for i in Date:
      Day=i
      date_list.insert(0, Day)
   date_list.insert(0,'Date')
   date_list.pop()
   Title_closing_prices=Final_url[1]
   sma_list=[]
   Ticker_closing_prices=(Title_closing_prices[1:])
   prices=Title_closing_prices[0:]
   for i in range(len(Ticker_closing_prices)):
      Ticker_closing_prices[i] = float(Ticker_closing_prices[i])

   for i in prices:
      closing_price_list.append(i)
   
   response=input('What signal strategy would you like to use?(directional or sma)')
   if response=='sma':
      sma_list=[]
      strategy_list=[]
      days=signal_days()
      Indicator=Indicators.execute(Indicators.Simple_moving_average(days),Ticker_closing_prices)
      sma_list.append('Sma')
      for i in Indicator:
         myIndicator=i
         if i != None:
            myIndicator=str(i)[:6]
         sma_list.append(myIndicator)
      Strategy=Signal_strategies.execute(Signal_strategies.Signal_sma(Indicators.execute(Indicators.Simple_moving_average(days), Ticker_closing_prices),Ticker_closing_prices))
      print(Strategy)
      strategy_list.append('Signal_strategies')
      for i in Strategy:
         myStrategy=i
         strategy_list.append(myStrategy)
      print(len(date_list))
      print(len(closing_price_list))
      print(len(sma_list))
      print(len(strategy_list))
      for i in range(len(date_list)):
         
         print('{:10}   {:10}  {:10}   {:10}'.format(date_list[i], closing_price_list[i], sma_list[i],strategy_list[i]))
   elif response=='directional':
      indicator_list=[]
      strategy_list=[]
      days=signal_days()
      buy_threshold=int(input('What is the buy threshold'))
      sell_threshold=int(input('What is the sell threshold'))
      Indicator=Indicators.execute(Indicators.Directional_indicator(days),Ticker_closing_prices)
      indicator_list.append('Indicator')
      for i in Indicator:
         myIndicator=i
         indicator_list.append(myIndicator)
      Strategy=Signal_strategies.execute(Signal_strategies.Signal_Directional(Indicators.execute(Indicators.Directional_indicator(days),Ticker_closing_prices),buy_threshold,sell_threshold))
      strategy_list.append('Signal_strategies')
      for i in Strategy:
         myStrategy=i
         strategy_list.append(myStrategy)

      for i in range(len(date_list)):
         print('{:10}  {:10}  {:10}  {:10}'.format(date_list[i], closing_price_list[i], indicator_list[i], strategy_list[i]))

         
   else:
      print('You did not select simple-moving-average or directional. Please try again.')
      signal_strategy()                  




if __name__=='__main__':
   symbol=ticker
   start_date=start
   end_date=end
   start_year=start_date[:4]
   start_month=start_date[5:7]
   start_day=start_date[8:]
   end_year=end_date[:4]
   end_month=end_date[5:7]
   end_day=end_date[8:]
   
   HTTP='''http://ichart.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d
   '''.format(symbol,start_month, start_day, start_year, end_month, end_day, end_year)

   signal_strategy()










   
