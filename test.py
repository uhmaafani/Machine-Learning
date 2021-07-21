def fees(age):
  if (age<=17):
    return 200
  elif (age>17 and age<40):
    return 400patient = []
patient_fees = []
while True:
  try:
    age_string = input()
    
    if age_string == '':  #break on last Enter
      break

    if len(patient) == 20: #break if current patient count is 20
      break

    age = int(age_string)
    if (age <= 0 or age > 120):
      print('invalid age')
      break
    else:
      patient.append(age)
      patient_fees.append(fees(age))
  except:
    print('Problem in input. Please try again')
    break
  else: #age is >40
    return 300
    
    
    
