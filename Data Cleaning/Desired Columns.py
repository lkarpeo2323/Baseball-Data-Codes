import pandas as pd

#The file you are trying to clean
old_path = '3-3File.csv'

data = pd.read_csv(old_path)

#List the columns you wanna keep
keep = [
'Pitcher',
'Batter',
'Balls',
'Strikes',
'RelSpeed',
'Tilt',
'ExitSpeed',
'Angle'
    ]

kept = data[keep]

#desired new file path
new_path = 'CleanedBaseball.csv'

kept.to_csv(new_path,index=False)

print(f"The data has been cleaned to {new_path}")
        
        
            
                  
            
              
