black = [150, 179, 149, 152, 154]
orange = [162, 181, 151, 160, 170]


def classPhoto(black, orange):
  for student in black:
    if student not in blackUniforms:
      blackUniforms.append(student)
      
  for student in orange:
    if student not in orangeUniforms:
      orangeUniforms.append(student)
      
  return len(blackUniforms) == len(black) and len(orangeUniforms) == len(orange)
  
print(classPhoto(black, orange))
