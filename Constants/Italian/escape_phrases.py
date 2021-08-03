escape_phrases =[
    'ha cambiato l\'oggetto da ',
    'Il codice sicurezza di',
    'ha abbandonato',
    'è stato aggiunto',
    'ha cambiato numero.',
    'Hai revocato il link',
    'ha cambiato l\'immagine del gruppo',
    'ha creato il gruppo “',
   ' Ora sei un amministratore',
    'I messaggi inviati a questo gruppo sono ora protetti con la crittografia end-to-end. Tocca per maggiori info.',
    'è entrato usando il link d\'invito al gruppo'
]

add_phrase = 'ha aggiunto'

rem_phrase = 'ha rimosso'

# test = '''18/06/17, 21:16 - Andrea Frenda: <Media omessi>
# 18/06/17, 21:19 - Pierpaolo Battigaglia: Nome - cognome Pier Battigaglia
# Data di nascita 19/07/1992
# Altezza poca
# Peso troppo
# Ruolo ala
# Partite giocate in serie A domanda stupida
# Partite giocate in serie B tante ma se sommiamo i minuti una
# Partite giocate in serie C sempre MaN of the match
# Proprio punto di forza in campo dare panzate
# Proprio punto debole in campo niente
# Obiettivo personale per prossima stagione dimagrire
# Obiettivo nella e con la squadra dimagrire con frenda
# Infortuni subiti tamponato da zingari'''

# test = test.split('\n')
# import re
# # for index, line in enumerate(test):
# #     pattern = re.compile("[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9], [0-9][0-9]:[0-9][0-9] - (.*):")
# #     print(index, pattern.match(line))
#
# def is_formatted (line):
#     pattern = re.compile("[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9], [0-9][0-9]:[0-9][0-9] - (.*):")
#     return pattern.match(line) != None
#
# index = 0
# end = len(test)-1
# while index < end:
#     curr_line = test[index]
#     next_line = test[index+1]
#
#     if is_formatted(next_line):
#         print('*A*', curr_line)
#         index+=1
#     else:
#         line_to_save=""
#         multiline_mode = True
#         while multiline_mode :
#             line_to_save += curr_line.replace('\n', ' ') + ' '
#             index+=1
#             if index > end-1:
#                 line_to_save += next_line.replace('\n', ' ') + ' '
#                 print('*B*', line_to_save.rstrip())
#                 index = end+2
#                 break
#             if is_formatted(next_line):
#                 multiline_mode=False
#                 print('*B*', line_to_save.rstrip())
#             else:
#                 curr_line= test[index]
#                 next_line= test[index+1]
