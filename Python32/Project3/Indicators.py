#Ronit Ghosh 72805756 Lab Section 4 Late Pass

class Simple_moving_average():
   '''This class gives us the simple moving average'''
   def __init__(self, days):
      self._days=days

   def calculate(self,closing_prices):
      myList=[]
      d=self._days
      for i in range(d-1):
         myList.append(None)   
      for i in range(d, len(closing_prices)+1):
         if i>=d:
            a=closing_prices[i-d:i]
            b=sum(a)
            average=b/d
            myList.append(average)
      return myList

#s=Simple_moving_average(3)
#s.calculate([775.60,755.69,753.83,753.68,750.73,753.67,754.21,741.50,702.87,704.51,711.32,715.19,724.93,723.25,739.99,741.48,738.12,733.30,734.75,737.97,723.67,723.25])
                                      


class Directional_indicator():
   '''This class gives us the Directional Indicators'''
   def __init__(self, days):
      self._days=days

   def calculate(self, closing_prices):
      first=[]
      Indicator=[]
      d=self._days
      for i in range(len(closing_prices)-1):
         if i==0:
            first.append(0)
         if closing_prices[i]<closing_prices[i+1]:
            first.append(1)
         elif closing_prices[i] >closing_prices[i+1]:
            first.append(-1)
      for i in range(len(first)):
         if i<d:
            temp=first[0:i+1]
            new_list=sum(temp)
            Indicator.append(new_list)
         elif i>=d:
            temp=first[i-d+1:i+1]
            new_list=sum(temp)
            Indicator.append(new_list)
      print(Indicator)
      return Indicator
         



def execute(myClass, closing_prices):
   return myClass.calculate(closing_prices)



#execute(Directional_indicator(3),[775.60,755.69,753.83,753.68,750.73,753.67,754.21,741.50,702.87,704.51,711.32,715.19,724.93,723.25,739.99,741.48,738.12,733.30,734.75,737.97,723.67,723.25])
#execute(Simple_moving_average(3),[775.60,755.69,753.83,753.68,750.73,753.67,754.21,741.50,702.87,704.51,711.32,715.19,724.93,723.25,739.99,741.48,738.12,733.30,734.75,737.97,723.67,723.25])
      
            





