def isValid(s):
  s=s.lower()
  if 'e' in s and s.count('e')==1 :
    idx=s.index('e')
    if s[idx - 1].isnumeric()==True:
      s=s.replace('e','')
  
  elif '.' in s and s.count('.')==1:
    idx=s.index('.')
    print(idx)
    if s[idx - 1].isnumeric() == True or s[idx + 1].isnumeric() == True:
      s=s.replace('.','')

  elif s[0] == '+' or s[0] == '-':
    first=s[0]
    if s.count(first)==1:
      s=s.replace(s[0],'') 

  elif s.isnumeric()==True:
    return True
    
  else:
    return False
