ticker = {
    'WMT':150, 'PINS':20, 'AMZ': 5, 'MSFT': 300, 'C': 175,
    'PFE': 33, 'CSCO': 95, 'T': 75, 'EBAY': 190, 'MMM': 220
    }
print('WMT for Walmart,PINS for Pinterest, AMZ for Amazon, MSFT for Microsoft, C for Citigroup Inc,')
print('PFE for Pfiser Inc, CSCO for Cisco Systems Inc, T for AT&T Inc, EBAY for eBayInc, or MMM for 3M Company')

while True:
    #input stock symbol
        symbol = input('Please enter a ticker symbol for one of the stocks listed above(Type exit to exit program):')
       
    
        if symbol =='exit':
            break
        
       #print current price of sticker chosen 
        if symbol in ticker.keys():
    
            print ('The current price of ' + symbol + ' is $' + str('{:,}'.format(ticker[symbol])))
            
        else: print("Please enter a different ticker symbol that is listed. No known cost for the ticker symbol",symbol)                                                
       
 
  
 
  
 
