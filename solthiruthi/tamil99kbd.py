## -*- coding: utf-8 -*-
## (C) 2019 Muthiah Annamalai,
## This module is part of solthiruthi project under open-tamil umbrella.
## This code maybe used/distributed under MIT LICENSE.

# Tamil99 Keyboard adjacency matrix - aka - confusion matrix
# for keystroke error modeling

confusion_matrix = {
u'ஆ' : [u'ஈ',u'இ',u'அ'], 
u'ஈ' : [u'ஊ',u'உ',u'இ',u'அ',u'ஆ'], 
u'ஊ' : [u'ஏ',u'உ',u'உ',u'இ',u'ஈ'], 
u'ஏ' : [u'ள',u'எ',u'ஐ',u'உ',u'ஊ'], 
u'ள' : [u'ற',u'க',u'எ',u'ஐ',u'ஏ'], 
u'ற' : [u'ன',u'ப',u'க',u'எ',u'ள'], 
u'ன' : [u'ட',u'ம',u'ப',u'க',u'ற'], 
u'ட' : [u'ண',u'த',u'ம',u'ப',u'ன'], 
u'ண' : [u'ச',u'ந',u'த',u'ம',u'ட'], 
u'ச' : [u'ஞ',u'ய',u'ந',u'த',u'ண'], 
u'ஞ' : [u'ய',u'ந',u'ச'], 
u'அ' : [u'ஆ',u'இ',u'ஔ'], 
u'இ' : [u'ஊ',u'உ',u'ஔ',u'அ',u'ஆ',u'ஈ'], 
u'உ' : [u'ஏ',u'ஐ',u'ஓ',u'ஔ',u'இ',u'ஈ',u'ஊ'], 
u'ஐ' : [u'ள',u'எ',u'ஒ',u'ஓ',u'உ',u'ஊ'], 
u'எ' : [u'ற',u'க',u'வ',u'ஒ',u'ஐ',u'ஏ',u'ள'], 
u'க' : [u'ன',u'ப',u'ங',u'வ',u'எ',u'ள',u'ற'], 
u'ப' : [u'ட',u'ம',u'ல',u'ங',u'க',u'ற',u'ன'], 
u'ம' : [u'ண',u'த',u'ர',u'ல',u'ப',u'ன',u'ட'], 
u'த' : [u'ச',u'ந',u'ழ',u'ர',u'ம',u'ட',u'ண'], 
u'ந' : [u'ஞ',u'ய',u'ழ',u'த',u'ண',u'ச'], 
u'ய' : [u'ந',u'ச',u'ஞ'], 
u'ஔ' : [u'உ',u'ஓ',u'இ'], 
u'ஓ' : [u'உ',u'ஐ',u'ஒ',u'ஔ'], 
u'ஒ' : [u'எ',u'வ',u'ஓ',u'ஐ'], 
u'வ' : [u'க',u'ங',u'ஒ',u'எ'], 
u'ங' : [u'ப',u'ல',u'வ',u'க'], 
u'ல' : [u'ம',u'ர',u'ங',u'ப',u'்'], 
u'ர' : [u'த',u'ழ',u'ல',u'ம',u'்'], 
u'ழ' : [u'ந',u'ர',u'த',u'்'], 
}

inv_confusion_matrix = {
u'ஆ' : [u'ஈ',u'அ',u'இ'], 
u'ஈ' : [u'உ',u'ஊ',u'இ',u'ஆ'], 
u'ஊ' : [u'உ',u'ஈ',u'ஏ',u'இ',u'ஐ'], 
u'ஏ' : [u'உ',u'ள',u'ஊ',u'எ'], 
u'ள' : [u'ற',u'ஐ',u'க',u'ஏ',u'எ'], 
u'ற' : [u'ன',u'ள',u'ப',u'க',u'எ'], 
u'ன' : [u'ற',u'ப',u'க',u'ட',u'ம'], 
u'ட' : [u'ன',u'ண',u'ப',u'த',u'ம'], 
u'ண' : [u'ந',u'ச',u'த',u'ட',u'ம'], 
u'ச' : [u'ந',u'ண',u'த',u'ய',u'ஞ'], 
u'ஞ' : [u'ந',u'ச',u'ய'], 
u'அ' : [u'ஈ',u'இ',u'ஆ'], 
u'இ' : [u'அ',u'ஆ',u'உ',u'ஈ',u'ஊ',u'ஔ'], 
u'உ' : [u'இ',u'ஈ',u'ஊ',u'ஏ',u'ஐ',u'ஓ',u'ஔ'], 
u'ஐ' : [u'உ',u'ள',u'ஏ',u'எ',u'ஓ',u'ஒ'], 
u'எ' : [u'ஏ',u'ற',u'ஐ',u'ள',u'ஒ',u'க',u'வ'], 
u'க' : [u'ன',u'ப',u'எ',u'ற',u'ள',u'வ',u'ங'], 
u'ப' : [u'ன',u'ம',u'ற',u'ல',u'க',u'ங',u'ட'], 
u'ம' : [u'ண',u'த',u'ன',u'ப',u'ர',u'ல',u'ட'], 
u'த' : [u'ண',u'ந',u'ம',u'ர',u'ழ',u'ச',u'ட'], 
u'ந' : [u'ண',u'த',u'ய',u'ழ',u'ச',u'ஞ'], 
u'ய' : [u'ந',u'ச',u'ஞ'], 
u'ஔ' : [u'உ',u'ஓ',u'அ',u'இ'], 
u'ஓ' : [u'உ',u'ஐ',u'ஒ',u'ஔ'], 
u'ஒ' : [u'ஐ',u'ஓ',u'வ',u'எ'], 
u'வ' : [u'ங',u'ஒ',u'க',u'எ'], 
u'ங' : [u'வ',u'ப',u'க',u'ல'], 
u'ல' : [u'ங',u'ர',u'ப',u'ம'], 
u'ர' : [u'ழ',u'ல',u'த',u'ம'], 
u'ழ' : [u'ந',u'த',u'ர'], 
}
