import pandas as pd
messyd= {'Box': ['Box 1','Box 1','Box 1','Box 2','Box 2','Box 2',],
        'Dimension': ['Length','Width','Height','Length','Width','Height'],
        'Value': [6,4,2,5,3,4]}
boxesd = pd.DataFrame(messyd, columns = ['Box','Dimension','Value'])
tidyd = boxesd.pivot_table(index = ['Box'], columns = 'Dimension', values = 'Value').reset_index()
f4 = tidyd['Volume'] = tidyd.Length*tidyd.Height*tidyd.Width
fformat = pd.DataFrame(tidyd, columns = ['Box','Height','Length','Width','Volume'])
