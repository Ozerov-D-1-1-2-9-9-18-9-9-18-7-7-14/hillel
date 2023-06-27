import all


st1 = all.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = all.Student('Female', 23, 'Liza', 'Taylor', 'AN1451')
gr = all.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))

gr.delete_student('Taylor')
print(gr)
